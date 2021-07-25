# NO... pls Dont.. Not yet

from discord.ext import commands
import discord
import urllib
import aiohttp
from config import *

class voter(commands.Cog):
    def __init__(self, bot, **kwargs):
        self.bot = bot

    @commands.command(
        help = ('get voters'),
        name = 'voters',
        description = 'get voters',
    )
    async def voters(self,ctx, *, input_params):
        await ctx.message.add_reaction(WAITING_EMOJI)

        try:
            headers = {
               'Authorization': TOPGG_TOKEN 
            }
            async with aiohttp.ClientSession(headers=headers) as session:
                async with session.get(VOTER_API_LINK) as r:
                    print(r)
                    if "application/json" in r.headers["Content-Type"]:
                        json_out = await r.json()
                        await ctx.reply(f"{json_out}")
                        pass
                        await ctx.message.add_reaction(ERROR_EMOJI)
                        
        except Exception as e:
            print(str(e))

def setup(bot):
    bot.add_cog(voter(bot))