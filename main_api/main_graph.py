# this is the cog that handles three-D graphs (without embeds)

# imports
from discord.ext import commands
import discord
import urllib
import aiohttp
from main_api.fetchgraph import fetchgraph
from utils.custom_checks import voter_only

# Config
from config import *

class GraphingCommand(commands.Cog):
    def __init__(self, bot, **kwargs):
        self.bot = bot

#################################################################################################################

    @commands.hybrid_command(
        aliases = ['threeDgraph','threeDgr','3dgraph','3dgr'],
        help = ('Plot three-dimensional graphs providing a formula with x and y (z is NOT supported)'),
        name = '3D_Graph',
        description = 'Plot 3D Graphs with this command',
    )
    async def threeD_graph(self,ctx, *, input_params):
        await fetchgraph(ctx, input_params, API_BASE_LINK, API_PATH_3D_GRAPH, 'threeD_graph', DEFAULT_SPLITTER, WAITING_EMOJI, DONE_EMOJI, ERROR_EMOJI, MAIN_COLOR, ERROR_COLOR, False)

#################################################################################################################

    @commands.hybrid_command(
        aliases = ['threeDgraphembed','3dgrembed','3dgraphembed','3dgrem'],
        help = ('Plot three-dimensional graphs providing a formula with x and y insude beautiful embeds (z is NOT supported)'),
        name = '3D_Graph_Embed',
        description = 'Plot 3D Graphs in Embeds with this command',
    )
    async def threeD_graph_embed(self,ctx, *, input_params):
        await fetchgraph(ctx, input_params, API_BASE_LINK, API_PATH_3D_GRAPH, 'threeD_graph', DEFAULT_SPLITTER, WAITING_EMOJI, DONE_EMOJI, ERROR_EMOJI, MAIN_COLOR, ERROR_COLOR, True)

#################################################################################################################

    @commands.hybrid_command(
        aliases = ['derivativegraphembed','derivativegrembed','dgraphembed','dgrem'],
        help = ('Plot derivative graphs providing a formula with x and y, inside cool looking embeds'),
        name = 'derivative_Graph_Embed',
        description = 'Plot derivative Graphs in Embeds with this command',
    )
    @voter_only()
    async def derivative_graph_embed(self,ctx, *, input_params):
        await fetchgraph(ctx, input_params, API_BASE_LINK, API_PATH_DERIVATIVE_GRAPH, 'derivative_graph', DEFAULT_SPLITTER, WAITING_EMOJI, DONE_EMOJI, ERROR_EMOJI, MAIN_COLOR, ERROR_COLOR, True)

#################################################################################################################

    @commands.hybrid_command(
        aliases = ['dgr','derivative'],
        help = ('Plot derivates of graphs providing a formula with x'),
        name = 'Derivative_Graph',
        description = 'Plot derivatives with this command',
    )
    @voter_only()
    async def derivative_graph(self,ctx, *, input_params):
        await fetchgraph(ctx, input_params, API_BASE_LINK, API_PATH_DERIVATIVE_GRAPH, 'derivative_graph', DEFAULT_SPLITTER, WAITING_EMOJI, DONE_EMOJI, ERROR_EMOJI, MAIN_COLOR, ERROR_COLOR, False)

#################################################################################################################

    @commands.hybrid_command(
        aliases = ['flatgraph','flatgr','fgraph','fgr'],
        help = ('Plot Flat graphs providing a formula with x and y'),
        name = 'Flat_Graph',
        description = 'Plot Flat Graphs with this command',
    )

    async def flat_graph(self,ctx, *, input_params):
        await fetchgraph(ctx, input_params, API_BASE_LINK, API_PATH_FLAT_GRAPH, 'flat_graph', DEFAULT_SPLITTER, WAITING_EMOJI, DONE_EMOJI, ERROR_EMOJI, MAIN_COLOR, ERROR_COLOR, False)

#################################################################################################################

    @commands.hybrid_command(
        aliases = ['flatgraphembed','flatgrembed','fgraphembed','fgrem'],
        help = ('Plot Flat graphs providing a formula with x and y, inside cool looking embeds'),
        name = 'Flat_Graph_Embed',
        description = 'Plot Flat Graphs in Embeds with this command',
    )

    async def flat_graph_embed(self,ctx, *, input_params):
        await fetchgraph(ctx, input_params, API_BASE_LINK, API_PATH_FLAT_GRAPH, 'flat_graph', DEFAULT_SPLITTER, WAITING_EMOJI, DONE_EMOJI, ERROR_EMOJI, MAIN_COLOR, ERROR_COLOR, True)

#################################################################################################################

    @commands.hybrid_command(
        aliases = ['polargraph','polargr','pgraph','pgr'],
        help = ('Plot Polar graphs providing a formula with x and y'),
        name = 'Polar_Graph',
        description = 'Plot Polar Graphs with this command',
    )

    async def polar_graph(self,ctx, *, input_params):
        await fetchgraph(ctx, input_params, API_BASE_LINK, API_PATH_POLAR_GRAPH, 'polar_graph', DEFAULT_SPLITTER, WAITING_EMOJI, DONE_EMOJI, ERROR_EMOJI, MAIN_COLOR, ERROR_COLOR, False)

#################################################################################################################

    @commands.hybrid_command(
        aliases = ['polatgraphembed','polargrembed','pgraphembed','pgrem'],
        help = ('Plot Polar graphs providing a formula with x and y inside beautiful embeds'),
        name = 'Polar_Graph_Embed',
        description = 'Plot Polar Graphs in Embeds with this command',        
    )

    async def polar_graph_embed(self,ctx, *, input_params):
        await fetchgraph(ctx, input_params, API_BASE_LINK, API_PATH_POLAR_GRAPH, 'polar_graph', DEFAULT_SPLITTER, WAITING_EMOJI, DONE_EMOJI, ERROR_EMOJI, MAIN_COLOR, ERROR_COLOR, True)

#################################################################################################################

def setup(bot):
    bot.add_cog(GraphingCommand(bot))