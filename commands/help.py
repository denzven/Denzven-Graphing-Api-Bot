from discord.ext import commands
import discord

class Command(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        aliases = ['help2']
    )
    async def help2(self,ctx):
        embed=discord.Embed(title="Attributes:", description="these are the possible attributes for a given graph. There are a total of 15 of them", color=0xd9e91b)
        embed.set_author(name="Help has arrived!", url="https://denzven.pythonanywhere.com/docs")
        embed.add_field(name="grid=<1|2|3>", value="adds grids to the graph", inline=True)
        embed.add_field(name="plot_style=<0-25>", value="determines the plot_style (boring)", inline=True)
        embed.add_field(name="x_coord=<any>", value="fixes the value of the x_coord", inline=True)
        embed.add_field(name="y_coord=<any>", value="fixes the value of the y_coord", inline=True)
        embed.add_field(name="spine_top=<hex without #>", value="top-spine color", inline=True)
        embed.add_field(name="spine_bottom=<hex without #>", value="bottom-spine color", inline=True)
        embed.add_field(name="spine_left=<hex without #>", value="left-spine color", inline=True)
        embed.add_field(name="spine_right=<hex without #>", value="right-spine color", inline=True)
        embed.add_field(name="line_style=<hex without #>", value="change the color of the plot line", inline=True)
        embed.add_field(name="grid_lines_major=<hex without #>", value="applies color to major girds", inline=True)
        embed.add_field(name="grid_lines_minor=<hex without #>", value="applies color to minor girds", inline=True)
        embed.add_field(name="tick_colors=<hex without #>", value="applies color to ticks", inline=True)
        embed.add_field(name="axfacecolor=<hex without #>", value="applies color to foreground", inline=True)
        embed.add_field(name="figfacecolor=<hex without #>", value="applies color to background", inline=True)
        embed.add_field(name="title_text=<any text>", value="sets title", inline=True)
        await ctx.reply(embed=embed)

def setup(bot):
	bot.add_cog(Command(bot))