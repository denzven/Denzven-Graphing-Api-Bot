from discord.ext import commands
import discord
from config import *

class VeryNiceView(discord.ui.View): # this is a view class, we can reuse this view whenever we want
    def __init__(self, ctx):
        super().__init__()
        self.ctx = ctx # ctx part is optional but it is recommended

    @discord.ui.button(label='test button', style=discord.ButtonStyle.green)
    async def test_button(self, button: discord.ui.Button, interaction: discord.Interaction): # this is the function that gets called when the button is pressed
        await interaction.response.send_message(f'{interaction.user} has clicked the button') # this will reply when someone clicks the button
        # you can use `ephemeral=True` if u want to make it "Only you can see this messsage" kind of message

    # Notes about views:
        # They have a timeout of 180 seconds by default that means after 180 seconds u will get "interaction failed" thing
        # ^ you can put `timeout=None` in the `super().__init__()` to make it infinite
        # Also, if u want to stop a view you can do `self.stop()` which will stop it and on clicking u would get "interaction failed" thing

class MyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def button_test(self, ctx):
        view = VeryNiceView(ctx=ctx)
        await ctx.reply("this is a nice test for buttons", view=view)

def setup(bot):
    bot.add_cog(MyCog(bot))