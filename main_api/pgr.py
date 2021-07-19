from discord.ext import commands
import discord
import urllib
import aiohttp
from config import *

class GraphingCommand(commands.Cog):
    def __init__(self, bot, **kwargs):
        self.bot = bot

    @commands.command(
        aliases = ['polargraph','polargr','pgraph','pgr'],
        help = ('Plot Polar graphs providing a formuala with x and y')

    )
    async def polar_graph(self,ctx, *, input_params):
        ApiBaseUrl = API_BASE_LINK
        ApiBaseUrl_polar = ApiBaseUrl + "/DenzGraphingApi/v1/polar_graph/test/plot"
        params = input_params.split(' ')
        i = 0
        for e in params:
            if i == 0:
                e = urllib.parse.quote(e, safe='')
                ReqUrl_polar = ApiBaseUrl_polar + f"?formula={e}"
                i += 1
            else:
                ReqUrl_polar = ReqUrl_polar + f"&{e}"

        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(ReqUrl_polar) as r:
                    if "image/png" in r.headers["Content-Type"]:
                        file = open("renders/polar_graph.png", "wb")
                        file.write(await r.read())
                        file.close()
                        await ctx.reply(file=discord.File('renders/polar_graph.png'))
                    if "application/json" in r.headers["Content-Type"]:
                        json_out = await r.json()
                        await ctx.reply(f"**Error!** \n error = {json_out['error']} \n error_id = {json_out['error_id']} \n fix = {json_out['fix']}")

        except Exception as e:
            print(str(e))

def setup(bot):
    bot.add_cog(GraphingCommand(bot))