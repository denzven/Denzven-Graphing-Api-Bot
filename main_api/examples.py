# this is the cog that gives examples

# Imports
import guilded
from guilded.ext import commands

# Config
from config import *

class Examples(commands.Cog):
    def __init__(self, bot, **kwargs):
        self.bot = bot

    @commands.command(
        aliases = [],
        help = ('Get Examples'),
        name = 'Examples',
        description = 'get Examples',
    )

    async def Examples(self,ctx, *, input_params):
        print('code')

def setup(bot):
    bot.add_cog(Examples(bot))