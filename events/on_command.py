# This is a On_command Event for Logging the cmds

# Imports
from discord.ext import commands
import discord
import datetime
# Config
from config import *

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
        desc = f'''
        \n\n\n
        +--------------------------------------------------+
        | {server} > {channel} > {user} > {command}         
        +--------------------------------------------------+
        | Bot-Usage: {self.bot.user}                        
        +--------------------------------------------------+
        | Server: {server}                                  
        | Channel: {channel}                                
        | User: {user}                                      
        | Command: {command}                                 
        | Command content: {ctx.message.content}            
        | Command Number: {self.bot.CommandNumber}          
        +--------------------------------------------------+
        \n\n\n
        '''
        print(desc)
        embed=discord.Embed(title=f"Command", color=MAIN_COLOR)
        embed.add_field(name="Server", value=f'```{ctx.guild.name} ({ctx.guild.id})```',inline=False)
        embed.add_field(name="Channel", value=f'```{ctx.channel.name} ({ctx.channel.id})```',inline=False)
        embed.add_field(name="User", value=f'```{ctx.author.name} ({ctx.author.id})```',inline=False)
        embed.add_field(name="Command", value=f'```{ctx.command}```',inline=False)
        embed.add_field(name="Content", value=f'```{ctx.message.content}```',inline=False)
        embed.timestamp = datetime.datetime.utcnow()
        log_channel = self.bot.get_channel(LOG_ON_CMD)
        await log_channel.send(embed = embed) 

def setup(bot):
	bot.add_cog(Command(bot))