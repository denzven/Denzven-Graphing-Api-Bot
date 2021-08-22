# this is the cog that handles three-D graphs (with embeds)

# Imports
from discord.ext import commands
import discord
import urllib
import aiohttp
import datetime

# Config
from config import *

class GraphingCommandEmbed_3d(commands.Cog):
    def __init__(self, bot, **kwargs):
        self.bot = bot

    @commands.command(
        aliases = ['threeDgraphembed','3dgrembed','3dgraphembed','3dgrem'],
        help = ('Plot three-dimensional graphs providing a formula with x and y insude beautiful embeds (z is NOT supported)'),
        name = '3D_Graph_Embed',
        description = 'Plot 3D Graphs in Embeds with this command',
    )

    async def threeD_graph_embed(self,ctx, *, input_params):
        await ctx.message.add_reaction(WAITING_EMOJI)
        async with ctx.typing():
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
    
                            embed = discord.Embed(title = f'the graph',color=MAIN_COLOR,url = ReqUrl_3D)
                            file = discord.File("renders/3D_graph.png")
                            embed.set_image(url="attachment://3D_graph.png")
                            embed.timestamp = datetime.datetime.utcnow()
                            embed.set_footer(text=f'rendered by {ctx.author.name}',icon_url=ctx.author.avatar.url)
                            await ctx.reply(embed=embed, file=file)
                            pass
                            await ctx.message.add_reaction(DONE_EMOJI)
    
                        if "application/json" in r.headers["Content-Type"]:
                            json_out = await r.json()
    
                            embed=discord.Embed(color=ERROR_COLOR)
                            embed.add_field(name="Error:", value=f"{json_out['error']}", inline=False)
                            embed.add_field(name="Error_ID:", value=f"{json_out['error_id']}", inline=False)
                            embed.add_field(name="Fix:", value=f"{json_out['fix']}", inline=False)
                            embed.timestamp = datetime.datetime.utcnow()
                            embed.set_footer(text=f'rendered by {ctx.author.name}',icon_url=ctx.author.avatar.url)
                            await ctx.reply(embed=embed)
                            pass
                            await ctx.message.add_reaction(ERROR_EMOJI)
    
            except Exception as e:
                print(str(e))

def setup(bot):
    bot.add_cog(GraphingCommandEmbed_3d(bot))