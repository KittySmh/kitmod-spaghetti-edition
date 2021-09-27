import discord
from discord.ext import tasks, commands
import asyncio
import random
import datetime

class routwarn(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        self.routwarn.start()

    @tasks.loop(seconds=7200) 
    async def routwarn(self):
        embed= discord.Embed(title="Kind Routine Warning!", description = "Do not use any bad/NSFW words anywhere except for <#859608400811130900> !",timestamp=datetime.datetime.now()
        ).set_footer(text="Ignoring this will result in a moderation.")
        channel = discord.utils.get(self.bot.get_all_channels(), guild__name = 'GalaxyBlox_YT Community!!!', name = 'chat')
        await channel.send(embed=embed)

def setup(bot):
    bot.add_cog(routwarn(bot))      