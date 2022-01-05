import discord
from discord.ext import commands
import datetime
import random
import os
import asyncio
from discord import Spotify, Game

class whois(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 
 
 
    @commands.command(aliases=["devw"])
    @commands.is_owner()
    async def devwhois(self, ctx, user: discord.User = None):
     if not user:  # if member is no mentioned
       user = ctx.message.author  # set member as the author
     
     try:
       m = ctx.guild.get_member(user)
       embed = discord.Embed(colour=ctx.author.color,timestamp=ctx.message.created_at,title=f"{m.name}'s Information")
       #Author/Member avatar
       embed.set_thumbnail(url=m.display_avatar)
       #FooterShit
       embed.set_footer(text=f"Requested by {ctx.author}")
       #roles defining
       roles = [role for role in m.roles]
       #ID 
       embed.add_field(name="ID:", value=user.id, inline=False)
       #display username
       embed.add_field(name="Display Name:",value=m.display_name,inline=False)
       #Created Account ON
       embed.add_field(name="Created Account On:",value=m.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"),inline=False)
       #Joined server on
       embed.add_field(name="Joined Server On:",value=m.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"),inline=False)
       #Member Status
       if str(m.status) == "dnd":
         status = "Do Not Disturb <:dnd:894389291898273832>"
       elif str(m.status) == "idle":
         status = "Idle <:idle:894389291982139412>"
       elif str(m.status) == "online":
         status = "Online <:online:894389291986333777>"
       elif str(m.status) == "streaming":
         status = "Streaming <:streaming:894389292099575830>" 
       elif str(m.status) == "offline":
         status = "Offline <:offline:894389292107989082>"   
     
       embed.add_field(name="Currently:", value=f"{status}", inline=False)

       #Roles
       embed.add_field(name="Roles:", value="".join([role.mention for role in roles]),inline=False)
     
       #Highest Role
       embed.add_field(name="Highest Role:", value=m.top_role.mention)  
     
     except:
       m = await self.bot.fetch_user(user)
       embed=discord.Embed(title=m.name+"'s Information",description="User is not in the server",timestamp=ctx.message.created_at)
       embed.set_thumbnail(url=m.avatar)
       e = m.created_at.strftime("%b %d, %Y, %I:%M UTC")
       embed.add_field(name=f"General Information:", value=f"Mention: {m.mention}\nUsername: {m.name}\nAccount Created On: {e}")
       embed.set_footer(text=f"ID: {m.id}")
       await ctx.send(embed=embed)
    
     await ctx.send(embed=embed)    
     

     

     


     

     

def setup(bot):
    bot.add_cog(whois(bot))      