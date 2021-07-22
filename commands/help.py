import discord
from discord.ext import commands
import datetime
from config import *
HELP_BTNS_OPTIONS = [
    discord.SelectOption(label = 'fgr'    ,value = 'flat_graph'   ,description = 'qq' ),
    discord.SelectOption(label = 'fgrem'  ,value = 'fgrem' ,description = 'qq' ),
    discord.SelectOption(label = 'pgr'    ,value = 'pgr'   ,description = 'qq' ),
    discord.SelectOption(label = 'pgrem'  ,value = 'pgrem' ,description = 'qq' ),
    discord.SelectOption(label = '3dgr'   ,value = '3dgr'  ,description = 'qq' ),
    discord.SelectOption(label = '3dgrem' ,value = '3dgrem',description = 'qq' ),
]


async def get_command_help(command,context):
        #command = context.bot.get_command_help(command)
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
            ).add_field(name='‎‎', value=f"[Invite Me]({BOT_INVITE_LINK}) | [Support Server]({SUPPORT_SERVER_LINK})", inline=False)
        return embed
            #await ctx.reply(embed=embed, allowed_mentions=discord.AllowedMentions.none())
 

class BotHelpSelect(discord.ui.Select):
    def __init__(self, placeholder, options, ctx):
        super().__init__(
            placeholder=placeholder,
            options=HELP_BTNS_OPTIONS,
        )
        self.ctx = ctx

    async def callback(self, i):
        await i.response.send_message(embed =await get_command_help(self.ctx.bot.get_command(self.values[0]),self.ctx)
        #await i.response.send_message(type(await self.ctx.send_help(self.values[0]))
        , ephemeral=True)


class MyHelpCommand(commands.HelpCommand):
    async def send_bot_help(self, cog):
        embed,view_ui = await self.get_bot_help(self.context)
        await self.context.reply(embed = embed,view=view_ui)

    #async def get_bot_help(self, mapping):
    async def get_bot_help(cog, context):
            ctx = context
            #views = 
            view_ui = discord.ui.View(timeout=None)
            select = BotHelpSelect(
                placeholder="Select a category.",
                options=HELP_BTNS_OPTIONS,
                ctx=ctx
            )
            view_ui.add_item(select)
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
                description="This Bot is a showcase of the use of Denzven-Graphing-Api \n```py\n try using >help <command> at each of the below sections```\n\n\n", timestamp=datetime.datetime.utcnow())
            embed.set_image(url=API_COVER_PIC)
            embed.set_thumbnail(url=BOT_AVATAR)
            embed.set_footer(text=f'rendered by {ctx.author.name}',icon_url=ctx.author.avatar.url)
            embed.add_field( name = "GraphingCommands"      , value=">fgr <input_formula> [attr] \n>pgr <input_formula> [attr] \n>3dgr <input_formula> [attr] \n"                                          , inline=False)
            embed.add_field( name = "GraphingCommandsEmbed" , value=">fgrem <input_formula> [attr] \n>pgrem <input_formula> [attr] \n>3dgrem <input_formula> [attr] \n"                                    , inline=False)
            embed.add_field( name = "OtherCommands"         , value=">attr \n>docs \n>github \n>ping \n>pypi  \n>src \n>website \n>prefix \n>attr \n", inline=False)
            embed.add_field( name = "OwnerCommands"         , value=">jsk"                                                                          , inline=False)
            return embed,view_ui
            #await ctx.reply(content=f"**Help has arrived!** \n run `>prefix` to find out the prefix", embed=embed,view=view_ui)
    async def send_command_help(self, command):
        embed = await get_command_help(command,self.context)
        await self.context.reply(embed = embed)

    # This function triggers when someone type `<prefix>help <cog>`
    async def send_cog_help(self, cog):
            ctx = self.context
            if cog == 'help':
                    return
            else:
                    embed = discord.Embed(color=MAIN_COLOR)
                    embed.set_author(name=f'{cog.qualified_name} Help')
                    for thing in cog.get_commands():
                            embed.add_field(name=thing.qualified_name, value=f'Description: {thing.help}\nUsage: {self.clean_prefix}{thing.qualified_name} {thing.signature}', inline=False)
                    await ctx.send(embed=embed)
            # Do what you want to do here


    async def send_group_help(self, group):
            ctx = self.context
            embed = discord.Embed(color=MAIN_COLOR)
            embed.set_author(name=f'{group.qualified_name} Help')
            for thing in group.commands:
                embed.add_field(name=thing.qualified_name, value=f'Description: {thing.help}\nUsage: {thing.qualified_name} {thing.signature}', inline=False)
            await ctx.send(embed=embed)
            
                
class Help(commands.Cog):
    """Shows this command, allows for in-depth explanations."""
    def __init__(self, bot):
        self.bot = bot
        
        # Storing main help command in a variable
        self.bot._original_help_command = bot.help_command
        
        # Assiginig new help command to bot help command
        bot.help_command = MyHelpCommand()
        
        # Setting this cog as help command cog
        bot.help_command.cog = self
        
        # Event triggers when this cog unloads
    def cog_unload(self):
                
        # Setting help command to the previous help command so if this cog unloads the help command restores to previous
        self.bot.help_command = self.bot._original_help_command


def setup(bot):
        bot.add_cog(Help(bot))