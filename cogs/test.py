import discord
from discord.ext import commands
import datetime
import random
import os

class whoistest(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def fetchuser(self, ctx, userID):
      m = await self.bot.fetch_user(userID)
      embed=discord.Embed(title=m.name+"'s Information",description="User is not in the server",timestamp=ctx.message.created_at)
      embed.set_thumbnail(url=m.avatar)
      e = m.created_at.strftime("%b %d, %Y, %I:%M UTC")
      embed.add_field(name=f"General Information:", value=f"Mention: {m.mention}\nUsername: {m.name}\nAccount Created On: {e}")
      embed.set_footer(text=f"ID: {m.id}")
      await ctx.send(embed=embed)
      

def setup(bot):
    bot.add_cog(whoistest(bot))          