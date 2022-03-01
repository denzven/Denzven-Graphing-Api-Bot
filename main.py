'''
+------------------------------------------------------------------------+                                                                        
|                                                                        |
| Welcome! This is an Example Bot in Dicord.py,                          |                                              
| that showcases the use of the DenzGraphingApi,                         |                                               
| to form embeds and send basic info                                     |                                   
| you can invite the bot here: https://dsc.gg/denzven-graphing-api-bot   |                                                                     
| for doubts and queries Join the support/chill server:                  |                                                       
| https://dsc.gg/chilly_place                                            |                            
|                                                                        |
+------------------------------------------------------------------------+                                                                        

'''

#importing Modules
import guilded
from guilded.ext import commands
import os
import json
import aiohttp
import datetime
#import Denzven_Graphing_Api_Wrapper as GraphingApi #pip install

#importing the config files
from config import *
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


#################################################################################################################

# Defining the Bot
description = BOT_DESCRIPTION
bot = GraphingBot(
    command_prefix=DEFAULT_PREFIX)

#################################################################################################################


#################################################################################################################

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

#################################################################################################################

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

    ##groups = {} 
    ##def func(e):
    ##    return len(list(filter(lambda m: not m.bot, e.members)))    
    ##for guild in bot.guilds:
    ##    if guild.member_count in groups:
    ##        hmph = groups[guild.member_count]
    ##        hmph.append(guild)
    ##        groups.update({guild.member_count: hmph})
    ##    else:
    ##        groups.update({guild.member_count: [guild]})    
    ##for count, group in groups.items():
    ##    groups.update({count: sorted(group, key=func)}) 
    ##amogus = {}
    ##for i in sorted(groups):
    ##    amogus.update({i: groups[i]})
    ##print(amogus)
    ##Gets the Server Names  
    #name = []
    #id = []
    #members = []
    #Humans = []
    #Bots = []
    #Owners = [] 
    #def func(e):
    #    return len(list(filter(lambda m: not m.bot, e.members)))
    #sorted_guilds = bot.guilds 
    #sorted_guilds = sorted(sorted_guilds, key=func)
    ##import operator
    ##sorted_guilds = sorted(bot.guilds, key=operator.attrgetter("member_count"))
    ##sorted_guilds = sorted(bot.guilds, key = list(filter(lambda m: not m.bot, operator.attrgetter("members"))))
    #for guild in sorted_guilds:
    #    name.append(guild.name)
    #    id.append(guild.id)
    #    members.append(len(guild.members))
    #    Humans.append(len(list(filter(lambda m: not m.bot, guild.members))))
    #    Bots.append(len(list(filter(lambda m: m.bot, guild.members))))
    #    Owners.append(str(guild.owner))
    #    print(f'| name:{guild.name}\n| guild id:{guild.id}\n| no. of members:{len(guild.members)}\n| Humans: {len(list(filter(lambda m: not m.bot, guild.members)))}\n| Bots: {len(list(filter(lambda m: m.bot, guild.members)))}\n| GuildOwner:{str(guild.owner)}')
    #    print('+--------------------------------------------------+')   
    #print('\n')
    ##print(name)
    ##print(id)
    ##print(members)
    ##print(Humans)
    ##print(Bots)
    ##print(Owners)

#################################################################################################################

# Enabling edit to command too
@bot.event
async def on_message_edit(before,after):
    if before.content == after.content:
        return
    if before.author.bot:
        return
    bot.dispatch("message", after)
    
#################################################################################################################

#keep_alive()	# Funtion for keeping replit alive
bot.run(str(os.environ['LOGIN_EMAIL']),str(os.environ['LOGIN_PASSWD']))