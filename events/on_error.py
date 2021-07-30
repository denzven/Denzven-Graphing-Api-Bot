# This is a On_error Event and runns every time a error is faced,
# it also logs the location and raises the error and spams the console

# Imports
from discord.ext import commands
import discord

# Config
from config import *
from utils.custom_checks import NotVotedError

class Error(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self,ctx, error):

        server = ctx.guild.name
        channel = ctx.channel
        user = ctx.author
        command = ctx.command

        print(f'{server} > {channel} > {user} > {command} > {error}')

        if isinstance(error,commands.BadArgument):
            await ctx.send('BadArgument', allowed_mentions=discord.AllowedMentions.none())

        if isinstance(error, commands.errors.CommandInvokeError):
            await ctx.reply("CommandInvokeError", allowed_mentions=discord.AllowedMentions.none())

        # Gets annoying pretty quickly my bot got muted becasue of this...
        #if isinstance(error, commands.CommandNotFound): 
        #    await ctx.reply("CommandNotFound", allowed_mentions=discord.AllowedMentions.none())

        if isinstance(error,commands.errors.CommandOnCooldown):
            await ctx.reply(f"CommandOnCooldown retry after {error.retry_after:.2f}s.", allowed_mentions=discord.AllowedMentions.none())

        if isinstance(error, commands.errors.MissingPermissions):
            await ctx.reply(f"MissingPermissions {' '.join(error.NotOwner[0].split('_')).title()}", allowed_mentions=discord.AllowedMentions.none())
            return

        if isinstance(error, NotVotedError):
            await ctx.reply(f"NotVotedError (Beg for Votes)")
            return

        if isinstance(error, commands.errors.NotOwner):
            await ctx.reply(f"NotOwner {error}", allowed_mentions=discord.AllowedMentions.none())
            return

        #if isinstance(error,commands.MissingRequiredArgument):
        #    await ctx.reply('MissingRequiredArgument')

        if isinstance(error, commands.BotMissingPermissions):
            if error.missing_perms[0] == 'send_messages':
                return
            await ctx.reply(f"BotMissingPermissions **{' '.join(error.missing_perms[0].split('_')).title()}**", allowed_mentions=discord.AllowedMentions.none())

        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send_help(ctx.command) # Sends the help if the cmd isnt used properly

        raise error # Spammer boi
        
def setup(bot):
	bot.add_cog(Error(bot))