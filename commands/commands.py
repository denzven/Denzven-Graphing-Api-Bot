from discord.ext import commands
import discord

class Command(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        aliases = ['attr']
    )
    async def attributes(self,ctx):
        embed=discord.Embed(title="Attributes:", description="these are the possible attributes for a given graph. There are a total of 15 of them", color=0x11ffcc)
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
        await ctx.reply(embed = embed)

    @commands.command()
    async def ping(self,ctx):
        self.bot.ping = round(self.bot.latency * 1000)
        await ctx.reply(f"ping ---> {self.bot.ping} ms")

    @commands.command()
    async def github(self,ctx):
        await ctx.reply("https://github.com/denzven/Denzven-Graphing-Api")

    @commands.command()
    async def invite(self,ctx):
        await ctx.reply("https://discord.com/oauth2/authorize?client_id=851532461061308438&permissions=117760&scope=bot")

    @commands.command()
    async def invite2(self,ctx):
        await ctx.reply("https://dsc.gg/Denzven-Graphing-Api-Bot")

    @commands.command()
    async def docs(self,ctx):
        await ctx.reply("https://denzven.pythonanywhere.com/docs")

    @commands.command()
    async def website(self,ctx):
        await ctx.reply("https://denzven.pythonanywhere.com")

    @commands.command()
    async def pypi(self,ctx):
        await ctx.reply("https://pypi.org/project/Denzven-Graphing-Api-Wrapper (not currently developed)")

    @commands.command()
    async def src(self,ctx):
        await ctx.reply("https://github.com/denzven/Denzven-Graphing-Api-Bot")

def setup(bot):
	bot.add_cog(Command(bot))