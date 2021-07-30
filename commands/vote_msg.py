# In-Process

# Imports
import discord 
import random 
from discord.ext import commands 

#Config
from config import * 

class VoteMsg(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.vote_tracking_bot_id = 702134514637340702
        self.vote_scraping_channel_id = VOTE_SCRAPING_CHANNEL
        self.vote_sending_channel_id = VOTE_SENDING_CHANNEL

    @commands.Cog.listener("on_message")
    async def get_vote(self, message: discord.Message):
        # print("msg recieved")
        if message.author.id != self.vote_tracking_bot_id:
           # print("not from vtbot")
            return
        if message.channel.id != self.vote_scraping_channel_id:
            print("not in the channel")
            return
        #if len(message.embeds) != 1:
        #    print('no embed in msg recieved from bot in channel')
        #    return
        try:
            voter_id = int(message.embeds[0].title)
            print(voter_id)
            votes = int(message.embeds[0].description)
            print(votes)
            channel = self.bot.get_channel(self.vote_sending_channel_id)
            await channel.send(
                f"Thx a ton! <@{voter_id}> for voting me! {random.choice(CUTE_EMOJIS)}\nYou have a total of **{votes}** votes now! {random.choice(CUTE_EMOJIS)}"
            )

        except Exception as e:
            print(e)
            return

def setup(bot):
    bot.add_cog(VoteMsg(bot))