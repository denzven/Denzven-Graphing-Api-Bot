# this is the cog that handles Flat graphs (with embeds)

# Imports
from discord.ext import commands
import discord
import urllib
import aiohttp
import datetime

# Config
from config import *

class GraphingCommandEmbed_flat(commands.Cog):
    def __init__(self, bot, **kwargs):
        self.bot = bot

    @commands.command(
        aliases = ['flatgraphembed','flatgrembed','fgraphembed','fgrem'],
        help = ('Plot Flat graphs providing a formula with x and y, inside cool looking embeds'),
        name = 'Flat_Graph_Embed',
        description = 'Plot Flat Graphs in Embeds with this command',
    )

    async def flat_graph_embed(self,ctx, *, input_params):
        await ctx.message.add_reaction(WAITING_EMOJI)
        async with ctx.typing():
            ApiBaseUrl = API_BASE_LINK
            ApiBaseUrl_flat = ApiBaseUrl + "/DenzGraphingApi/v1/flat_graph/test/plot"
            params = input_params.split(' ')
            i = 0
    
            for e in params:
                if i == 0:
                    e = urllib.parse.quote(e, safe='')
                    ReqUrl_flat = ApiBaseUrl_flat + f"?formula={e}"
                    i += 1
                    
                else:
                    ReqUrl_flat = ReqUrl_flat + f"&{e}"
    
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get(ReqUrl_flat) as r:
                    
                        if "image/png" in r.headers["Content-Type"]:
                            file = open("renders/flat_graph.png", "wb")
                            file.write(await r.read())
                            file.close()
    
                            embed = discord.Embed(title = f'the graph',color=MAIN_COLOR,url = ReqUrl_flat)
                            file = discord.File("renders/flat_graph.png")
                            embed.set_image(url="attachment://flat_graph.png")
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
    bot.add_cog(GraphingCommandEmbed_flat(bot))