import discord
from discord.ext import commands
import datetime
import random
import os
from discord import Spotify
import asyncio
import random


determine_flip = [1, 0]

class Random(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    


    @commands.command()
    async def coinflip(self, ctx):
     if random.choice(determine_flip) == 1:
        embed = discord.Embed(
            title=f"{ctx.author.name}'s Coinflip",
            description=
            f"{ctx.author.mention} Flipped the coin, we got **Heads**!",
            colour=discord.Color.gold(),
            timestamp=datetime.datetime.now()).set_footer(
                text="Test Your Luck with s!coinflip")
        await ctx.send(embed=embed)

     else:
        embed = discord.Embed(
            title=f"{ctx.author.name}'s Coinflip",
            description=
            f"{ctx.author.mention} Flipped the coin, we got **Tails**!",
            colour=discord.Color.gold(),
            timestamp=datetime.datetime.now()).set_footer(
                text="Test Your Luck with s!coinflip")
        await ctx.send(embed=embed)    

    @commands.command()
    async def announce(self, ctx, *, text):
     if ctx.message.author.id == 484318483258015754:
        message = ctx.message
        await message.delete()

        await ctx.send(f"{text}")
     else:
        await ctx.reply("You don't have access to this command.")
 
    @commands.command()
    async def dm(self, ctx,member: discord.Member = None, *, msg = None):
     if ctx.message.author.id == 484318483258015754:
       while True:
         if member == None:
           d = await ctx.reply("Please **Mention** a user!")
           await asyncio.sleep(30)
           await d.delete()
           await ctx.message.delete()
           return
         else:
           if msg == None:
             c = await ctx.reply("Do the command again. but **State What  you would like to be sent** to the user!")
             await asyncio.sleep(30)
             await c.delete()
             await ctx.message.delete()
             return
           else:
             try:
               await member.send(msg) 
               b = await ctx.reply("Message Sent!")
               await asyncio.sleep(30)
               await b.delete()
               await ctx.message.delete()
               return
             except:
               a = await ctx.reply("I was unable to sent the message to   the user. **Ensure that they have their DMs enabled for this server!**") 
               await asyncio.sleep(30)
               await a.delete()
               await ctx.message.delete()
               return
       else:
         await ctx.reply("You Don't Have Access To This Command.") 

    @commands.command()
    async def spotify(self, ctx, user: discord.Member = None):
     if user == None:
        user = ctx.author

     if user.activities:
        for activity in user.activities:
          if isinstance(activity, Spotify):
                embed = discord.Embed(
                    title=
                    f"{user.name}'s Current Spotify Soundtrack  <:Spotifyyyy:866309114543865867>",
                    description="Listening to **{}**".format(activity.title),
                    color=discord.Colour.gold())
                embed.set_thumbnail(url=activity.album_cover_url)
                embed.add_field(name="Artist", value=activity.artist)
                embed.add_field(name="Album", value=activity.album)
                embed.set_footer(text="Started listening to spotify on {} UTC".format(
                    activity.created_at.strftime("%H:%M")))
                await ctx.send(embed=embed)
                return

          else:
            await ctx.send("It may have appears that you aren't listening to **Spotify**<:Spotifyyyy:866309114543865867> right now. Perhaps give it a shot at: https://www.spotify.com/ ???")
            return

    @commands.command()
    async def comms(self, ctx):
     await ctx.reply(
        f'**SVPM Radio Comms Latency** = {round(self.bot.latency * 1000)} ms')
    
    @commands.command()
    async def banner(self,ctx,member:discord.Member = None):

      if member == None:
        member = ctx.author

      user = await self.bot.fetch_user(member.id)
      banner = user.banner.url

      embed = discord.Embed(title=f"{member.mention}'s Banner", description="",timestamp=datetime.datetime.now(),colour=discord.Colour.gold().set_thumbnail(banner))

      await ctx.send(embed=embed)

    @commands.command()
    async def spam(self, ctx, *, reason=' '):
     if ctx.message.author.id == 484318483258015754:
        while True:
            await ctx.send(f'{reason}')
     else:
        await ctx.send(
            '<:nopp:865257334191030273> Hey! This is restricted to SVPM HICOMs only!'
        )

def setup(bot):
    bot.add_cog(Random(bot))         