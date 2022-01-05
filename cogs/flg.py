import discord
from discord.ext import tasks, commands
import asyncio
import random
import datetime
import random
import os
from datetime import timezone

token = os.environ.get("TOKEN")

class flg(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_message(self, message):
       invite = "https://discord.gg"
       skam="https://dlcsorcl.com"
       nooblonk = "https://tenor.com/view/roblox-gif-23755795"
       hidmod = discord.utils.get(message.guild.roles, name="Moderation Advisor")
       role = discord.utils.get(message.guild.roles, name="Override Perms")
       bots = discord.utils.get(message.guild.roles, name="Bots")
       admLR = discord.utils.get(message.guild.roles, name="Moderator")
       muted = discord.utils.get(message.guild.roles, name="Muted")
       retard = "😈"
       taik = "taik"
       Taik2 = "Taik"
       nou = "no u"
       nob = "noob"
       dnc = "dnc"
       noab = "noab"
       troll = "troll"
       n = datetime.datetime.now(timezone.utc)
       day = n.strftime("%A %d %B %Y")
       tim = n.strftime("%H:%M.%S | Timezone: %Z")
       h3 = "h3"
       if hidmod in message.author.roles:
          return


       elif nooblonk in message.content: 
         await message.delete()
         await message.channel.send(f"{message.author.mention}, Do not.")  

       elif troll in message.content:
         if message.author.id == 844024083935133696:
           await message.delete()
           await message.channel.send(f"No trolling {message.author.mention}")
           return
         else:
           return
         
      
       
       elif skam in message.content:
        await message.delete()
        try:
          await message.author.ban(delete_message_days=7)
          await message.author.unban()
          await message.channel.send(f"{message.author} has been softbanned due to a scam link.")
          return
        except:
          await message.author.add_roles(muted)  
          await message.channel.send("**Scam link Detected.** Unable to softban user, user has been muted. <@&898561560941821983>, please handle the issue.")
          return
       
  

       else:
        return    

          

      

def setup(bot):
    bot.add_cog(flg(bot)) 