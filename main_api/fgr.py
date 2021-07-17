from discord.ext import commands
import discord
import urllib
import aiohttp

class GraphingCommand(commands.Cog):
    def __init__(self, bot, **kwargs):
        self.bot = bot

    @commands.command(
        aliases = ['flatgraph','flatgr','fgraph','fgr']
    )
    async def flat_graph(self,ctx, *, input_params):
        ApiBaseUrl = "https://denzven.pythonanywhere.com"
        ApiBaseUrl_Flat = ApiBaseUrl + "/DenzGraphingApi/v1/flat_graph/test/plot"
        params = input_params.split(' ')
        i = 0
        for e in params:
            if i == 0:
                e = urllib.parse.quote(e, safe='')
                ReqUrl_Flat = ApiBaseUrl_Flat + f"?formula={e}"
                i += 1
            else:
                ReqUrl_Flat = ReqUrl_Flat + f"&{e}"

        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(ReqUrl_Flat) as r:
                    if "image/png" in r.headers["Content-Type"]:
                        file = open("renders/flat_graph.png", "wb")
                        file.write(await r.read())
                        file.close()
                        await ctx.reply(file=discord.File('renders/flat_graph.png'))
                    if "application/json" in r.headers["Content-Type"]:
                        json_out = await r.json()
                        await ctx.reply(f"**Error!** \n error = {json_out['error']} \n error_id = {json_out['error_id']} \n fix = {json_out['fix']}")

        except Exception as e:
            print(str(e))

def setup(bot):
    bot.add_cog(GraphingCommand(bot))