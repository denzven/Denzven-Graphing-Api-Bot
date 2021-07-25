# you can invite the bot here: https://dsc.gg/denzven-graphing-api-bot
# for doubts and queries Join the support/chill server: 
# https://dsc.gg/chilly_place

# These are all the "sub-commands" of the bot,
# Like, attr, botinfo, suggest ,vote etc..

# Imports Stuff
from discord.ext import commands
import discord
import datetime
from config import *

# Cog Class
class OtherCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
#################################################################################################################

    # attr cmd
    @commands.command(
        aliases = ['attr'],
        help = ('A list of all the attributes in the graphs'),
        name = 'Graph_Attributes',
        description = 'A list of all the attributes in the graphs',
    )
    async def attributes(self,ctx):
        embed=discord.Embed(title="Attributes:", description="these are the possible attributes for a given graph. There are a total of 15 of them", color=MAIN_COLOR)
        embed.set_author(name = "Help has arrived!", url="https://denzven.pythonanywhere.com/docs")
        embed.add_field( name = "grid=<1|2|3>",                     value = "adds grids to the graph",            inline = True )
        embed.add_field( name = "plot_style=<0-25>",                value = "determines the plot_style (boring)", inline = True )
        embed.add_field( name = "x_coord=<any>",                    value = "fixes the value of the x_coord",     inline = True )
        embed.add_field( name = "y_coord=<any>",                    value = "fixes the value of the y_coord",     inline = True )
        embed.add_field( name = "spine_top=<hex without #>",        value = "top-spine color",                    inline = True )
        embed.add_field( name = "spine_bottom=<hex without #>",     value = "bottom-spine color",                 inline = True )
        embed.add_field( name = "spine_left=<hex without #>",       value = "left-spine color",                   inline = True )
        embed.add_field( name = "spine_right=<hex without #>",      value = "right-spine color",                  inline = True )
        embed.add_field( name = "line_style=<hex without #>",       value = "change the color of the plot line",  inline = True )
        embed.add_field( name = "grid_lines_major=<hex without #>", value = "applies color to major girds",       inline = True )
        embed.add_field( name = "grid_lines_minor=<hex without #>", value = "applies color to minor girds",       inline = True )
        embed.add_field( name = "tick_colors=<hex without #>",      value = "applies color to ticks",             inline = True )
        embed.add_field( name = "axfacecolor=<hex without #>",      value = "applies color to foreground",        inline = True )
        embed.add_field( name = "figfacecolor=<hex without #>",     value = "applies color to background",        inline = True )
        embed.add_field( name = "title_text=<any text>",            value = "sets title",                         inline = True )
        await ctx.reply(embed = embed, allowed_mentions=discord.AllowedMentions.none())

#################################################################################################################

    # Botinfo cmd
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(
        aliases = ['btinfo','botinfo'],
        help = ('an Embed with all the neccessary info about the bot'),
        name = 'Bot_Info',
        description = 'All the neccessary info about the bot',
    )
    async def botinfo(self, ctx):
        embed = discord.Embed(title = "**Bot Info**", description = f"I am {BOT_DESCRIPTION}. My help command is `>help`. I am currently in `{len(self.bot.guilds)}` servers, and i have more than `{len(set(self.bot.get_all_members()))}` users. I have a total of `{TOTAL_CMDS}` commands.", color = 0x00FFFF)
        embed.set_thumbnail(url=BOT_AVATAR)
        embed.add_field(name = "**Invite GraphingBot**",
                        value = f"[Click Here]({BOT_INVITE_LINK})",
                        inline = True)
        embed.add_field(name = "**Support Server**",
                        value = f"[Click Here]({SUPPORT_SERVER_LINK})",
                        inline = True)
        embed.add_field(name = "**Bug Report**",
                        value = f"[Click Here]({GOOGLE_FORM})",
                        inline = True)
        embed.add_field(name = "**Vote GraphingBot**",
                        value = f"[Click Here]({BOT_VOTE})",
                        inline = True)
        embed.add_field(name = "**Our Website**",
                        value = f"[Click Here]({API_BASE_LINK})",
                        inline = True)
        embed.set_footer(text=f"{ctx.guild}", icon_url=f"{ctx.guild.icon.url}")
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed = embed)

#################################################################################################################

    # The Almighty Ping cmd
    @commands.command(
        help = ('Well.. the almighty ping cmd'),
        name = 'Ping',
        description = 'Check Ping of the Bot',
    )
    async def ping(self,ctx):
        self.bot.ping = round(self.bot.latency * 1000)
        await ctx.reply(f"ping ---> {self.bot.ping} ms", allowed_mentions=discord.AllowedMentions.none())

#################################################################################################################

    # Github cmd
    @commands.command(
        aliases = ['gh'],
        help = ('GitHub Repo of the Denzven-Graphing-Api'),
        name = 'GitHub',
        description = 'GitHub Repo of the Denzven-Graphing-Api',
    )
    async def github(self,ctx):
        await ctx.reply(API_GITHUB_LINK, allowed_mentions=discord.AllowedMentions.none())

#################################################################################################################

    # Invite cmd
    @commands.command(
        aliases = ['inv'],
        help = ('Invite the Bot in your Server!'),
        name = 'Invite',
        description = 'Invite the Bot in your Server!',
    )
    async def invite(self,ctx):
        await ctx.reply(BOT_INVITE_LINK, allowed_mentions=discord.AllowedMentions.none())

