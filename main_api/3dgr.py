# this is the cog that handles three-D graphs (without embeds)

# imports
from discord.ext import commands
import discord
import urllib
import aiohttp

# Config
from config import *

class GraphingCommand_3d(commands.Cog):
    def __init__(self, bot, **kwargs):
        self.bot = bot

    @commands.command(
        aliases = ['threeDgraph','threeDgr','3dgraph','3dgr'],
        help = ('Plot three-dimensional graphs providing a formuala with x and y (z is NOT supported)'),
        name = '3D_Graph',
        description = 'Plot 3D Graphs with this command',
    )
    
    async def threeD_graph(self,ctx, *, input_params):
        await ctx.message.add_reaction(WAITING_EMOJI)
        ApiBaseUrl = API_BASE_LINK
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
                        pass
                        await ctx.message.add_reaction(DONE_EMOJI)
                        
                    if "application/json" in r.headers["Content-Type"]:
                        json_out = await r.json()
                        await ctx.reply(f"**Error!** \n error = {json_out['error']} \n error_id = {json_out['error_id']} \n fix = {json_out['fix']}", allowed_mentions=discord.AllowedMentions.none())
                        pass
                        await ctx.message.add_reaction(ERROR_EMOJI)

        except Exception as e:
            print(str(e))

def setup(bot):
    bot.add_cog(GraphingCommand_3d(bot))