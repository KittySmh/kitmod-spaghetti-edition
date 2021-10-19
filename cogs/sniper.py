import discord
from discord.ext import commands
import datetime
import time
from datetime import timezone
import random
import os


errmsg = [1, 2, 3, 4]

class Snipe(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot.snipes = {}
        self.bot.edits = {}
    
    @commands.Cog.listener()
    async def on_message_delete(self, message):
     self.bot.snipes[message.channel.id] = message
     
    @commands.command()  
    async def snipe(self,ctx, *, channel: discord.TextChannel = None):
      if ctx.author.id == 484318483258015754:
       while True:
         channel = channel or ctx.channel
         try:
           msg = self.bot.snipes[channel.id]
           await ctx.send(embed=discord.Embed(description="", color=msg.author.color).set_author(name=f"{str(msg.author)}'s Sniped Message", icon_url=str(msg.author.display_avatar)).add_field(name="Message Content:",value=msg.content,inline=True).add_field(name="Time/Date:", value=(msg.created_at.strftime("Date: %A %d %B %Y | Time: %H:%M.%S | Timezone: %Z")),inline=True))
           return
         except KeyError:
           return await ctx.send('Nothing to snipe!')
            # one liner, dont complain
      else:
        if random.choice(errmsg) == 1:
         await ctx.reply("Congrats! You have discovered a command that's useless to you! ||*sarcasm!*||") 
         return  
        elif random.choice(errmsg) == 2:
         await ctx.reply("Dude, you do know that this command is restricted to devs?")
         return
        elif random.choice(errmsg) == 3:
         await ctx.reply("ERROR: You do not Have Access To This Command. <:nopp:865257334191030273>")
         return 
        elif random.choice(errmsg) == 4:
         await ctx.reply("You do not have permission to run the command: '**snipe**'")  
         return      
       
def setup(bot):
    bot.add_cog(Snipe(bot))            