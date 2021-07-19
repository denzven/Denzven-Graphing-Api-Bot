from discord.ext import commands
import discord
import datetime
from config import *

class Command(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help2(self,ctx,command=None):
        #try:
        print(self.bot.prefixes_cache) 
        #print(self.bot.prefixes_cache["764449914146521118"])
        #except:
        #    prefix = '>'
        if command==None:
            #embed.add_field( name="fgr"    , value="flat_graph"                     , inline=True )
            #embed.add_field( name="fgrem"  , value="flat_graph_embed"               , inline=True )
            #embed.add_field( name="pgr"    , value="polar_graph"                    , inline=True )
            #embed.add_field( name="pgrem"  , value="polar_graph_embed"              , inline=True )
            #embed.add_field( name="3dgr"   , value="threeD_graph"                   , inline=True )
            #embed.add_field( name="3dgrem" , value="threeD_graph_embed"             , inline=True )
            #embed.add_field( name="ping"   , value="ping of the bot"                , inline=True )
            #embed.add_field( name="github" , value="sends the link of github"       , inline=True )
            #embed.add_field( name="docs"   , value="Docs of the api"                , inline=True )
            #embed.add_field( name="attr"   , value="all attributes of the graph"    , inline=True )
            #embed.add_field( name="src"    , value="source code of this Bot"        , inline=True )
            #embed.add_field( name="prefix" , value="changes the prefix of this Bot" , inline=True )
            #embed.add_field( name="jsk"    , value="owner only cmd for this Bot"    , inline=True )
            #embed.set_footer(text="hmmm")
            embed = discord.Embed(
                title="Denzven-Graphing-Api-Bot", 
                colour=0x11ffcc, 
                description="This Bot is a showcase of the use of Denzven-Graphing-Api \n```py\n try using >help <command> at each of the below sections```\n\n\n", timestamp=datetime.datetime.utcnow())
            embed.set_image(url="https://opengraph.githubassets.com/9f69f5225e6394f4d3f5213bf5d88d0442425c78f9881347da6e99da316eaed5/denzven/Denzven-Graphing-Api-Bot")
            embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/851532461061308438/ebb1bb6821da8d47a8559a6a4fb95ec6.webp")
            embed.set_footer(text=f'rendered by {ctx.author.name}',icon_url=ctx.author.avatar_url)
            embed.add_field( name = "GraphingCommands"      , value=">fgr <input_formula> [attr] \n>pgr <input_formula> [attr] \n>3dgr <input_formula> [attr] \n"                                          , inline=False)
            embed.add_field( name = "GraphingCommandsEmbed" , value=">fgrem <input_formula> [attr] \n>pgrem <input_formula> [attr] \n>3dgrem <input_formula> [attr] \n"                                    , inline=False)
            embed.add_field( name = "OtherCommands"         , value=">attr \n>docs \n>github \n>ping \n>pypi  \n>src \n>website \n>prefix \n>attr \n", inline=False)
            embed.add_field( name = "OwnerCommands"         , value=">jsk"                                                                          , inline=False)
            await ctx.reply(content=f"**Help has arrived!** \n the prefix for this is server is ``prefix``", embed=embed, allowed_mentions=discord.AllowedMentions.none())
            #await ctx.send(embed=embed)
        else:
            await ctx.send_help(command)

def setup(bot):
	bot.add_cog(Command(bot))