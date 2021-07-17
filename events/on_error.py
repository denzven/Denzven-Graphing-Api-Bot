from discord.ext import commands

class Error(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self,ctx, error):
        print(error)
        if isinstance(error,commands.BadArgument):
            await ctx.send('BadArgument')
        if isinstance(error, commands.errors.CommandInvokeError):
            await ctx.reply("CommandInvokeError")
        if isinstance(error, commands.CommandNotFound):
            await ctx.reply("CommandNotFound")
        if isinstance(error,commands.errors.CommandOnCooldown):
            await ctx.reply(f"CommandOnCooldown retry after {error.retry_after:.2f}s.")
        if isinstance(error, commands.errors.MissingPermissions):
            await ctx.reply(f"MissingPermissions {' '.join(error.NotOwner[0].split('_')).title()}")
            return
        if isinstance(error, commands.errors.NotOwner):
            await ctx.reply(f"NotOwner {error}")
            return
        #if isinstance(error,commands.MissingRequiredArgument):
        #    await ctx.reply('MissingRequiredArgument')
        if isinstance(error, commands.BotMissingPermissions):
            if error.missing_perms[0] == 'send_messages':
                return
            await ctx.reply(f"BotMissingPermissions **{' '.join(error.missing_perms[0].split('_')).title()}**")
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send_help(ctx.command)
        raise error
        

def setup(bot):
	bot.add_cog(Error(bot))