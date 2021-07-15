# Welcome! This is an Example Bot in Dicord.py,
# that showcases the use of the DenzGraphingApi,
# to form embeds and send basic info
# you can invite the bot here: https://dsc.gg/denzven-graphing-api-bot
# for doubts and queries Join the support/chill server: 
# https://dsc.gg/chilly_place

import discord
from discord.ext import commands
import os
import random
import asyncio
import json
#import Denzven_Graphing_Api_Wrapper as GraphingApi #pip install

from list.statuslist import inputstatus
from list.cog_list import cogs
#from keep_alive import keep_alive

#################################################################################################################

class GraphingBot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.CommandNumber = 0
        self.prefixes_cache = []
        self.ping = 0
        self.ApiBaseUrl = "https://denzven.pythonanywhere.com"

    async def get_custom_prefix(bot, message):
        prefixes_ = [f'<@{bot.user.id}> ', f'<@!{bot.user.id}> ']
        with open("prefixes.json") as f:
            prefixes = json.load(f)

        prefixes_.append(">" if str(message.guild.id) not in prefixes else prefixes[str(message.guild.id)])
        return prefixes_

#################################################################################################################

description = 'description'
intents = discord.Intents.all()
intents.members = True
intents.presences = True
bot = GraphingBot(
    #command_prefix=commands.when_mentioned_or(">"),
    command_prefix=GraphingBot.get_custom_prefix,
    intents=discord.Intents.all(),
    case_insensitive=True,
    strip_after_prefix=False,
    allowed_mentions=discord.AllowedMentions.none())


#################################################################################################################

bot.load_extension('jishaku') # pip install -U jishaku

@bot.event
async def on_connect():
    print('+--------------------------------------------------+')
    print('|                 Bot has Connected                |')
    print('+--------------------------------------------------+')

@bot.event
async def on_ready():
    print('+--------------------------------------------------+')
    print('|                 Bot has Started                  |')
    print('+--------------------------------------------------+')
    print('| logged in as: {}   |'.format(bot.user))
    print('+--------------------------------------------------+')
    print('| No. of Servers: {}                                |'.format(len(bot.guilds)))
    print('| No. of Users: {}                                |'.format(len(bot.users)))
    print('| Bot Prefix: ">"                                  |')
    print('| Bot made by: @Denzven#2004                       |')
    print('| Join my chill server: https://dsc.gg/chilly_place|')
    print('+--------------------------------------------------+')
    print('\n\n\n')
    with open("prefixes.json","r") as f:
        GraphingBot.prefixes_cache = json.load(f)
        print('prefixes havs loaded')

    for cog in cogs:
        try:
            bot.load_extension(cog)
            print(f"{cog} has loaded")
        except Exception as e:
            print(f"{cog} has not been loaded")
            print(e)

#################################################################################################################

@bot.command()
async def ping(ctx):
    bot.ping = round(bot.latency * 1000)
    await ctx.send(f"ping ---> {bot.ping} ms")
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