#################################################################################################################

    # a fancier invite
    @commands.command(
        aliases = ['inv2'],
        help = ('Invite the Bot in your Server! with a fancy link!'),
        name = 'Invite2',
        description = 'Invite the Bot in your Server! with a fancy link',
    )
    async def invite2(self,ctx):
        await ctx.reply(FANCY_BOT_INVITE_LINK, allowed_mentions=discord.AllowedMentions.none())

#################################################################################################################

    # Docs cmd
    @commands.command(
        help = ('Get the Docs of the Denzven-Graphing-Api'),
        name = 'Docs',
        description = 'Get the Docs of the Denzven-Graphing-Api',
    )
    async def docs(self,ctx):
        await ctx.reply("https://denzven.pythonanywhere.com/docs", allowed_mentions=discord.AllowedMentions.none())

#################################################################################################################

    # Website cmd
    @commands.command(
        aliases = ['web'],
        help = ('Visit the website of Denzven-Graphing-Api'),
        name = 'Website',
        description = 'Visit the website of Denzven-Graphing-Api',
    )
    async def website(self,ctx):
        await ctx.reply(API_BASE_LINK, allowed_mentions=discord.AllowedMentions.none())

#################################################################################################################

    # Pypi cmd (in process)
    #@commands.command()
    #async def pypi(self,ctx):
    #    await ctx.reply("https://pypi.org/project/Denzven-Graphing-Api-Wrapper (not currently developed)")

#################################################################################################################

    # Github repo of bot
    @commands.command(
        aliases = ['source'],
        help = ('Get the Source Code of the Bot'),
        name = 'Source_Code',
        description = 'Get the Source Code of the Bot',
    )
    async def src(self,ctx):
        await ctx.reply(BOT_GITHUB_LINK)

#################################################################################################################

    # Vote cmd
    @commands.command(
        help = ('Vote the Bot on top.gg!!'),
        name = 'Vote',
        description = 'Vote the Bot on top.gg!!',
    )
    async def vote(self,ctx):
        embed = discord.Embed(title="Vote for GraphBot", url=BOT_VOTE, description="vote me on top.gg!")
        embed.set_thumbnail(url = BOT_AVATAR)
        embed.set_footer(text=f"{ctx.guild}", icon_url=f"{ctx.guild.icon.url}")
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)

#################################################################################################################

    # Botlists cmd
    @commands.command(
        aliases = ['bl'],
        help = ('Get the lists of the BotLists the Bot has enrolled'),
        name = 'BotLists',
        description = 'Get the lists of the BotLists the Bot has enrolled',
    )
    async def botlists(self,ctx):
        embed=discord.Embed(title="Bot-Lists:", description="these are the websites the bot is currently uploaded to", color=MAIN_COLOR)
        embed.set_author(name = "Roll in the Lists!")
        embed.add_field( name = "Top.gg",                           value = "https://top.gg/bot/851532461061308438",            inline = False )
        embed.add_field( name = "discordbotlist",                   value = "https://discordbotlist.com/bots/graphingbot",      inline = False )
        embed.add_field( name = "botlists.com",                     value = "https://botlists.com/bot/851532461061308438",      inline = False )
        embed.add_field( name = "discord.bots.gg",                  value = "https://discord.bots.gg/bots/851532461061308438",  inline = False )
        await ctx.reply(embed = embed, allowed_mentions=discord.AllowedMentions.none())
    
#################################################################################################################

    # Chnagelog cmd
    @commands.command(
        aliases = ['cl'],
        help = ('Get the ChangeLog of the latest update!'),
        name = 'Change_Log',
        description = 'Get the ChangeLog of the latest update!',
    )
    async def chnage_log(self,ctx):
        embed=discord.Embed(title="Change Log", description=CHANGE_LOG, color=MAIN_COLOR)
        embed.set_footer(text = BOT_VERSION)
        await ctx.reply(embed = embed, allowed_mentions=discord.AllowedMentions.none())
    
#################################################################################################################

    # Suggest cmd
    @commands.command(
        aliases = ['s'],
        help = ('Suggest suggestions for the Bot!'),
        name = 'Suggest',
        description = 'Suggest suggestions for the Bot!',
    )
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def suggest(self,ctx,*,suggestion=None):
        if suggestion == None:
            await ctx.reply("You cant have an Empty Suggestion!")
        else:
            await ctx.message.add_reaction(THX_EMOJI)
            pass
            embed=discord.Embed(title=f"{ctx.author} has sent a suggestion!", description=f"{suggestion}", color=MAIN_COLOR)
            embed.set_footer(text=f"{ctx.guild}", icon_url=f"{ctx.guild.icon.url}")
            embed.timestamp = datetime.datetime.utcnow()
            channel = self.bot.get_channel(SUGGEST_CHANNEL)
            
            embed2 = discord.Embed(title="thx for the suggestion!", description="thnq for making the bot better!",color=MAIN_COLOR)
            embed2.add_field(name="you sent:",value =f"{suggestion}")
            embed2.set_footer(text=f"{ctx.guild}", icon_url=f"{ctx.guild.icon.url}")
            embed2.timestamp = datetime.datetime.utcnow()

            view_ui = discord.ui.View(timeout=None)
            view_ui.add_item(discord.ui.Button(
                style=discord.ButtonStyle.url,
                url=SUPPORT_SERVER_LINK,
                label="support server",
            ))
            suggestion = await channel.send(embed = embed)
            await suggestion.add_reaction(UPVOTE_EMOJI)
            await suggestion.add_reaction(DOWNVOTE_EMOJI)
            await ctx.reply(embed = embed2,view=view_ui, allowed_mentions=discord.AllowedMentions.none())
    
#################################################################################################################

def setup(bot):
	bot.add_cog(OtherCommands(bot))