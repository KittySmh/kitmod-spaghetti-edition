import discord
from discord.ext import commands
import datetime
import random
import os
from discord import Spotify
import asyncio
import requests



determine_flip = [1, 0]

class Random(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def verifyembed(self,ctx):
      embed = discord.Embed(title="Welcome to **GalaxyBlox_YT Community!!!**",description="By joining this server, you agree to the rules. \n** **\nRules can be found in __<#781115907644719104>__")
      dan = await ctx.send(embed=embed)
      await dan.add_reaction("✅")
      return

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
         else:
           if msg == None:
             g = discord.Embed(description="Do the command again. But **State What you would like to be sent** to the user!",color=discord.Colour.red()).set_author(name="ERROR", icon_url=str(ctx.author.display_avatar))
             c = await ctx.reply(embed=g)
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
               p = discord.Embed(description="I was unable to sent the message to the user. **Ensure that they have their DMs enabled for this server!**",color=discord.Colour.red()).set_author(name="ERROR", icon_url=str(ctx.author.display_avatar))
               a = await ctx.reply(embed=p) 
               await asyncio.sleep(30)
               await a.delete()
               await ctx.message.delete()
               return
       else:
         await ctx.reply("You Don't Have Access To This Command.",delete_after=10) 

    @commands.command()
    async def spotify(self, ctx, user: discord.Member = None):
     if user == None:
        user = ctx.author

     if user.activities:
        for activity in user.activities:
          if isinstance(activity, Spotify):
            while True:
                embed = discord.Embed(
                    title=
                    f"{user.name}'s Current Spotify Soundtrack  <:Spotifyyyy:866309114543865867>",
                    description="Listening to **{}**".format(activity.title),
                    color=activity.colour) 
                embed.set_thumbnail(url=activity.album_cover_url)
                embed.add_field(name="Artist", value=str(activity.artists),inline=True)
                embed.add_field(name="Album", value=activity.album,inline=True)
                embed.add_field(name="Spotify Party ID",value=f"||{activity.party_id}||",inline=True)
                embed.add_field(name="Listen Here!", value=activity.track_url,inline=False)
                embed.set_footer(text="Started listening to spotify on {} UTC".format(activity.created_at.strftime("%H:%M")))
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