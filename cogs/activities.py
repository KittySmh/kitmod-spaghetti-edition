from discord.ext import commands
from discord_together import DiscordTogether
import os
import discord


class activities(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
 
    @commands.Cog.listener()
    async def on_ready(self):  
      token=os.getenv("TOKEN")  
      self.bot.togetherControl = await DiscordTogether(token)
    
    @commands.command()
    async def activities(self,ctx):
      embed=discord.Embed(title="List of Activities ⚔️", description="**Youtube Together** = `s!youtube`\n**Poker Night** = `s!poker`\n**Chess in the Park** = `s!chess`\n**Betrayal.io** = `s!betrayal`\n**Fishington.io** = `s!fishing`\n**Letter Tile** = `s!lettertile`\n**Word Snack** = `s!wordsnack`\n**Doodle Crew** = `s!doodle`\n**SpellCast** = `s!spellcast`\n** **\n__Mobile Users does not have the capability to join an activity due to discord limitations__\n** **")
      embed.set_footer(text="Every command stated above requires you to be in a Discord VC in order to work.")
      await ctx.send(embed=embed)

    @commands.command()
    async def youtube(self, ctx):
     link = await self.bot.togetherControl.create_link(ctx.author.voice.channel.id, 'youtube')
     embed= discord.Embed(title="Click To Begin!", description="Click the **__BLUE LINK__** if no one started the activity, click **Play/Spectetate** in order to join the currenly running activity!\n** **\n__Make sure that you're in a discord voice channel in order for this to work!__")
     await ctx.send(embed=embed,content=f"{link}")

    @commands.command()
    async def poker(self, ctx):
     link = await self.bot.togetherControl.create_link(ctx.author.voice.channel.id, 'poker')
     embed= discord.Embed(title="Click To Begin!", description="Click the **__BLUE LINK__** if no one started the activity, click **Play/Spectetate** in order to join the currenly running activity!\n** **\n__Make sure that you're in a discord voice channel in order for this to work!__")
     await ctx.send(embed=embed,content=f"{link}")

    @commands.command()
    async def chess(self, ctx):
     link = await self.bot.togetherControl.create_link(ctx.author.voice.channel.id, 'chess')
     embed= discord.Embed(title="Click To Begin!", description="Click the **__BLUE LINK__** if no one started the activity, click **Play/Spectetate** in order to join the currenly running activity!\n** **\n__Make sure that you're in a discord voice channel in order for this to work!__")
     await ctx.send(embed=embed,content=f"{link}")

    @commands.command()
    async def betrayal(self, ctx):
     link = await self.bot.togetherControl.create_link(ctx.author.voice.channel.id, 'betrayal')
     embed= discord.Embed(title="Click To Begin!", description="Click the **__BLUE LINK__** if no one started the activity, click **Play/Spectetate** in order to join the currenly running activity!\n** **\n__Make sure that you're in a discord voice channel in order for this to work!__")
     await ctx.send(embed=embed,content=f"{link}")

    @commands.command()
    async def fishing(self, ctx):
     link = await self.bot.togetherControl.create_link(ctx.author.voice.channel.id, 'fishing')
     embed= discord.Embed(title="Click To Begin!", description="Click the **__BLUE LINK__** if no one started the activity, click **Play/Spectetate** in order to join the currenly running activity!\n** **\n__Make sure that you're in a discord voice channel in order for this to work!__")
     await ctx.send(embed=embed,content=f"{link}")   

    @commands.command()
    async def lettertile(self, ctx):
     link = await self.bot.togetherControl.create_link(ctx.author.voice.channel.id, 'letter-tile')
     embed= discord.Embed(title="Click To Begin!", description="Click the **__BLUE LINK__** if no one started the activity, click **Play/Spectetate** in order to join the currenly running activity!\n** **\n__Make sure that you're in a discord voice channel in order for this to work!__")
     await ctx.send(embed=embed,content=f"{link}")   

    @commands.command()
    async def wordsnack(self, ctx):
     link = await self.bot.togetherControl.create_link(ctx.author.voice.channel.id, 'word-snack')
     embed= discord.Embed(title="Click To Begin!", description="Click the **__BLUE LINK__** if no one started the activity, click **Play/Spectetate** in order to join the currenly running activity!\n** **\n__Make sure that you're in a discord voice channel in order for this to work!__")
     await ctx.send(embed=embed,content=f"{link}")   

    @commands.command()
    async def doodle(self, ctx):
     link = await self.bot.togetherControl.create_link(ctx.author.voice.channel.id, 'doodle-crew')
     embed= discord.Embed(title="Click To Begin!", description="Click the **__BLUE LINK__** if no one started the activity, click **Play/Spectetate** in order to join the currenly running activity!\n** **\n__Make sure that you're in a discord voice channel in order for this to work!__")
     await ctx.send(embed=embed,content=f"{link}") 

    @commands.command()
    async def spellcast(self, ctx):
     link = await self.bot.togetherControl.create_link(ctx.author.voice.channel.id, 'spellcast')
     embed= discord.Embed(title="Click To Begin!", description="Click the **__BLUE LINK__** if no one started the activity, click **Play/Spectetate** in order to join the currenly running activity!\n** **\n__Make sure that you're in a discord voice channel in order for this to work!__")
     await ctx.send(embed=embed,content=f"{link}")       

    

def setup(bot):
  bot.add_cog(activities(bot))       