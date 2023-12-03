import datetime
from datetime import date
from discord.ext import commands, tasks
import discord
from bot import DICT
import bot
import re
import random
import json

UTC = datetime.timezone.utc

TIME = datetime.time(hour=1, minute=5, tzinfo=UTC) 
class time(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.my_task.start()

    def cog_unload(self):
        self.my_task.cancel()

    @tasks.loop(time=TIME)
    async def my_task(self):
        async for guild in self.bot.fetch_guilds(limit=None):
            data = DICT[guild.id]

            if data['daily_quotes'] == None:
                print("no daily quotes")
                return
            else:
                if data['history'] == []:
                    async for message in data['quotes_chat'].history(limit=None):
                        if re.match(bot.QUOTE_FORMAT, message.content) and message.author != bot.user:
                            data['history'].append(message)
                random_quote = random.choice(data['history'])
                speaker = random_quote.mentions[0].display_name
                author = random_quote.author
                quote = re.match(bot.QUOTE_ONLY, random_quote.content)
                qdate = random_quote.created_at.strftime("%d/%m/%Y")
                await data['daily_quotes'].send(f"QUOTE OF THE DAY {date.today()}:\n@{speaker} said: {quote[0]} on {qdate}.")
                DICT[guild.id] = data

async def setup(bot):
    await bot.add_cog(time(bot))
