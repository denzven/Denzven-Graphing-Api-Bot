from discord.ext import commands

class Command(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command(self,ctx):
        self.bot.CommandNumber += 1
        server = ctx.guild.name
        channel = ctx.channel
        user = ctx.author
        command = ctx.command
        print(f'\n\n\n')
        print(f'+--------------------------------------------------+')
        print(f'| {server} > {channel} > {user} > {command}         ')
        print(f'+--------------------------------------------------+')
        print(f'| Bot-Usage: {self.bot.user}                        ')
        print(f'+--------------------------------------------------+')
        print(f'| Server: {server}                                  ')
        print(f'| Channel: {channel}                                ')
        print(f'| User: {user}                                      ')
        print(f'| Command: {command}                                ') 
        print(f'| Command content: {ctx.message.content}            ')
        print(f'| Command Number: {self.bot.CommandNumber}          ')
        print(f'+--------------------------------------------------+')
        print(f'\n\n\n') 

def setup(bot):
	bot.add_cog(Command(bot))