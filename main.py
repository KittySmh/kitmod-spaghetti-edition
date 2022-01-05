import discord
from discord.ext import commands
import os
from keep_alive import keep_alive
import asyncio
import requests
import aiosqlite
import random
from discord.ext import commands
from discord_together import DiscordTogether


intents = discord.Intents.default()
intents.members = True
intents.typing = True
intents.presences = True

bot = commands.Bot(command_prefix="s!", intents=intents)


token=os.getenv("TOKEN")
errmsg = [1, 2, 3, 4]

@bot.command()
async def load(ctx, extension):
  if ctx.author.id == 484318483258015754:
   while True:
     try:  
       bot.load_extension(f"cogs.{extension}")
       await ctx.reply(f"The **{extension}** Extension has been loaded! 👍")
       return
  
     except:
       await ctx.reply("Either Something went wrong or the extension is not unloaded")
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
      await ctx.reply("You Do not have permission to run the command: **load**")  
      return 

@bot.command(aliases=['UNLOAD'])
async def unload(ctx, extension):
  if ctx.author.id == 484318483258015754:
   while True:
    try:
     bot.unload_extension(f"cogs.{extension}")
     await ctx.reply(f"The **{extension}** Extension has been unloaded! 👍")
     return
    except:
     await ctx.reply("Either Something went wrong or the extension is not loaded")
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
      await ctx.reply("You Do not have permission to run the command: **unload**")
      return
    

@bot.command(aliases=['RELOAD'])
async def reload(ctx, extension):
  if ctx.author.id == 484318483258015754:
   while True: 
    try: 
     bot.reload_extension(f"cogs.{extension}")
     await ctx.reply(f"The **{extension}** Extension has been reloaded! 👍")
     return
    except:
      await ctx.reply("Something Went Wrong...")
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
      await ctx.reply("You Do not have permission to run the command: **reload**")    
      return



for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
      bot.load_extension(f'cogs.{filename[:-3]}')
      print(f"{filename[:-3]} Extension Loaded!")
        

async def warninit():
    await bot.wait_until_ready()
    warndb = await aiosqlite.connect("warnData.db")
    await warndb.execute("CREATE TABLE IF NOT EXISTS warningsData (guild_id int, admin_id int, user_id int, reason text)")
    await warndb.commit()

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')
    await bot.change_presence(activity=discord.Activity(
        type=discord.ActivityType.listening, name='SPVM Radio Comms!'))
        
 

keep_alive()
bot.loop.create_task(warninit())
bot.run(token)        