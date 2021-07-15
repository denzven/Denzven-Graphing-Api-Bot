from discord.ext import tasks
import random
from list.statuslist import inputstatus
from discord.ext import commands
import discord
import asyncio

class Tasks(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.status_task.start()
 
    @tasks.loop(seconds=60) # <- will do this every 5 seconds
    async def status_task(self):
        self.bot.ping = round(self.bot.latency * 1000)
        random_status = random.choice(inputstatus)
        await self.bot.change_presence(activity=discord.Game(
        name=
            f">help | Guilds: {len(self.bot.guilds)} | Members: {len(self.bot.users)} | Ping: {self.bot.ping} ms"))
        await self.bot.change_presence(activity=discord.Activity(
            type=discord.ActivityType.playing, name=f"{random_status}"))
            
def setup(bot):
	bot.add_cog(Tasks(bot))