import discord
from discord.ext import commands
import datetime
import random
import os

token = os.environ.get("TOKEN")

class BotConfig(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def Code4(self, ctx):
     if ctx.message.author.id == 484318483258015754:
        while True:
            await ctx.send('Code 4 on the scene. 19-2 Calling it a night.')
            await self.logout()
        else:
            await ctx.reply(
                '<:nopp:865257334191030273> Hey! This is restricted to SVPM HICOMs only!'
            )

    @commands.command()
    async def restart(self, ctx):
     if ctx.message.author.id == 484318483258015754:
        while True:
            await ctx.send('Restart SPVM Systems. Please Stand By...')
            await self.bot.logout()
            await self.bot.login(token)
        else:
            await ctx.reply(
                '<:nopp:865257334191030273> Hey! This is restricted to SVPM HICOMs only!'
            ) 

def setup(bot):
    bot.add_cog(BotConfig(bot)) 