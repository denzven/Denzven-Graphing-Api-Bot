from discord.ext import commands
from config import *

import aiohttp 

class NotVotedError(commands.CheckFailure):
    pass

async def check_voter(user_id):
    CHECK_IF_VOTER_LINK = f'https://top.gg/api/bots/851532461061308438/check?userId={user_id}'
    try:
        headers = {
           'Authorization': TOPGG_TOKEN 
        }
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.get(CHECK_IF_VOTER_LINK) as r:
                if "application/json" in r.headers["Content-Type"]:
                    json_out = await r.json()
                    if json_out['voted'] == 1:
                        return True
                    if json_out['voted'] == 0:
                        return False
                    else:
                        return json_out
                        
    except Exception as e:
        print(str(e))

def voter_only():
    async def predicate(ctx):
        thing = await check_voter(ctx.author.id)
        if thing == False:
            raise NotVotedError('Beg for votes msg')
        return True
    return commands.check(predicate)