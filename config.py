# this is the almighty config file,
# where all the necessary variables are dumped
# this file is imported in every file
# so changes here is almost universal

# Imports 
import os

# Standard Variables
MAIN_COLOR                = 0x11ffcc
SECONDARY_COLOR           = 0x8ebd9d
ERROR_COLOR               = 0xff0000
DEFAULT_PREFIX            = '>'
BOT_TOKEN                 = os.environ['bottoken']
VOTER_API_LINK            = 'https://top.gg/api/bots/851532461061308438/votes'
API_BASE_LINK             = 'https://denzven.pythonanywhere.com'
API_GITHUB_LINK           = 'https://github.com/denzven/Denzven-Graphing-Api'
BOT_GITHUB_LINK           = 'https://github.com/denzven/Denzven-Graphing-Api-Bot'
BOT_DESCRIPTION           = 'A Graphing-Bot that uses Denzven-Graphing-Api made by Denzven#2004'
BOT_INVITE_LINK           = 'https://discord.com/oauth2/authorize?client_id=851532461061308438&permissions=117760&scope=bot'
FANCY_BOT_INVITE_LINK     = 'https://dsc.gg/Denzven-Graphing-Api-Bot'
SUPPORT_SERVER_LINK       = 'https://discord.gg/EDcpV2V'
FANCY_SUPPORT_SERVER_LINK = 'https://dsc.gg/chilly_place'
API_COVER_PIC             = 'https://opengraph.githubassets.com/9f69f5225e6394f4d3f5213bf5d88d0442425c78f9881347da6e99da316eaed5/denzven/Denzven-Graphing-Api-Bot'
BOT_AVATAR                = 'https://cdn.discordapp.com/avatars/851532461061308438/ebb1bb6821da8d47a8559a6a4fb95ec6.png?size=256'
TOTAL_CMDS                = 27
GOOGLE_FORM               = ''
BOT_VOTE                  = 'https://top.gg/bot/851532461061308438/vote'
EMPTY_CHAR                = '‎‎'
SUGGEST_CHANNEL           = 854953071393898537
WAITING_EMOJI             = '⏱️'
DONE_EMOJI                = '✅'
ERROR_EMOJI               = '‼️'
THX_EMOJI                 = '🙏' 
UPVOTE_EMOJI              = '👍'
DOWNVOTE_EMOJI            = '👎'
TOPGG_TOKEN               = os.environ['topgg_token']
VOTE_SCRAPING_CHANNEL     = 868373815393128479
VOTE_SENDING_CHANNEL      = 869060640529088632

STATSCORD_KEY = os.environ['statscord_key']
ATTR_LINK = 'https://denzven.pythonanywhere.com/DenzGraphingApi/v1/attr'
#################################################################################################################
# Lists
EMOJI_FOR_CMDS = {
       '3D_Graph'         : '<:3D_Graph:868552735891529759>',
       '3D_Graph_Embed'   : '<:3D_Graph:868552735891529759>',
       'Flat_Graph'       : '🧻',
       'Flat_Graph_Embed' : '🧻',
       'Polar_Graph'      : '🐻‍❄️',
       'Polar_Graph_Embed': '🐻‍❄️',
       'Derivative_Graph' : '🐻‍❄️',
# 'derivative_Graph_Embed' : '🐻‍❄️',
       'Graph_Attributes' : '<:graph:868554000281239563>',
       'Bot_Info'         : '🤖',
       'Ping'             : '<a:typing:868554352141402133>',
       'GitHub'           : '<:GitHubWhite:868554626079785020>',
       'Invite'           : '<:invite:868554868372148244>',
       'Invite2'          : '<:invite:868554868372148244>',
       'Docs'             : '<:readthedocs:868555051214463057>',
       'Website'          : '🕸️',
       'Source_Code'      : '<:Python:868556292875227146>',
       'Vote'             : '<:MH_UwUlove:868556594785427516>',
       'BotLists'         : '<:list:868555435756650526>',
       'Suggest'          : '<:cp_flooshed:868555789638467664>',
       'help'             : '<:WindowsHelp:868556843557978173>',
       'Examples'         : '<:WindowsHelp:868556843557978173>',
       'Prefix'           : '<:code:868557140036571177>',
       'Change_Log'       : '<:code:868557140036571177>',
       'Showcase'         : '✨',
       'voters'           : '🙏',
       'get_vote'         : '🙏',
}

#################################################################################################################
# Change log
CHANGE_LOG = '''
Bot got approved on top.gg!

 [-]Started using Discord.py Beta
 [-]Added cool btns
 [-]Added Prefixes
 [-]Added Attr
 [-]Added Reactions to know if the cmd is in process or not
 [-]general Bug fixes
 [-]Added Botlists

'''
BOT_VERSION = 'v0.0.1'

#################################################################################################################

COGS = [
#----------main api cmds--------------
    "main_api.3dgr",
    "main_api.3dgrem",
    "main_api.fgr",
    "main_api.fgrem",
    "main_api.pgr",
    "main_api.pgrem",
    "main_api.examples",
    "main_api.derivatives",
    "main_api.derivative_embed",
    "main_api.kill",
#----------events--------------
    "events.on_command",
    "events.on_error",
    "events.on_guild_join",
#------------other cmds------------
    "commands.commands",
    "commands.help",
    "commands.prefix",
    "commands.topgg",
    "commands.vote_msg",
    "commands.statscord",
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
    "Imagine using eval(), could not be me... Sob internally",
    "Vote For meeeee!!!",
    "I Got approved on Top.gg!!",
    "Maths is fun when you know what you are doing"
]

CUTE_EMOJIS = [
'<:MH_UwUlove:868556594785427516>',
'<a:hamsterSpin:755091479021486221>',
'<a:qwerty:841934299284766730>'
]

