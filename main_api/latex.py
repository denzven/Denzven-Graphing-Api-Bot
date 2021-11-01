# this is the cog that handles three-D graphs (without embeds)

# imports
import guilded
from guilded.ext import commands
import urllib
import aiohttp

# Config
from config import *

class Latex(commands.Cog):
    def __init__(self, bot, **kwargs):
        self.bot = bot

    @commands.command(
        aliases = ['tex'],
        help = ('render Latex'),
        name = 'Latex',
        description = 'render latex',
    )
    
    async def latex(self,ctx, *, input_params):
        await ctx.message.add_reaction(WAITING_EMOJI)
        async with ctx.typing():
            ApiBaseUrl = API_BASE_LINK
            ApiBaseUrl_Latex = ApiBaseUrl + "/DenzGraphingApi/v1/latex/test/plot"
            params = input_params.split(' ')
            i = 0

            for e in params:
                if i == 0:
                    e = urllib.parse.quote(e, safe='')
                    ReqUrl_Latex = ApiBaseUrl_Latex + f"?text={e}"
                    i += 1

                else:
                    ReqUrl_Latex = ReqUrl_Latex + f"&{e}"

            try:
                print(ReqUrl_Latex)
                async with aiohttp.ClientSession() as session:
                    async with session.get(ReqUrl_Latex) as r:

                        if "image/png" in r.headers["Content-Type"]:
                            print("gmmm")
                            file = open("renders/latex.png", "wb")
                            file.write(await r.read())
                            file.close()
                            await ctx.reply(file=discord.File('renders/latex.png'))
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
    bot.add_cog(Latex(bot))