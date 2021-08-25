# this is the almighty config file,
# where all the necessary variables are dumped
# this file is imported in every file
# so changes here is almost universal

# Imports 
import os
from inputstatus import inputstatus

# Standard Variables
MAIN_COLOR                = 0x01abe1
SECONDARY_COLOR           = 0x8ebd9d
ERROR_COLOR               = 0xff0000
PASS_COLOR                = 0x00ff00
DEFAULT_PREFIX            = '>'
BOT_TOKEN                 = os.environ['bottoken']
VOTER_API_LINK            = 'https://top.gg/api/bots/851532461061308438/votes'
DEFAULT_SPLITTER          = ' '
API_BASE_LINK             = 'https://denzven.pythonanywhere.com'

API_PATH_FLAT_GRAPH       = '/DenzGraphingApi/v1/flat_graph/test/plot'
API_PATH_POLAR_GRAPH      = '/DenzGraphingApi/v1/polar_graph/test/plot'
API_PATH_3D_GRAPH         = '/DenzGraphingApi/v1/threeD_graph/test/plot'
API_PATH_DERIVATIVE_GRAPH = '/DenzGraphingApi/v1/derivative_graph/test/plot'
API_PATH_LATEX            = '/DenzGraphingApi/v1/latex/test/plot'

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
PLOT_EMOJI                = '📈'
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
 'derivative_Graph_Embed' : '🐻‍❄️',
       'Graph_Attributes' : '<:graph:868554000281239563>',
       'Bot_Info'         : '🤖',
       'Ping'             : '<a:typing:868554352141402133>',
       'GitHub'           : '<:GitHubWhite:868554626079785020>',
       'Invite'           : '<:invite:868554868372148244>',
#       'Invite2'          : '<:invite:868554868372148244>',
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
Bot got Verified!!
Bot crossed Over 100 guilds!! 
Thx to all the voters and Supporters!

[-] Added VoterOnly Commands
[-] added 
'''
BOT_VERSION = 'v1.0.0'

#################################################################################################################

inputstatus = inputstatus

COGS = [
#----------Main API Commands--------------#                    
        "main_api.examples",              #               
        "main_api.latex",                 #             
        "main_api.main_graph",            #             
        "main_api.kill",                  # 
#--------------Events---------------------#                 
        "events.on_command",              #    
        "events.on_error",                #  
        "events.on_guild_join",           #       
#------------Other Commands---------------#                 
        "commands.commands",              #    
        "commands.help",                  #
        "commands.prefix",                #  
        "commands.topgg",                 # 
        "commands.vote_msg",              #    
        "commands.statscord",             #     
#--------------Tasks----------------------#         
        "task.status_task",               #   
#-----------------------------------------#     
        ]

#################################################################################################################



CUTE_EMOJIS = [
'<:MH_UwUlove:868556594785427516>',
'<a:hamsterSpin:755091479021486221>',
'<a:qwerty:841934299284766730>'
]

LOG_SERVER          = 877055490113306715
LOG_ON_CMD          = 877056797469454357
LOG_ON_GUILD_JOIN   = 877056911852331039
LOG_ON_GUILD_REMOVE = 877058774676946944
LOG_ON_ERROR        = 877057625441845288
LOG_ON_CONNECT      = 877057755322646558
LOG_ON_DISCONNECT   = 877058311239905300
LOG_ON_READY        = 877057817830391849
LOG_ON_DM           = 877059522622017536
LOG_SUGGESTION      = 877060305119752232