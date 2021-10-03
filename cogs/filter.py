import discord
from discord.ext import commands
import os
import asyncio
import datetime
import time
from datetime import timezone

class Filter(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    with open('BadWords.txt', 'r') as f:
     global badwords  # You want to be able to access this throughout the code
     words = f.read()
     badwords = words.split()

    
    
    

    @commands.Cog.listener()
    async def on_message(self, message):
      
      
      for word in badwords:
       if word in message.content:
         role = discord.utils.get(message.guild.roles, name="Override Perms")
         muted = discord.utils.get(message.guild.roles, name="Muted")
         hidmod = discord.utils.get(message.guild.roles, name="Hidden Moderator || HR")
         channel1 = discord.utils.get(message.guild.text_channels, name="mod-logs")
         rrrrrr = discord.utils.get(message.guild.roles, name="rrrrrr")
         n = datetime.datetime.now(timezone.utc)
         day = n.strftime("%A %d %B %Y")
         tim = n.strftime("%H:%M.%S | Timezone: %Z")
         counter = 0
         if message.author.id == 484318483258015754:
           return

         elif message.channel.id == 859608400811130900:
           return 
         
         elif rrrrrr in message.author.roles:
           while True:
             return

         elif role in message.author.roles:
          while True:
             return

         elif hidmod in message.author.roles:
          while True:
             return    

         elif message.author.guild_permissions.kick_members:
           while True:
             with open("flagsystem.txt", "r+") as file:
               await message.channel.send(f"Flag Added for {message.author.display_name}.")
               file.write(f"{message.author} - {message.content}. Time of Flag = {day}, Date of Flag: {tim}\n")
               for lines in file:
                 return
                 if lines.strip("\n") == str(message.author.id):
                   counter+=1
                   return
         
         else:
           embed = discord.Embed(title = "User Muted", description = f"{message.author} has been muted for using a moderated word ({message.content})",timestamp=datetime.datetime.now(),
           colour=discord.Colour.red())
           embed.set_thumbnail(url=message.author.display_avatar)
           await channel1.send(embed=embed)
           await message.delete()
           await message.author.add_roles(muted)
           await message.channel.send(f"{message.author.mention} has been muted for a period of 1 hour for using a moderated word.")
           await asyncio.sleep(3600)
           if muted in message.author.roles:
             while True:
               await message.author.remove_roles(muted)
               await message.channel.send(f"{message.author.mention} has been unmuted. Do not use moderated words again.")
               return
           else:
             return  
      
      

def setup(bot):
  bot.add_cog(Filter(bot))    