# this is the cog that handles derivative graphs (with embeds)

# Imports
from discord.ext import commands
import discord
import urllib
import aiohttp
import datetime

# Config
from config import *
from utils.custom_checks import voter_only


class GraphingCommandEmbed_derivative(commands.Cog):
    def __init__(self, bot, **kwargs):
        self.bot = bot

    @commands.command(
        aliases = ['derivativegraphembed','derivativegrembed','dgraphembed','dgrem'],
        help = ('Plot derivative graphs providing a formuala with x and y, inside cool looking embeds'),
        name = 'derivative_Graph_Embed',
        description = 'Plot derivative Graphs in Embeds with this command',
    )
    @voter_only()
    async def derivative_graph_embed(self,ctx, *, input_params):
        await ctx.message.add_reaction(WAITING_EMOJI)
        async with ctx.typing():
            ApiBaseUrl = API_BASE_LINK
            ApiBaseUrl_derivative = ApiBaseUrl + "/DenzGraphingApi/v1/derivative_graph/test/plot"
            params = input_params.split(' ')
            i = 0
    
            for e in params:
                if i == 0:
                    e = urllib.parse.quote(e, safe='')
                    ReqUrl_derivative = ApiBaseUrl_derivative + f"?formula={e}"
                    i += 1
                    
                else:
                    ReqUrl_derivative = ReqUrl_derivative + f"&{e}"
    
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get(ReqUrl_derivative) as r:
                    
                        if "image/png" in r.headers["Content-Type"]:
                            file = open("renders/derivative_graph.png", "wb")
                            file.write(await r.read())
                            file.close()
    
                            embed = discord.Embed(title = f'the graph',color=MAIN_COLOR,url = ReqUrl_derivative)
                            file = discord.File("renders/derivative_graph.png")
                            embed.set_image(url="attachment://derivative_graph.png")
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
    bot.add_cog(GraphingCommandEmbed_derivative(bot))