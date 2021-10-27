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
      hidmod = discord.utils.get(message.guild.roles, name="Hidden Moderator || HR")
      role = discord.utils.get(message.guild.roles, name="Override Perms")
      bots = discord.utils.get(message.guild.roles, name="Bots")
      admLR = discord.utils.get(message.guild.roles, name="Moderator || LR")
      admMR = discord.utils.get(message.guild.roles, name="Moderator || MR")
      admHR = discord.utils.get(message.guild.roles, name="Moderator || HR")
      appr = discord.utils.get(self.bot.get_all_channels(), guild__name = 'GalaxyBlox_YT Community!!!', name = 'admin-app-stuff')
      muted = discord.utils.get(message.guild.roles, name="Muted")
      blcklist = discord.utils.get(message.guild.roles, name="Blacklisted from ModApps")
      n = datetime.datetime.now(timezone.utc)
      day = n.strftime("%A %d %B %Y")
      tim = n.strftime("%H:%M.%S | Timezone: %Z")
      if invite in message.content:
        if hidmod in message.author.roles:
          return
        elif role in message.author.roles:
          return  
        elif bots in message.author.roles:
          return
        else:
          await message.delete()
          await message.author.ban(delete_message_days=7)
          await message.author.unban()
          await message.channel.send(f"{message.author} has been softbanned due to an invite link.")
          return

      if skam in message.content:
        await message.delete()
        try:
          await message.author.ban(delete_message_days=7)
          await message.author.unban()
          await message.channel.send(f"{message.author} has been softbanned due to a scam link.")
          return
        except:
          await message.author.add_roles(muted)  
          await message.channel.send("**Scam link Detected.** Unable to softban user, user has been muted. <@484318483258015754>, please handle the issue.")
          return


      if message.channel.id == 875381860086206504:
       if hidmod in message.author.roles:
          await message.delete()
          await message.author.send(f"You have the role **Hidden Moderator || HR**. You are not eligible to apply for moderator.")
          return
          
       elif admLR in message.author.roles:
          await message.delete()
          await message.author.send(f"You have the role **Moderator || LR**. You are not eligible to apply for moderator.")
          return

       elif admMR in message.author.roles:    
          await message.delete()
          await message.author.send(f"You have the role **Moderator || MR**. You are not eligible to apply for moderator.")
          return

       elif admHR in message.author.roles: 
          await message.delete()
          await message.author.send(f"You have the role **Moderator || HR**. You are not eligible to apply for moderator.")   
          return

       elif blcklist in message.author.roles:   
         await message.delete()
         await message.author.send("You have been blacklisted from the current Season of Moderator Applications. Apply during the next season!") 
         return

       else:
          await appr.send(f"**New Application** \n User: **{message.author.mention}** \n **Application:** \n{message.content} \n **Time Of Application:** {tim}\n **Day Of Application:** {day} \n||<@&891906754118561842>||")
          await message.delete()
          await message.author.send("Your Application has been forwarded to the Application Readers. <:yass:865257334023782400>")
          return

      elif message.channel.id == 893119497593032774:
         reaction = "🎉"
         await message.add_reaction(reaction)
      
      

      else:
        return    

          

      

def setup(bot):
    bot.add_cog(flg(bot)) 