from discord.ext import commands
import discord
import urllib
import aiohttp
import datetime

class GraphingCommandEmbed(commands.Cog):
    def __init__(self, bot, **kwargs):
        self.bot = bot

    @commands.command(
        aliases = ['threeDgraphembed','3dgrembed','3dgraphembed','3dgrem']
    )
    async def threeD_graph_embed(self,ctx, *, input_params):
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

                        embed = discord.Embed(title = f'the graph',color=0x11ffcc,url = ReqUrl_3D)
                        file = discord.File("renders/3D_graph.png")
                        embed.set_image(url="attachment://3D_graph.png")
                        embed.timestamp = datetime.datetime.utcnow()
                        embed.set_footer(text=f'rendered by {ctx.author.name}',icon_url=ctx.author.avatar_url)
                        await ctx.reply(embed=embed, file=file)

                    if "application/json" in r.headers["Content-Type"]:
                        json_out = await r.json()

                        embed=discord.Embed(color=0xff0000)
                        embed.add_field(name="Error:", value=f"{json_out['error']}", inline=False)
                        embed.add_field(name="Error_ID:", value=f"{json_out['error_id']}", inline=False)
                        embed.add_field(name="Fix:", value=f"{json_out['fix']}", inline=False)
                        embed.timestamp = datetime.datetime.utcnow()
                        embed.set_footer(text=f'rendered by {ctx.author.name}',icon_url=ctx.author.avatar_url)
                        await ctx.reply(embed=embed)

        except Exception as e:
            print(str(e))

def setup(bot):
    bot.add_cog(GraphingCommandEmbed(bot))