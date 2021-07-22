import os
import discord
# This is the Config file... most commonly used strings/colors etc are set here for easy acsess


# Not gonna change often
MAIN_COLOR = 0x11ffcc
SECONDARY_COLOR = 0x8ebd9d
ERROR_COLOR = 0xff0000
DEFAULT_PREFIX = '>'
BOT_TOKEN = os.environ['bottoken']
API_BASE_LINK = 'https://denzven.pythonanywhere.com'
API_GITHUB_LINK = 'https://github.com/denzven/Denzven-Graphing-Api'
BOT_GITHUB_LINK = 'https://github.com/denzven/Denzven-Graphing-Api-Bot'
BOT_DESCRIPTION = 'A Graphing-Bot that uses Denzven-Graphing-Api made by Denzven#2004'
BOT_INVITE_LINK = 'https://discord.com/oauth2/authorize?client_id=851532461061308438&permissions=117760&scope=bot'
FANCY_BOT_INVITE_LINK = 'https://dsc.gg/Denzven-Graphing-Api-Bot'
SUPPORT_SERVER_LINK = 'https://discord.gg/EDcpV2V'
FANCY_SUPPORT_SERVER_LINK = 'https://dsc.gg/chilly_place'
API_COVER_PIC = 'https://opengraph.githubassets.com/9f69f5225e6394f4d3f5213bf5d88d0442425c78f9881347da6e99da316eaed5/denzven/Denzven-Graphing-Api-Bot'
BOT_AVATAR = 'https://cdn.discordapp.com/avatars/851532461061308438/ebb1bb6821da8d47a8559a6a4fb95ec6.png?size=256'
TOTAL_CMDS = 15
GOOGLE_FORM = ''
BOT_VOTE = ''
#################################################################################################################
CHANGE_LOG = '''
lotta strs hmmm
'''
#################################################################################################################
cogs = [
#----------main api cmds--------------
    "main_api.3dgr",
    "main_api.3dgrem",
    "main_api.fgr",
    "main_api.fgrem",
    "main_api.pgr",
    "main_api.pgrem",
    "main_api.kill",
#----------events--------------
    "events.on_command",
    "events.on_error",
#------------other cmds------------
    "commands.commands",
    "commands.help",
    "commands.prefix",
    "commands.btns",
#-----------tasks------------
    "task.status_task",
#------------------------
        ]
#################################################################################################################
inputstatus =   [
    "Busy plotting Graphs",
    "Rendering Equations",
    "Matplotlib is awesome!",
    "with Mathematics",
    "with Graphs",
    "with lines,parabolas and circles",
    "hmmmm... what to plot today?",
    "Star me on GitHub pls! >github",
    "Do i make you feel like plotting some graphs?",
    "Eating RealityProgrammer's Brain",
    "Checking errors",
    "with Styles!",
    "Python is pogg!",
    "Eating tortillas with 69 others",
    "My favorite number is 01000101",
    "I'm being stuck under a basement",
    "Send help",
    "What does this piece of code do? while trueeeeeeeeeeeeeeeeeeeeee...",
    "Imagine using eval(), could not be me... Sob internally",
    
]
