import datetime
from discord.ext import commands, tasks
import discord
import bot
import re
import json

UTC = datetime.timezone.utc

TIME = datetime.time(hour=5, minute=0, tzinfo=UTC) 

class update(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.my_task.start()

    def cog_unload(self):
        self.my_task.cancel()

    @tasks.loop(time=TIME)
    async def my_task(self):
        with open(f'./data/{bot.ctx.guild.id}.json', 'rw') as f:
            data = json.load(f)
            if data['daily_quotes'] == None:
                 return
            temp_history = []
            async for message in data['quotes_chat'].history(limit=None):
                    if re.match(bot.QUOTE_FORMAT, message.content) and message.author != bot.user:
                        temp_history.append(message)
            data['history'] = temp_history
            json.dump(data, f)

async def setup(bot):
    await bot.add_cog(update(bot))