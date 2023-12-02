import discord
import responses
import os
from dotenv import load_dotenv
from discord.ext import commands, tasks
import re
import random
import datetime
import json

bot = commands.Bot(command_prefix='!q', intents=discord.Intents.all())

QUOTE_FORMAT = re.compile('".*".*')
QUOTE_ONLY = re.compile('".*"')

async def load():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')

async def run_discord_bot():
    async with bot:
        load_dotenv()
        await load()
        await bot.start(os.getenv('TOKEN'))

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def set(ctx):
    if not os.path.isfile(f'./data/{ctx.guild.id}.json'):
            data = {
                'quotes_chat': ctx.channel,
                'daily_quotes': None,
                'history': []
            }
            with open(f'./data/{ctx.guild.id}.json', 'w') as f:
                json.dump(data, f)
    with open(f'./data/{ctx.guild.id}.json', 'rw') as f:
        data = json.load(f)
        data['quotes_chat'] = ctx.channel
        if data['history'] == []:
            async for message in data['quotes_chat'].history(limit=None):
                if re.match(QUOTE_FORMAT, message.content) and message.author != bot.user:
                    data['history'].append(message)
        await ctx.send(f"#{data['quotes_chat']} has been set as the quotes chat.")
        json.dump(data, f)

@bot.command()
async def rand(ctx):
    with open(f'./data/{ctx.guild.id}.json', 'rw') as f:
        data = json.load(f)
        if data['quotes_chat'] == None:
            await ctx.send('No quotes chat has been set.')
        else:
            if data['history'] == []:
                async for message in ctx.channel.history(limit=None):
                    if re.match(QUOTE_FORMAT, message.content) and message.author != bot.user:
                        data['history'].append(message)
            await ctx.send(f"#{data['quotes_chat']} has been set as the quotes chat.")
            random_quote = random.choice(data['history'])
            speaker = random_quote.mentions[0].display_name
            author = random_quote.author
            quote = re.match(QUOTE_ONLY, random_quote.content)
            date = random_quote.created_at.strftime("%d/%m/%Y")

        await ctx.send(f'@{speaker} said: {quote[0]} on {date}.')
        json.dump(data, f)

@bot.command()
async def daily(ctx):
    with open(f'./data/{ctx.guild.id}.json', 'rw') as f:
        data = json.load(f)
        data['daily_quotes'] = ctx.channel.id
        await ctx.send(f"#{data['data_quotes']} has been set as the daily quotes chat.")
        json.dump(data, f)


        
          