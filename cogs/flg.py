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
    async def on_message(self, message):
      hidmod = discord.utils.get(message.guild.roles, name="Hidden Moderator || HR")
      admLR = discord.utils.get(message.guild.roles, name="Moderator || LR")
      admMR = discord.utils.get(message.guild.roles, name="Moderator || MR")
      admHR = discord.utils.get(message.guild.roles, name="Moderator || HR")
      appr = discord.utils.get(self.bot.get_all_channels(), guild__name = 'GalaxyBlox_YT Community!!!', name = 'admin-app-stuff')
      blcklist = discord.utils.get(message.guild.roles, name="Blacklisted from ModApps")
      n = datetime.datetime.now(timezone.utc)
      day = n.strftime("%A %d %B %Y")
      tim = n.strftime("%H:%M.%S | Timezone: %Z")
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

      if message.channel.id == 893119497593032774:
         reaction = "🎉"
         await message.react(reaction)

      else:
        return    

          

      

def setup(bot):
    bot.add_cog(AdmFlg(bot)) 