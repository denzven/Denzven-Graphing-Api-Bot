import discord
import urllib
import aiohttp
import json
import datetime

from config import *

async def fetchgraph(ctx, input_params, ApiBaseUrl, PathUrl, filename, spliter, WAITING_EMOJI, DONE_EMOJI, ERROR_EMOJI, MAIN_COLOR, ERROR_COLOR, IsEmbed=False):
    await ctx.message.add_reaction(WAITING_EMOJI)
    async with ctx.typing():
        ApiBaseUrl += PathUrl
        params = input_params.split(spliter)
        i = 0
        for e in params:
            if i == 0:
                e = urllib.parse.quote(e, safe='')
                ReqUrl = ApiBaseUrl + f"?formula={e}"
                i += 1
            else:
                ReqUrl += f"&{e}"
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(ReqUrl) as r:
                    if "image/png" in r.headers["Content-Type"]:
                        file = open(f"renders/{filename}.png", "wb")
                        file.write(await r.read())
                        file.close()

                        if IsEmbed is False:
                            await ctx.reply(file=discord.File(f"renders/{filename}.png"))
                            pass
                            await ctx.message.add_reaction(DONE_EMOJI)

                        if IsEmbed is True:
                            embed = discord.Embed(title = f'the graph',color=MAIN_COLOR,url = ReqUrl)
                            file = discord.File(f"renders/{filename}.png")
                            embed.set_image(url=f"attachment://{filename}.png")
                            embed.timestamp = datetime.datetime.utcnow()
                            embed.set_footer(text=f"rendered by {ctx.author.name}",icon_url=ctx.author.avatar.url)
                            await ctx.reply(embed=embed, file=file)
                            pass
                            await ctx.message.add_reaction(DONE_EMOJI)

                    if "application/json" in r.headers["Content-Type"]:
                        json_out = await r.json()

                        if IsEmbed is False:
                            await ctx.reply(f"**Error!** \n error = {json_out['error']} \n error_id = {json_out['error_id']} \n fix = {json_out['fix']}", allowed_mentions=discord.AllowedMentions.none())
                            pass
                            await ctx.message.add_reaction(ERROR_EMOJI)

                        if IsEmbed is True:
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