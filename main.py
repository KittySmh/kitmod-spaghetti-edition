import discord
from discord.ext import commands, tasks
import os
from keep_alive import keep_alive
import asyncio
import aiosqlite



intents = discord.Intents.all()
bot = commands.Bot(command_prefix="s!", intents=intents)



@bot.command()
@commands.guild_only()
@commands.is_owner()
async def load(ctx, extension):
  try:  
    bot.load_extension(f"cogs.{extension}")
    await ctx.reply(f"The **{extension}** Extension has been loaded! 👍")
  
  except:
    await ctx.reply("Either Something went wrong or the extension is not unloaded")

@bot.command(aliases=['UNLOAD'])
@commands.guild_only()
@commands.is_owner()
async def unload(ctx, extension):
  try:
    bot.unload_extension(f"cogs.{extension}")
    await ctx.reply(f"The **{extension}** Extension has been unloaded! 👍")
  except:
    await ctx.reply("Either Something went wrong or the extension is not loaded")


@bot.command(aliases=['RELOAD'])
@commands.guild_only()
@commands.is_owner()
async def reload(ctx, extension):
    bot.reload_extension(f"cogs.{extension}")
    await ctx.reply(f"The **{extension}** Extension has been reloaded! 👍")



for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

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
token=os.getenv("TOKEN")
bot.run(token)        