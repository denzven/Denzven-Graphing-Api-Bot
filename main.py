# Welcome! This is an Example Bot in Dicord.py,
# that showcases the use of the DenzGraphingApi,
# to form embeds and send basic info
# you can invite the bot here: https://dsc.gg/denzgraphingapi-bot
# for doubts and queries Join the support/chill server: 

import discord
from discord.ext import commands
import os
import urllib.parse
import aiohttp
#from keep_alive import keep_alive
from API_Formula_Examples import API_Formula_Examples
import datetime
import Denzven_Graphing_Api_Wrapper as GraphingApi #pip install

description = 'description'
intents = discord.Intents.all()
intents.members = True
intents.presences = True
bot = commands.Bot(
    command_prefix=commands.when_mentioned_or(">"),
    intents=discord.Intents.all(),
    case_insensitive=True,
    strip_after_prefix=True,
    allowed_mentions=discord.AllowedMentions.none())

@bot.event
async def on_connect():
	print("the bot is ready")

@bot.event
async def on_ready():
	print(f'We have logged in as {bot.user}')

@bot.event
async def on_command(ctx):
	server = ctx.guild.name
	channel = ctx.channel
	user = ctx.author
	command = ctx.command
	print(f'{server} > {channel} > {user} > {command}')

@bot.event
async def on_command_error(ctx, error):
	#raise error
    if isinstance(error,commands.BadArgument):
        await ctx.send('BadArgument')
    if isinstance(error, commands.errors.CommandInvokeError):
        await ctx.reply("CommandInvokeError")
    if isinstance(error, commands.CommandNotFound):
        await ctx.reply("CommandNotFound")
    if isinstance(error,commands.errors.CommandOnCooldown):
        await ctx.reply(f"CommandOnCooldown retry after {error.retry_after:.2f}s.")
    if isinstance(error, commands.errors.MissingPermissions):
        await ctx.reply(f"MissingPermissions {' '.join(error.missing_perms[0].split('_')).title()}")
        return
    if isinstance(error,commands.MissingRequiredArgument):
        await ctx.reply('MissingRequiredArgument')
    if isinstance(error, commands.BotMissingPermissions):
        if error.missing_perms[0] == 'send_messages':
            return
        await ctx.reply(f"BotMissingPermissions **{' '.join(error.missing_perms[0].split('_')).title()}**")

@bot.command()
async def ping(ctx):
	await ctx.send(f"ping ---> {round(bot.latency * 1000)} ms")

@bot.command(
    aliases = ['pyg']
)
async def pythonanywhere_graph(ctx, formula):
    url = GraphingApi.py_anywhere_graph(formula)
    await ctx.send(url)

@bot.command(
    aliases = ['hg']
)
async def heroku_graph(ctx, formula):
    url = GraphingApi.heroku_graph(formula)
    await ctx.send(url)

@bot.command(
    aliases = ['pyem']
)
async def pythonanywhere_graph_with_Embed(ctx, formula):
    url = GraphingApi.py_anywhere_graph(formula)
    embed = discord.Embed(title = f' the graphical representation of \n ```{formula} = 0```',color = discord.Color.green(),url = url)
    embed.set_image(url = url)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text=f'rendered by {ctx.author.name}',icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

@bot.command(
    aliases = ['hgem']
)
async def heroku_graph_with_Embed(ctx, formula):
    url = GraphingApi.heroku_graph(formula)
    embed = discord.Embed(title = f' the graphical representation of \n ```{formula} = 0```',color = discord.Color.green(),url = url)
    embed.set_image(url = url)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text=f'rendered by {ctx.author.name}',icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

@bot.command(
    aliases = ['fgr']
)
async def async_file_graph(ctx,formula_input):
    file = GraphingApi.async_file_graph(formula_input)
    await ctx.send(file=discord.File(file))

@bot.command(
    aliases = ['pyb']
)
async def pythonanywhere_graph_beta(ctx, *, stuff):
    python_anywhere_beta_BASEURL = "http://denzven.pythonanywhere.com/DenzGraphingApi/v1/flat_graph/test/plot"
    #url = python_anywhere_beta_BASEURL + "http://denzven.pythonanywhere.com/DenzGraphingApi/v1/flat_graph/test/plot"
    params = stuff.split(' ')
    i = 0
    for e in params:
        if i == 0:
            e = urllib.parse.quote(e, safe='')
            python_anywhere_beta_BASEURL = python_anywhere_beta_BASEURL + f"?formula={e}"
            i += 1
        if i != 0:
            python_anywhere_beta_BASEURL = python_anywhere_beta_BASEURL + f"&{e}"
    await ctx.send(python_anywhere_beta_BASEURL)

@bot.command(
    aliases = ['pybem']
)
async def pythonanywhere_graph_beta_embed(ctx, *, stuff):
    python_anywhere_beta_BASEURL = "http://denzven.pythonanywhere.com/DenzGraphingApi/v1/flat_graph/test/plot"
    #url = python_anywhere_beta_BASEURL + "http://denzven.pythonanywhere.com/DenzGraphingApi/v1/flat_graph/test/plot"
    params = stuff.split(' ')
    i = 0
    for e in params:
        if i == 0:
            e = urllib.parse.quote(e, safe='')
            python_anywhere_beta_BASEURL = python_anywhere_beta_BASEURL + f"?formula={e}"
        else:
            python_anywhere_beta_BASEURL = python_anywhere_beta_BASEURL + f"&{e}"
        i += 1

    url = python_anywhere_beta_BASEURL
    embed = discord.Embed(title = f'the graph',color = discord.Color.green(),url = url)
    embed.set_image(url = url)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text=f'rendered by {ctx.author.name}',icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

@bot.command()
async def examples(ctx):
    await ctx.send(API_Formula_Examples)

@bot.command()
async def github(ctx):
    await ctx.send("https://github.com/denzven/DenzGraphingApiWrapper_py")

@bot.command()
async def docs(ctx):
    await ctx.send("https://denzgraphingapiwrapper-py.readthedocs.io/en/latest/")

@bot.command()
async def website(ctx):
    await ctx.send("https://denzven.pythonanywhere.com")

@bot.command()
async def pypi(ctx):
    await ctx.send("https://pypi.org/project/DenzGraphingApiWrapper-py/")

@bot.command()
async def test_pypi(ctx):
    await ctx.send("https://test.pypi.org/project/DenzGraphingApiWrapper-py-denzven/")

@bot.command()
async def code(ctx):
    await ctx.send(file = discord.File(r'main.py'), content = "Here is the Code of This Bot")

#################################################

#keep_alive()	
bot.run(os.environ['bottoken'])