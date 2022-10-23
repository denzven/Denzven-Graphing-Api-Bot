# this deals with setting a custom prefix and writing it to a json file
# (not the best way, but works)

# Imports
import guilded
from guilded.ext import commands
import json

# config
from config import DEFAULT_PREFIX


# cog class
class Prefix(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(
        help='Set a Custom prefix for the bot in this guild',
        name='Prefix',
        description='Set a Custom prefix for the bot in this guild',
    )
    @commands.has_permissions(manage_messages=True)
    async def prefix(self, ctx, prefix: str = None):
        if prefix is None:
            await ctx.reply(
                f'My prefix for this server is `{self.bot.prefixes_cache.get(str(ctx.guild.id), DEFAULT_PREFIX)}`'
            )
        else:
            with open("prefixes.json", "r") as f:
                current_prefixes: dict = json.load(f)
            if prefix != DEFAULT_PREFIX:
                if prefix.startswith("@") and prefix != "@":
                    await ctx.reply(f"The Prefix of the bot cannot be sent to a mention, it is recommended not to do so.")
                else:
                    current_prefixes[str(ctx.guild.id)] = prefix
            else:
                current_prefixes.pop(str(ctx.guild.id), 'amogus')
                if prefix.startswith("@") and prefix != "@":
                    print("mention prefix")
                else:
                    with open("prefixes.json", "w") as f:
                        json.dump(current_prefixes, f)
                        await ctx.reply(f'The Prefix has been set to `{prefix}`', allowed_mentions=discord.AllowedMentions.none())


def setup(bot):
    bot.add_cog(Prefix(bot))
