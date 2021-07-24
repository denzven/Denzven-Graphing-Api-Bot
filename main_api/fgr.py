from discord.ext import commands
import discord
import urllib
import aiohttp
from config import *

class GraphingCommand_flat(commands.Cog):
    def __init__(self, bot, **kwargs):
        self.bot = bot

    @commands.command(
        aliases = ['flatgraph','flatgr','fgraph','fgr'],
        help = ('Plot Flat graphs providing a formuala with x and y'),
        name = 'Flat_Graph',
        description = 'Plot Flat Graphs with this command',
    )
    async def flat_graph(self,ctx, *, input_params):
        await ctx.message.add_reaction(WAITING_EMOJI)
        ApiBaseUrl = API_BASE_LINK
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
                        pass
                        await ctx.message.add_reaction(DONE_EMOJI)
                        
                    if "application/json" in r.headers["Content-Type"]:
                        json_out = await r.json()
                        await ctx.reply(f"**Error!** \n error = {json_out['error']} \n error_id = {json_out['error_id']} \n fix = {json_out['fix']}")
                        pass
                        await ctx.message.add_reaction(ERROR_EMOJI)
                        
        except Exception as e:
            print(str(e))

def setup(bot):
    bot.add_cog(GraphingCommand_flat(bot))