import discord
from discord.ext import commands
import datetime
import discord
from discord.ext import commands
import datetime
import random
import os
import asyncio
from covid import Covid
import pydantic
import requests

errmsg = [1, 2, 3, 4]

class covid(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def cksource(self, ctx):
       if ctx.author.id == 484318483258015754:
         while True:
           covid = Covid()
           await ctx.reply(f"Covid 19 Source: **{covid.source}**")
           return
       else:
         if random.choice(errmsg) == 1:
           await ctx.reply("Congrats! You have discovered a command that's useless to you! ||*sarcasm!*||") 
           return  
         elif random.choice(errmsg) == 2:
           await ctx.reply("Dude, you do know that this command is restricted to devs?")
           return
         elif random.choice(errmsg) == 3:
           await ctx.reply("ERROR: You Do Not Have Access To This Command. <:nopp:865257334191030273>")
           return 
         elif random.choice(errmsg) == 4:
           await ctx.reply("You Do not have permission to run the command: **cksource**")  
           return 

    @commands.command()
    async def gtalldata(self, ctx):
     if ctx.author.id == 484318483258015754:
       while True:
         covid = Covid()
         pipa = covid.get_data()
         await ctx.reply(f"{pipa}")
         return
     else:
         if random.choice(errmsg) == 1:
           await ctx.reply("Congrats! You have discovered a command that's useless to you! ||*sarcasm!*||") 
           return  
         elif random.choice(errmsg) == 2:
           await ctx.reply("Dude, you do know that this command is restricted to devs?")
           return
         elif random.choice(errmsg) == 3:
           await ctx.reply("ERROR: You Do Not Have Access To This Command. <:nopp:865257334191030273>")
           return 
         elif random.choice(errmsg) == 4:
           await ctx.reply("You Do not have permission to run the command: **gtalldata**")  
           return 

    @commands.command()
    async def gtallcountries(self, ctx):
      if ctx.author.id == 484318483258015754:
        while True:
          covid = Covid()
          countries = covid.list_countries()
          print(f"Countries ID/Excact Name: \n {countries}")  
          return
      else:
         if random.choice(errmsg) == 1:
           await ctx.reply("Congrats! You have discovered a command that's useless to you! ||*sarcasm!*||") 
           return  
         elif random.choice(errmsg) == 2:
           await ctx.reply("Dude, you do know that this command is restricted to devs?")
           return
         elif random.choice(errmsg) == 3:
           await ctx.reply("ERROR: You Do Not Have Access To This Command. <:nopp:865257334191030273>")
           return 
         elif random.choice(errmsg) == 4:
           await ctx.reply("You Do not have permission to run the command: **gtallcountries**")  
           return   

    @commands.command()
    async def stats(self, ctx,*, country):
      covid = Covid()
      cases = covid.get_status_by_country_name(country)
      await ctx.reply(cases)
      return

    @commands.command()
    async def totalstats(self,ctx):
      covid = Covid()
      active = covid.get_total_active_cases()
      confirmed = covid.get_total_confirmed_cases()
      deaths = covid.get_total_deaths()

      embed = discord.Embed(title="Total Cases Worldwide", description = "")
      embed.add_field(name="Active Cases:", value=active,inline=True)
      embed.add_field(name="Confirmed Cases:", value=confirmed,inline=True)
      embed.add_field(name="Total Deaths:", value=deaths,inline=True)  
      await ctx.send(embed=embed)
      return







def setup(bot):
  bot.add_cog(covid(bot))   