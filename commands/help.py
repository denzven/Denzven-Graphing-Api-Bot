# This is Help cmd, some parts are dynamic, 
# but most of it is hard coded (i have to make it more dynamic but meh)

# Imports
import discord
from discord.ext import commands
import datetime

# Config
from config import *

#################################################################################################################

# a funtion to get the command_help Embed
async def get_command_help(command,context):
        embed = discord.Embed(
            colour=MAIN_COLOR,
            title=f'{command.qualified_name}'
            )
        use = ""
        aliases = ""
        for cancer in command.clean_params:
            use += f"<{cancer}> "
        for alias in command.aliases:
            aliases += f"`{alias}` "
        embed=discord.Embed(
            title=f"{command.name.title()} Help",
            description=f"""
    {command.help}
    
    **Usage:**
    ```
{command.name} {use}
    ```
    **Aliases:** {aliases if len(aliases) > 0 else "None"}
    **Cooldown:** {0 if command._buckets._cooldown == None else command._buckets._cooldown.per} seconds
                            """,
            color=MAIN_COLOR,
            timestamp=datetime.datetime.utcnow()
            ).set_footer(text=f"Requested by {context.author}"
            ).set_author(name=context.bot.user.name, icon_url=BOT_AVATAR
            ).set_thumbnail(url=BOT_AVATAR
            ).add_field(name=EMPTY_CHAR, value=f"[Invite Me]({BOT_INVITE_LINK}) | [Support Server]({SUPPORT_SERVER_LINK})", inline=False)
        return embed

#################################################################################################################
 
# Button Class
class BotHelpSelect(discord.ui.Select):
    def __init__(self, placeholder, options, ctx):
        super().__init__(
            placeholder=placeholder,
            #options=HELP_BTNS_OPTIONS,
            options=options,
        )
        self.ctx = ctx
    async def callback(self, i):
        if i.user == self.ctx.author:
            try:
                await i.response.send_message(await self.ctx.invoke(self.ctx.bot.get_command(self.values[0])))
            except:
                await i.response.send_message(embed=await get_command_help(self.ctx.bot.get_command(self.values[0]),self.ctx),ephemeral=True)
        else:
            await i.response.send_message("This is not your Help msg, Kindly run >help to continue",ephemeral=True)



#################################################################################################################

# Sub-Classing the Help Command
class MyHelpCommand(commands.HelpCommand):

    async def send_bot_help(self, mapping):# works at >help
        async with self.context.typing(): 
            options = []
            try:
                for cogs, commands in mapping.items():
                    for command in commands:
                        if not command.hidden:
                            options.append(discord.SelectOption(
                            label=command.qualified_name.title(),
                            description=command.description,
                            value=command.qualified_name,
                            emoji=EMOJI_FOR_CMDS[command.name]
                            ))            
            except Exception as e:
                print(e)
            embed,view_ui = await self.get_bot_help(self.context,options)
            await self.context.reply(embed = embed,view=view_ui)

#################################################################################################################

    async def get_bot_help(cog, context,options): # gives the help cmd Embed
        ctx = context
        view_ui = discord.ui.View(timeout=60)
        select = BotHelpSelect(
            placeholder="Get Help on a Commmand.",
            options=options,
            ctx=ctx
        )
        view_ui.add_item(select)

        #select2 = BotHelpSelect(
        #    placeholder="Invoke a cmd",
        #    options=options,
        #    ctx=ctx
        #)
        #view_ui.add_item(select2)

        view_ui.add_item(discord.ui.Button(
            style=discord.ButtonStyle.url,
            url=API_BASE_LINK,
            label="website",
        ))

        view_ui.add_item(discord.ui.Button(
            style=discord.ButtonStyle.url,
            url=SUPPORT_SERVER_LINK,
            label="support server",
        ))

        view_ui.add_item(discord.ui.Button(
            style=discord.ButtonStyle.url,
            url=BOT_GITHUB_LINK,
            label="github (src)",
        ))

        embed = discord.Embed(
                title="Denzven-Graphing-Api-Bot", 
                colour=MAIN_COLOR, 
                description="This Bot is a showcase of the use of Denzven-Graphing-Api \n```py\n try using >help <command> at each of the below sections```\n\n\n", timestamp=datetime.datetime.utcnow()
                )

        embed.set_image(url=API_COVER_PIC)
        embed.set_thumbnail(url=BOT_AVATAR)
        embed.set_footer(text=f'rendered by {ctx.author.name}',icon_url=ctx.author.avatar.url)
        p = DEFAULT_PREFIX
        embed.add_field( name = "GraphingCommands"      , value=f"{p}fgr <input_formula> [attr] \n{p}pgr <input_formula> [attr] \n{p}3dgr <input_formula> [attr] \n{p}dgr <input_formula> \n"      , inline=False)
        embed.add_field( name = "GraphingCommandsEmbed" , value=f"{p}fgrem <input_formula> [attr] \n{p}pgrem <input_formula> [attr] \n{p}3dgrem <input_formula> [attr] \n{p}dgrem <input_formula> \n", inline=False)
        embed.add_field( name = "OtherCommands"         , value=f"{p}attr \n{p}docs \n{p}github \n{p}ping \n{p}vote  \n{p}src \n{p}website \n{p}prefix \n{p}changelog \n{p}botlist \n{p}botinfo \n"                  , inline=False)
        embed.add_field( name = "OwnerCommands"         , value=f"{p}jsk"                                                                                             , inline=False)
        return embed,view_ui # also btns, if i forgot to say that

#################################################################################################################

    async def send_command_help(self, command): # works at >help <cmd>
        async with self.context.typing(): 
            embed = await get_command_help(command,self.context) # calls the embed thingy.. so yea
            await self.context.reply(embed = embed)

#################################################################################################################

    async def send_cog_help(self, cog): # works at >help <cog> (wont use it tho)
            ctx = self.context
            if cog == 'help':
                return
            else:
                embed = discord.Embed(color=MAIN_COLOR)
                embed.set_author(name=f'{cog.qualified_name} Help')
                for thing in cog.get_commands():
                        embed.add_field(name=thing.qualified_name, value=f'Description: {thing.help}\nUsage: {self.clean_prefix}{thing.qualified_name} {thing.signature}', inline=False)
                await ctx.send(embed=embed)

#################################################################################################################

    async def send_group_help(self, group): # works at >help <grp> (mostly for jsk actually)
            ctx = self.context
            embed = discord.Embed(color=MAIN_COLOR)
            embed.set_author(name=f'{group.qualified_name} Help')
            for thing in group.commands:
                embed.add_field(name=thing.qualified_name, value=f'Description: {thing.help}\nUsage: {thing.qualified_name} {thing.signature}', inline=False)
            await ctx.send(embed=embed)

#################################################################################################################
            
class Help(commands.Cog): 
    """Shows this command, allows for in-depth explanations."""

    def __init__(self, bot): # Some essential stuff that i have no idea about
        self.bot = bot
        self.bot._original_help_command = bot.help_command
        bot.help_command = MyHelpCommand()
        bot.help_command.cog = self

    def cog_unload(self):
        self.bot.help_command = self.bot._original_help_command
        
#################################################################################################################

def setup(bot):
        bot.add_cog(Help(bot))