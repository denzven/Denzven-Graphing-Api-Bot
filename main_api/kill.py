from discord.ext import commands
import discord
import urllib
import aiohttp
import os

class Kill(commands.Cog):
    def __init__(self, bot, **kwargs):
        self.bot = bot

    @commands.command(
        aliases = ['kill_switch','reset'],
        hidden=True
    )
    @commands.is_owner()
    async def Kill(self,ctx):
        passwd = os.environ['passwd']
        ReqUrl_Kill = f'https://denzven.pythonanywhere.com/reset?passwd={passwd}'
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(ReqUrl_Kill) as r:
                    print(r.headers["Content-Type"])
                    #if "application/json" in r.headers["Content-Type"]:
                    if "text/html" in r.headers["Content-Type"]:
                        await ctx.reply(f"Done")

        except Exception as e:
            print(str(e))

def setup(bot):
    bot.add_cog(Kill(bot))
    