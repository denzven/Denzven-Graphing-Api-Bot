from discord.ext import commands
import discord
import urllib
import aiohttp

class threeDgr(commands.Cog):
    def __init__(self, bot, **kwargs):
        self.bot = bot

    @commands.command(
         aliases = ['threeDgraph','threeDgr','3dgraph','3dgr']
    )
    async def threeD_graph(self,ctx, *, input_params):
        ApiBaseUrl = "https://denzven.pythonanywhere.com"
        ApiBaseUrl_3DGraph = ApiBaseUrl + "/DenzGraphingApi/v1/threeD_graph/test/plot"
        params = input_params.split(' ')
        i = 0
        for e in params:
            if i == 0:
                e = urllib.parse.quote(e, safe='')
                ReqUrl_3D = ApiBaseUrl_3DGraph + f"?formula={e}"
                i += 1
            else:
                ReqUrl_3D = ReqUrl_3D + f"&{e}"

        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(ReqUrl_3D) as r:
                    if "image/png" in r.headers["Content-Type"]:
                        file = open("renders/3D_graph.png", "wb")
                        file.write(await r.read())
                        file.close()
                        await ctx.reply(file=discord.File('renders/3D_graph.png'))
                    if "application/json" in r.headers["Content-Type"]:
                        json_out = await r.json()
                        await ctx.reply(f"**Error!** \n error = {json_out['error']} \n error_id = {json_out['error_id']} \n fix = {json_out['fix']}")

        except Exception as e:
            print(str(e))

def setup(bot):
    bot.add_cog(threeDgr(bot))