import datetime
from datetime import date
from discord.ext import commands, tasks
import discord
import bot
import re
import random
import json

UTC = datetime.timezone.utc

TIME = datetime.time(hour=0, minute=0, tzinfo=UTC) 

class time(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.my_task.start()

    def cog_unload(self):
        self.my_task.cancel()

    @tasks.loop(time=TIME)
    async def my_task(self):
        with open(f'./data/{bot.ctx.guild.id}.json', 'r') as f:
            data = json.load(f)
        if data['daily_quotes'] == None:
            print("no daily quotes")
            return
        else:
            random_quote = random.choice(data['history'])
            speaker = random_quote.mentions[0].display_name
            author = random_quote.author
            quote = re.match(bot.QUOTE_ONLY, random_quote.content)
            qdate = random_quote.created_at.strftime("%d/%m/%Y")
            await bot.DAILY_QUOTES.send(f"QUOTE OF THE DAY {date.today()}:\n@{speaker} said: {quote[0]} on {qdate}.")


async def setup(bot):
    await bot.add_cog(time(bot))
