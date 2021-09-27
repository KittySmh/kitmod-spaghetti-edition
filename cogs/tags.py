import discord
from discord.ext import commands
import datetime
import random
import os

class Tags(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group()
    async def tag(self, ctx):
     await ctx.send("**Tags:** staff,whatisslowmode ,tachankai, vietnam, spd, ainsley, rookmine, ban, banhammer, h2b, mute, cheezy")

    @tag.command()
    async def cheezy(self, ctx):
      await ctx.send("https://images-ext-2.discordapp.net/external/Q0tpr5XiY4gjO03VWaRHn9soTWdxYrYXeNwTBi4kYm8/https/i.redd.it/ldkuajdxeowy.png?width=699&height=468")  



    @tag.command()
    async def h2b(self, ctx):    
     await ctx.send("https://media.discordapp.net/attachments/859636474148421652/875748015476965506/bMyYTIor.jpg")  

    @tag.command()
    async def banhammer(self, ctx):
      await ctx.send("https://images-ext-1.discordapp.net/external/jqvQ9Qnens11iG6gOWqJ-iS2nN7_Z2XNE2hR_RKzrdA/https/i.imgur.com/65ZAxKw.jpg?width=832&height=468")

    @tag.command()
    async def ban(self, ctx):
      await ctx.send("https://gfycat.com/BountifulAmpleAffenpinscher")

    @tag.command()
    async def ainsley(self, ctx):
      await ctx.send("https://media.discordapp.net/attachments/859636474148421652/875747345738911835/dfBNYxP.png")

    @tag.command()
    async def rookmine(self, ctx):
      await ctx.send("https://media.discordapp.net/attachments/278986547187941377/279737279856246784/mt7xsrvAm3pDhOxEQFPtIHA0WUvMrpQ4i5ZAr-qWJRg.png?width=351&height=468")

    @tag.command()
    async def staff(self, ctx):
      await ctx.send("https://media.discordapp.net/attachments/253581140072464384/309729949357703178/Staffprivilage.jpg?width=445&height=468")

    @tag.command()
    async def whatisslowmode(self, ctx):
      await ctx.send("https://gfycat.com/FabulousInferiorBeardedcollie")

    @tag.command()
    async def tachankai(self, ctx):
      await ctx.send("https://media.discordapp.net/attachments/253581140072464384/309074052805296128/stolen.png?width=606&height=468")

    @tag.command()
    async def vietnam(self, ctx):
      await ctx.send("https://media.discordapp.net/attachments/253581140072464384/280448600352358401/f24a8e58dee05cfd385e127a7a80ecf4.png")

    @tag.command()
    async def spd(self, ctx):
      await ctx.send("https://media.discordapp.net/attachments/253581140072464384/805634251151245333/image01.png")

def setup(bot):
    bot.add_cog(Tags(bot))    