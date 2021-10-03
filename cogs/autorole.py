import discord
from discord.ext import tasks, commands
import asyncio
import random
import datetime
import random
import os
from datetime import timezone

token = os.environ.get("TOKEN")

class AdmFlg(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_member_join(self, member:discord.Member):
        galatians = discord.utils.get(self.guild.roles, name="galatians")
        channel = discord.utils.get(self.bot.get_all_channels(), guild__name = 'GalaxyBlox_YT Community!!!', name = 'mod-logs')
        await member.add_roles(galatians)
        embed= discord.Embed(title="New Member", description="")
        embed.add_field(name="Member Username:", value=f"{member.mention}",inline=True)
        embed.add_field(name="Roles Given:", value=f"galatians",inline=True)
        await channel.send(embed=embed)
        return


def setup(bot):
    bot.add_cog(AdmFlg(bot))     