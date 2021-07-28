# this is the cog that gives examples

# Imports
from discord.ext import commands
import discord
import urllib
import aiohttp
import datetime

# Config
from config import *

class Examples(commands.Cog):
    def __init__(self, bot, **kwargs):
        self.bot = bot

    @commands.command(
        aliases = [],
        help = ('Examples'),
        name = 'Examples',
        description = 'Get Examples',
    )

    async def Examples(self,ctx, *, input_params):
        print('code')

def setup(bot):
    bot.add_cog(Examples(bot))