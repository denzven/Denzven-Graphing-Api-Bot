# Welcome! This is an Example Bot in Dicord.py,
# that showcases the use of the DenzGraphingApi,
# to form embeds and send basic info
# you can invite the bot here: https://dsc.gg/denzven-graphing-api-bot
# for doubts and queries Join the support/chill server: 
# https://dsc.gg/chilly_place

import discord
from discord.ext import commands
import os
import urllib.parse
import random
import aiohttp
import asyncio
from statuslist import inputstatus
#from keep_alive import keep_alive
import datetime
#import Denzven_Graphing_Api_Wrapper as GraphingApi #pip install

#################################################################################################################

description = 'description'
intents = discord.Intents.all()
intents.members = True
intents.presences = True
bot = commands.Bot(
    command_prefix=commands.when_mentioned_or(">"),
    intents=discord.Intents.all(),
    case_insensitive=True,
    strip_after_prefix=False,
    allowed_mentions=discord.AllowedMentions.none())

ApiBaseUrl = "https://denzven.pythonanywhere.com"

#################################################################################################################

async def status_task():
	while True:
		random_status = random.choice(inputstatus)
		await bot.change_presence(activity=discord.Game(
		    name=
		    f">help | Guilds: {len(bot.guilds)} | Members: {len(bot.users)}"))
		await asyncio.sleep(30)
		await bot.change_presence(activity=discord.Activity(
		    type=discord.ActivityType.playing, name=f"{random_status}"))
		await asyncio.sleep(30)

bot.load_extension('jishaku') # pip install -U jishaku

@bot.event
async def on_connect():
    print('+--------------------------------------------------+')
    print('|                 Bot has Connected                |')
    print('+--------------------------------------------------+')

@bot.event
async def on_ready():
    bot.loop.create_task(status_task())
    global CommandNumber
    CommandNumber = 0
    print('+--------------------------------------------------+')
    print('|                 Bot has Started                  |')
    print('+--------------------------------------------------+')
    print('| logged in as: {}   |'.format(bot.user))
    print('+--------------------------------------------------+')
    print('| No. of Servers: {}                                |'.format(len(bot.guilds)))
    print('| Bot Prefix: ">"                                  |')
    print('| Bot made by: @Denzven#2004                       |')
    print('| Join my chill server: https://dsc.gg/chilly_place|')
    print('+--------------------------------------------------+')
    print('\n\n\n')

@bot.event
async def on_command(ctx):
    global CommandNumber
    CommandNumber += 1
    server = ctx.guild.name
    channel = ctx.channel
    user = ctx.author
    command = ctx.command
    print(f'\n\n\n')
    print(f'+--------------------------------------------------+')
    print(f'| {server} > {channel} > {user} > {command}         ')
    print(f'+--------------------------------------------------+')
    print(f'| Bot-Usage: {bot.user}                             ')
    print(f'+--------------------------------------------------+')
    print(f'| Server: {server}                                  ')
    print(f'| Channel: {channel}                                ')
    print(f'| User: {user}                                      ')
    print(f'| Command: {command}                                ') 
    print(f'| Command content: {ctx.message.content}            ')
    print(f'| Command Number: {CommandNumber}                   ')
    print(f'+--------------------------------------------------+')
    print(f'\n\n\n')

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

#################################################################################################################

@bot.command(
    aliases = ['flatgraph','flatgr','fgraph','fgr']
)
async def Flat_graph(ctx, *, input_params):
    ApiBaseUrl_FlatGraph = ApiBaseUrl + "/DenzGraphingApi/v1/flat_graph/test/plot"
    params = input_params.split(' ')
    i = 0
    for e in params:
        if i == 0:
            e = urllib.parse.quote(e, safe='')
            ReqUrl_Flat = ApiBaseUrl_FlatGraph + f"?formula={e}"
            i += 1
        else:
            ReqUrl_Flat = ReqUrl_Flat + f"&{e}"

    await ctx.reply(ReqUrl_Flat)

############

