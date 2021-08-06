# Welcome! This is an Example Bot in Dicord.py,
# that showcases the use of the DenzGraphingApi,
# to form embeds and send basic info
# you can invite the bot here: https://dsc.gg/denzven-graphing-api-bot
# for doubts and queries Join the support/chill server: 
# https://dsc.gg/chilly_place

#importing Modules
import discord
from discord.ext import commands
import os
import json
import aiohttp
#import Denzven_Graphing_Api_Wrapper as GraphingApi #pip install

#importing the config files
from config import *
from utils.custom_checks import voter_only
#from keep_alive import keep_alive

#################################################################################################################

# making a bot sub-class
class GraphingBot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.CommandNumber = 0
        self.prefixes_cache = {}
        self.ping = 0
        self.ApiBaseUrl = API_BASE_LINK

    # A function to get the custom prefix if set,from a server
    async def get_custom_prefix(bot, message):
        prefixes_ = [f'<@{bot.user.id}> ', f'<@!{bot.user.id}> ']
        with open("prefixes.json") as f:
            prefixes = json.load(f)

        prefixes_.append(DEFAULT_PREFIX if str(message.guild.id) not in prefixes else prefixes[str(message.guild.id)])
        return prefixes_

#################################################################################################################

# Defining the Bot
description = BOT_DESCRIPTION
intents = discord.Intents.all()
intents.members = True
intents.presences = True
bot = GraphingBot(
    #command_prefix=commands.when_mentioned_or(DEFAULT_PREFIX),
    command_prefix=GraphingBot.get_custom_prefix,
    intents=discord.Intents.all(),
    case_insensitive=True,
    strip_after_prefix=False,
    allowed_mentions=discord.AllowedMentions.none())
    
bot.remove_command('help') #Removing the Default Help

#################################################################################################################

# Hinding and Loading Jishaku for debugging
os.environ.setdefault("JISHAKU_HIDE", "1")
bot.load_extension('jishaku') # pip install -U jishaku

# On_connect Info
@bot.event
async def on_connect():
    print('+--------------------------------------------------+')
    print('|                 Bot has Connected                |')
    print('+--------------------------------------------------+')
    with open("prefixes.json","r") as f:
        GraphingBot.prefixes_cache = json.load(f)
        print(GraphingBot.prefixes_cache)
        print('+--------------------------------------------------+')
        print('|                  Prefixes have loaded            |')
        print('+--------------------------------------------------+')
        print('\n')

#On_ready Info
@bot.event
async def on_ready():
    print('+--------------------------------------------------+')
    print('|                 Bot has Started                  |')
    print('+--------------------------------------------------+')
    print('| logged in as: {}               |'.format(bot.user))
    print('+--------------------------------------------------+')
    print('| No. of Servers: {}                               |'.format(len(bot.guilds)))
    print('| No. of Users: {}                              |'.format(len(bot.users)))
    print('| Bot Prefix: "{}"                                  |'.format(DEFAULT_PREFIX))
    print('| Bot made by: @Denzven#2004                       |')
    print('| Join my chill server: https://dsc.gg/chilly_place|')
    print('+--------------------------------------------------+')
    print('\n')
    print('+--------------------------------------------------+')
    print('|                     Cogs:                        |')
    print('+--------------------------------------------------+')

    # Loads in the Cogs
    for cog in COGS:
        try:
            bot.load_extension(cog)
            print(f"| {cog} has loaded")
        except Exception as e:
            print(f"| {cog} has not been loaded")
            print(e)
    print('+--------------------------------------------------+') 
    print('\n')    
    print('+--------------------------------------------------+')
    print('|                     servers:                     |')
    print('+--------------------------------------------------+')

    #Gets the Server Names   
    for guild in bot.guilds:
        print(f'| name:{guild.name}\n| guild id:{guild.id}\n| no. of members:{len(guild.members)}\n| Humans: {len(list(filter(lambda m: not m.bot, guild.members)))}\n| Bots: {len(list(filter(lambda m: m.bot, guild.members)))}\n| GuildOwner:{str(guild.owner)}')
        print('+--------------------------------------------------+')   

    print('\n')

@bot.command()
@voter_only()
async def ex(ctx):
    await ctx.send("exclusive cmds hehe")

#################################################################################################################

#keep_alive()	# Funtion for keeping replit alive
bot.run(BOT_TOKEN)