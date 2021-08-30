# this deals with setting a custom prefix and writing it to a json file
# (not the best way, but works)

# Imports
from discord.ext import commands
import discord
import json

# config
from config import DEFAULT_PREFIX


# cog class
class Prefix(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        help='Set a Custom prefix for the bot in this guild',
        name='Prefix',
        description='Set a Custom prefix for the bot in this guild',
    )
    @commands.has_permissions(manage_messages=True)
    async def prefix(self, ctx, prefix: str = None):
        if prefix is None:
            await ctx.reply(
                f'My prefix for this server is `{self.bot.prefixes_cache.get(str(ctx.guild.id), DEFAULT_PREFIX)}`',
                allowed_mentions=discord.AllowedMentions.none()
            )
        else:
            with open("prefixes.json", "r") as f:
                current_prefixes = json.load(f)
            current_prefixes[str(ctx.guild.id)] = prefix
            with open("prefixes.json", "w") as f:
                json.dump(current_prefixes, f)
                await ctx.reply(f'The Prefix has been set to `{prefix}`', allowed_mentions=discord.AllowedMentions.none())


def setup(bot):
    bot.add_cog(Prefix(bot))