@bot.command(
    aliases = ['flatgraphembed','flatgrembed','fgraphembed','fgrem']
)
async def Flat_graph_embed(ctx, *, input_params):
    ApiBaseUrl_FlatGraph = ApiBaseUrl + "/DenzGraphingApi/v1/flat_graph/test/plot"
    params = input_params.split(' ')
    i = 0
    for e in params:
        if i == 0:
            e = urllib.parse.quote(e, safe='')
            ReqUrl_Flat = ApiBaseUrl_FlatGraph + f"?formula={e}"
            i += 1
        else:
            ReqUrl_Flat = ReqUrl_Flat + f"&{e}"

    url = ReqUrl_Flat
    embed = discord.Embed(title = f'the graph',color = discord.Color.green(),url = url)
    embed.set_image(url = url)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text=f'rendered by {ctx.author.name}',icon_url=ctx.author.avatar_url)
    await ctx.reply(embed=embed)

#################################################################################################################

@bot.command(
    aliases = ['poargraph','polargr','pgraph','pgr']
)
async def Polar_graph(ctx, *, input_params):
    ApiBaseUrl_PolarGraph = ApiBaseUrl + "/DenzGraphingApi/v1/polar_graph/test/plot"
    params = input_params.split(' ')
    i = 0
    for e in params:
        if i == 0:
            e = urllib.parse.quote(e, safe='')
            ReqUrl_Polar = ApiBaseUrl_PolarGraph + f"?formula={e}"
            i += 1
        else:
            ReqUrl_Polar = ReqUrl_Polar + f"&{e}"

    await ctx.reply(ReqUrl_Polar)

###############

@bot.command(
    aliases = ['polatgraphembed','polargrembed','pgraphembed','pgrem']
)
async def Polar_graph_embed(ctx, *, input_params):
    ApiBaseUrl_PolarGraph = ApiBaseUrl + "/DenzGraphingApi/v1/polar_graph/test/plot"
    params = input_params.split(' ')
    i = 0
    for e in params:
        if i == 0:
            e = urllib.parse.quote(e, safe='')
            ReqUrl_Polar = ApiBaseUrl_PolarGraph + f"?formula={e}"
            i += 1
        else:
            ReqUrl_Polar = ReqUrl_Polar + f"&{e}"

    url = ReqUrl_Polar
    embed = discord.Embed(title = f'the graph',color = discord.Color.green(),url = url)
    embed.set_image(url = url)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text=f'rendered by {ctx.author.name}',icon_url=ctx.author.avatar_url)
    await ctx.reply(embed=embed)

#################################################################################################################
@bot.command(
     aliases = ['threeDgraph','threeDgr','3dgraph','3dgr']
)
async def threeD_graph(ctx, *, input_params):
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

    await ctx.reply(ReqUrl_3D)

#############

@bot.command(
    aliases = ['threeDgraphembed','3dgrembed','3dgraphembed','3dgrem']
)
async def threeD_graph_embed(ctx, *, input_params):
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

    url = ReqUrl_3D
    embed = discord.Embed(title = f'the graph',color = discord.Color.green(),url = url)
    embed.set_image(url = url)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text=f'rendered by {ctx.author.name}',icon_url=ctx.author.avatar_url)
    await ctx.reply(embed=embed)

#################################################################################################################

@bot.command(
    aliases = ['attr']
)
async def attributes(ctx):
    attr = '''
```
grid_value=<1|2|3>
plot_style=<0-25>
x_coord=<any>
y_coord=<any>
spine_top=<hex without #>
spine_bottom=<hex without #>
spine_left=<hex without #>
spine_right=<hex without #>
line_style=<hex without #>
grid_lines_major=<hex without #>
grid_lines_minor=<hex without #>
tick_colors=<hex without #>
axfacecolor=<hex without #>
figfacecolor=<hex without #>
title_text=<any text>  
```
    '''
    await ctx.reply(attr)

#################################################################################################################

@bot.command()
async def ping(ctx):
	await ctx.send(f"ping ---> {round(bot.latency * 1000)} ms")
@bot.command()
async def github(ctx):
    await ctx.send("https://github.com/denzven/Denzven-Graphing-Api")
@bot.command()
async def docs(ctx):
    await ctx.send("https://denzven.pythonanywhere.com/docs")
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

#################################################################################################################

#keep_alive()	
bot.run(os.environ['bottoken'])