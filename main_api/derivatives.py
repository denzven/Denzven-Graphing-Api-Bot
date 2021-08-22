# this is the cog that handles three-D graphs (without embeds)

# imports
from discord.ext import commands
import discord
import urllib
import aiohttp

# Config
from config import *
from utils.custom_checks import voter_only

class GraphingCommand_derivative(commands.Cog):
    def __init__(self, bot, **kwargs):
        self.bot = bot

    @commands.command(
        aliases = ['dgr','derivative'],
        help = ('Plot derivates of graphs providing a formula with x'),
        name = 'Derivative_Graph',
        description = 'Plot derivatives with this command',
    )
    @voter_only()
    async def derivative_graph(self,ctx, *, input_params):
        await ctx.message.add_reaction(WAITING_EMOJI)
        async with ctx.typing():
            ApiBaseUrl = API_BASE_LINK
            ApiBaseUrl_3DGraph = ApiBaseUrl + "/DenzGraphingApi/v1/derivative_graph/test/plot"
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
                            file = open("renders/derivative_graph.png", "wb")
                            file.write(await r.read())
                            file.close()
                            await ctx.reply(file=discord.File('renders/derivative_graph.png'))
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
    bot.add_cog(GraphingCommand_derivative(bot))