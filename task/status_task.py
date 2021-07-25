# This is a fun little task that changes the status of the bot randomly

# Imports
from discord.ext import commands
from discord.ext import tasks
import random
import discord
import asyncio

# Config
from config import *

class Tasks(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.status_task.start()
 
    @tasks.loop(seconds=120)
    async def status_task(self):

        self.bot.ping = round(self.bot.latency * 1000)
        random_status = random.choice(inputstatus)
        await self.bot.change_presence(activity=discord.Game(
        name = f">help | Guilds: {len(self.bot.guilds)} | Members: {len(self.bot.users)} | Ping: {self.bot.ping} ms"))
        await asyncio.sleep(60)
        await self.bot.change_presence(activity=discord.Activity(
            type=discord.ActivityType.playing, name=f"{random_status}"))
            
def setup(bot):
	bot.add_cog(Tasks(bot))