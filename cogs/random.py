import discord
from discord.ext import commands
import datetime
import random
import os
from discord import Spotify
import asyncio
import requests
import re
from datetime import timedelta

determine_flip = [1, 0]


      
class Random(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    @commands.is_owner()
    async def verifyembed(self,ctx):
      embed = discord.Embed(title=f"Welcome to **{ctx.guild.name}**",description="By joining this server, you agree to the rules. \n** **\nRules can be found in __<#781115907644719104>__")
      dan = await ctx.send(embed=embed)
      await dan.add_reaction("✅")
      return
  
    @commands.command()
    async def rroles(self,ctx):
      embed = discord.Embed(title="⚔️ Reaction Roles ⚔️", description = "__Roles__\n• Pro Gamer = 🎮\n• Pro Music Producer = 🎵\n• Pro Editor = 💻\n• Pro Bedwars Player = 🛏️\n• GBYT Bedwars Clan = 👀")
      hoe = await ctx.send(embed=embed)
      await hoe.add_reaction("🎮")
      await hoe.add_reaction("🎵")
      await hoe.add_reaction("💻")
      await hoe.add_reaction("🛏️")
      await hoe.add_reaction("👀")
      
      await ctx.message.delete()
      await ctx.sennd(embed=embed)

    @commands.command()
    async def weather(self, ctx, *, city: str):
      
      api_key = "0aedee273cf0a3070c9410cc97353bdb"
      base_url = "http://api.openweathermap.org/data/2.5/weather?"
      
      city_name = city
      complete_url = base_url + "appid=" + api_key + "&q=" + city_name
      response = requests.get(complete_url)
      x = response.json()
      channel = ctx.message.channel
      if x["cod"] != "404":
        async with channel.typing():
           y = x["main"]
           current_temperature = y["temp"]
           current_temperature_celsiuis = str(round(current_temperature - 273.15))
           current_pressure = y["pressure"]
           current_humidity = y["humidity"]
           z = x["weather"]
           weather_description = z[0]["description"]
           weather_description = z[0]["description"]
           embed = discord.Embed(title=f"Weather in {city_name}",
           color=ctx.guild.me.top_role.color,timestamp=ctx.message.created_at,)
           embed.add_field(name="Descripition", value=f"**{weather_description}**", inline=False)
           embed.add_field(name="Temperature(C)", value=f"**{current_temperature_celsiuis}°C**", inline=False)
           embed.add_field(name="Humidity(%)", value=f"**{current_humidity}%**", inline=False)
           embed.add_field(name="Atmospheric Pressure(hPa)", value=f"**{current_pressure}hPa**", inline=False)
           embed.set_thumbnail(url="https://i.ibb.co/CMrsxdX/weather.png")
           embed.set_footer(text=f"Requested by {ctx.author.name}")   
           await channel.send(embed=embed)
      else:
        await channel.send("ERROR: City not found.")
 



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
    
    @commands.command(aliases=["gping"])
    async def ghostpong(self, ctx,*,member:discord.Member):
      if ctx.message.author.id == 484318483258015754:
        while True:
          await ctx.message.delete()
          beanz = await ctx.send(f"{member.mention}")
          await beanz.delete()
          return
      
      else:
        await ctx.reply("ERROR: Access Denied.")    


    @commands.command()
    async def petition(self, ctx,*,pet):
      if ctx.message.author.id == 484318483258015754:
        while True:
          embed= discord.Embed(title="Petition", description=f"{pet}", colour = ctx.author.color)
          embed.set_thumbnail(url=ctx.author.display_avatar)
          yes = "<:yass:865257334023782400>"
          no = "<:nopp:865257334191030273>" 
          maybe = "<:MaybeJustMAYBE:869425979385327637>"

          await ctx.message.delete()
          pipa = await ctx.send(embed=embed)
          await pipa.add_reaction(yes)
          await pipa.add_reaction(maybe)
          await pipa.add_reaction(no)
          await ctx.send(f"New Petition Made By Moderator: **{ctx.author.display_name}**.")
          return

      else:
        await ctx.reply("ERROR: Access Denied.")
 


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
           z = discord.Embed(description="Please **Mention** a user!",color=discord.Colour.red()).set_author(name="ERROR", icon_url=str(ctx.author.display_avatar))
           d = await ctx.reply(embed=z)
           await asyncio.sleep(30)
           await d.delete()
           await ctx.message.delete()
           return
          
         elif msg == None:
             g = discord.Embed(description="Do the command again. But **State What you would like to be sent** to the user!",color=discord.Colour.red()).set_author(name="ERROR", icon_url=str(ctx.author.display_avatar))
             c = await ctx.reply(embed=g)
             await asyncio.sleep(30)
             await c.delete()
             await ctx.message.delete()
             return
         else:
             try:
               await member.send(msg) 
               t = discord.Embed(description="Message **Successfully Sent**!",color=discord.Colour.green()).set_author(name="SUCCESS", icon_url=str(ctx.author.display_avatar))
               t.add_field(title="Message Content", value=msg)
               b = await ctx.send(embed=t)
               await asyncio.sleep(30)
               await b.delete()
               await ctx.message.delete()
               return
             except:
               p = discord.Embed(description="I was unable to sent the message to the user. **Ensure that they have their DMs enabled for this server!**",color=discord.Colour.red()).set_author(name="ERROR", icon_url=str(ctx.author.display_avatar))
               a = await ctx.reply(embed=p) 
               await asyncio.sleep(30)
               await a.delete()
               await ctx.message.delete()
               return
     else:
        await ctx.reply("You don't have access to this command.",delete_after=10) 
    
    @commands.command()
    async def spotify(self, ctx, user: discord.Member=None):
     user = user if user else ctx.author

     activity = None

     for act in user.activities:
      if isinstance(act, Spotify):
        activity = act
        break
      
     if activity:
      embed = discord.Embed(
        title=f"{user.name}'s Spotify Details <:logo:904559253317091360>",
        description="Currently listening to **{}**".format(activity.title),
        color=activity.color
      )

      embed.set_thumbnail(url=activity.album_cover_url)
      artist = str(activity.artists)
      splitartist = artist.replace("[","").replace("]","").replace("'","").replace("'","")
      embed.add_field(
        name="Artist", 
        value=splitartist,
        inline=False
      )

      embed.add_field(
        name="Album", 
        value=activity.album,
        inline=False
      )
      
      m1, s1 = divmod(int(activity.duration.seconds), 60)

      song_length = f'{m1}:{s1}'

      embed.add_field(
        name="Song Duration",
        value=song_length,
        inline=True
      )                   
      embed.add_field(
        name="Track Link", 
        value=f"[{activity.title}](https://open.spotify.com/track/{activity.track_id})",
        inline=True
      )

      embed.set_footer(text=f'Requested by: {ctx.author}', icon_url=ctx.author.display_avatar)
      
      await ctx.send(embed=embed)

     else:
      await ctx.send(f'{user.name} is not listening to spotify currently.')

    @commands.command()
    async def comms(self, ctx):
     await ctx.reply(
        f'**SVPM Radio Comms Latency** = {round(self.bot.latency * 1000)} ms')
    
    @commands.command()
    async def banner(self,ctx,member = None):

      if member == None:
        member = ctx.author.id

      user = await self.bot.fetch_user(member)
      banner = user.banner.url

      embed = discord.Embed(title=f"{user.name}'s Banner", description="",timestamp=datetime.datetime.now())
      embed.set_footer(text="Requested by "+ ctx.author.name)
      embed.set_image(url=banner)

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