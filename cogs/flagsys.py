import discord
from discord.ext import commands


class flagsys(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
 
    

    @commands.command()
    async def modflags(self, ctx):
     
      hidmod = discord.utils.get(ctx.guild.roles, name="Moderation Supervisor || SHR")
      role = discord.utils.get(ctx.guild.roles, name="Override Perms")

      with open('flagsystem.txt', 'r') as f:
       global flags  # You want to be able to access this throughout the code
       words = f.read()
      
      if role in ctx.author.roles:
        embed=discord.Embed(title="Server Flags", description=f"{words}")
        await ctx.send(embed=embed)
        return
           

      elif hidmod in ctx.author.roles:
        embed=discord.Embed(title="Server Flags", description=f"{words}")
        await ctx.send(embed=embed)
        return
       
      
      else:
          await ctx.reply("You do not have sufficient permissions to use this command.")  
          return  
    
    @commands.command(aliases=["blw"])
    async def blacklist(self, ctx, word):
      if ctx.author.id == 484318483258015754:
       while True:
         with open("BadWords.txt", "r+") as file:
           file.write(f"{word} ")
           self.bot.reload_extension(f"cogs.filter")
           await ctx.reply(f"The Word **{word}** has been added to **BadWords.txt**")
           return

      else:
        await ctx.reply("You do not have sufficient permissions to use this command.")     

    @commands.command()    
    async def clearflags(self,ctx):
     if ctx.author.id == 484318483258015754:
       with open("flagsystem.txt", "r+") as file: 
         file.truncate(0)
         await ctx.reply("**flagsystem.txt** has been cleared. All Server Flags has been removed.")
         return 
     else:
       await ctx.reply("You do not have sufficient permissions to use this command.")

       
def setup(bot):
  bot.add_cog(flagsys(bot))         