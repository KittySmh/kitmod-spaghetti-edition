import discord
from discord.ext import commands
import datetime
import discord
from discord.ext import commands
import datetime
import random
import os
import asyncio
from googletrans import Translator

class translate(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def translate(self, ctx, lang = None, *, thing = None):
     if lang == None:
       await ctx.send("Please mention a language to translate into.")
       return
       
     if thing == None:
       await ctx.send("Please state what would you like me to translate.")
       return
     
     translator = Translator()
     translations = translator.translate(thing, dest=lang)
     for translation in translations:
       embed = discord.Embed(title="Google Translate Results", description="")
       embed.add_field(name="Before", value=f"{translator.orgin}", inline=True)
       embed.add_field(name="After",value=f"{translator.text}", inline=True)
       await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(translate(bot))       
