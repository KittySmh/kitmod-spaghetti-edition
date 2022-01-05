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
        
    
  
    @tasks.loop(seconds=3600)
    async def petitnoob(self):
      m = await self.bot.fetch_user(844024083935133696)
      try:
         await m.send("PAY NOEL AND KYAN MONEI WHEN AH?????")
         print("Message sent to the retard")
      except:
        print("something went wrong, Probably that I cant DM the user")




    @tasks.loop(seconds=7200) 
    async def routwarn(self):
        embed= discord.Embed(title="Kind Routine Warning!", description = "Be Sure to Follow the rules at all times!",timestamp=datetime.datetime.now()).set_footer(text="Ignoring this will result in a moderation.")
        channel = discord.utils.get(self.bot.get_all_channels(), guild__name = 'GalaxyBlox_YT Community!!!', name = 'chat')
        nutz = await channel.send(embed=embed)

def setup(bot):
    bot.add_cog(routwarn(bot))      