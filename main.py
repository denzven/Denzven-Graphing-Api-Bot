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
import datetime
import re
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

    async def fetch_prefix(self, message: discord.Message):
        if not message.guild:
            return ">"

        guild_id = message.guild.id
        prefix_cache = self.prefixes_cache

        for ee in prefix_cache:
            if ee['_id'] == guild_id:
                return ee['prefix']

        return ">"

    async def get_custom_prefix(self, message: discord.Message):
        prefix = await self.fetch_prefix(message)
        bot_id = self.user.id
        prefixes = [prefix, f"<@{bot_id}> ", f"<@!{bot_id}> "]

        comp = re.compile(
            "^(" + "|".join(re.escape(p) for p in prefixes) + ").*", flags=re.I
        )
        match = comp.match(message.content)
        if match is not None:
            return match.group(1)
        return prefix

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
    with open("prefixes.json","r") as f:
        GraphingBot.prefixes_cache = json.load(f)
        print(GraphingBot.prefixes_cache)

    for cog in cogs:
        try:
            bot.load_extension(cog)
            print(f"{cog}")
        except Exception as e:
            print(e)

#################################################################################################################

@bot.command()
async def prefix(ctx,prefix):

    with open("prefixes.json","r") as f:
        GraphingBot.prefixes_cache = json.load(f)

    GraphingBot.prefixes_cache[str(ctx.guild.id)] = prefix
    
    with open("prefixes.json","w") as f:
        json.dump(GraphingBot.prefixes_cache,f)



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