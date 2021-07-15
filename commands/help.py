from discord.ext import commands
import discord

class Command(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        aliases = ['help3']
    )
    async def help2(self,ctx):
        embed=discord.Embed(title="Help Menu", description="provides help for using this bot")
        embed.set_author(name="Help has arrived!")
        embed.add_field(name=">fgr", value="flat_graph", inline=True)
        embed.add_field(name=">fgrem", value="flat_graph_embed", inline=True)
        embed.add_field(name=">pgr", value="polar_graph", inline=True)
        embed.add_field(name=">pgrem", value="polar_graph_embed", inline=True)
        embed.add_field(name=">3dgr", value="threeD_graph", inline=True)
        embed.add_field(name=">3dgrem", value="threeD_graph_embed", inline=True)
        embed.add_field(name=">ping", value="ping of the bot", inline=True)
        embed.add_field(name=">github", value="sends the link of github", inline=True)
        embed.add_field(name=">docs", value="Docs of the api", inline=True)
        await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(Command(bot))