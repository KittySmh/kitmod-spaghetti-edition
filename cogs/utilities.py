import discord
from discord.ext import commands
import datetime
import random
import os
import asyncio

class Utilities(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(pass_context=True)
    @commands.has_permissions(manage_nicknames=True)
    async def Feditname(self, ctx, member: discord.Member, *, nick="Content Deleted"):
     embed = discord.Embed(title = "Nickname Edited", description = f"{ctx.author.mention} has edited {member.mention}'s user name from {member.name} to {nick}. ",timestamp=datetime.datetime.now(),colour=discord.Colour.gold())
     embed.set_thumbnail(url=ctx.author.display_avatar)
     channel1 = discord.utils.get(ctx.guild.text_channels, name="mod-logs")
     try: 
       await channel1.send(embed=embed)
       await member.edit(nick=nick)
       await ctx.send(f'Nickname has successfully been changed for {member.mention}')
     except:
       await ctx.send("Something went wrong while editing the user's profile name")
        
    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def tlock(self, ctx, duration=None):
     embed = discord.Embed(title = "Channel TimeLocked :lock:", description = f"{ctx.author.mention} has Timedlocked the channel named **{ctx.channel.mention}** for **{duration}**. ",timestamp=datetime.datetime.now(),colour=discord.Colour.gold())
     channel1 = discord.utils.get(ctx.guild.text_channels, name="mod-logs")
     embed.set_thumbnail(url=ctx.author.display_avatar) 
     if duration == None:
       await ctx.reply("State a time limit!")
       return
     else:   
      converter = {'s': 1, 'm': 60, 'h': 3600, 'd': 86400}
      locktime = int(duration[0]) * converter[duration[-1]]
      await ctx.channel.set_permissions(ctx.guild.default_role,send_messages=False)
      await ctx.send(ctx.channel.mention + f" Has Been **Locked** for {duration}. :lock: ")
      await channel1.send(embed=embed)
      await asyncio.sleep(locktime)
      await ctx.channel.set_permissions(ctx.guild.default_role,send_messages=True)
      await ctx.send(f"Timer **Completed**. {ctx.channel.mention} has been **Unlocked**. :unlock:")

 
    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def lock(self, ctx):
     embed = discord.Embed(title = "Channel Locked :lock:", description = f"{ctx.author.mention} has locked the channel named \n**{ctx.channel.mention}**. ",timestamp=datetime.datetime.now(),colour=discord.Colour.gold())
     embed.set_thumbnail(url=ctx.author.display_avatar)
     channel1 = discord.utils.get(ctx.guild.text_channels, name="mod-logs")
     await ctx.channel.set_permissions(ctx.guild.default_role,send_messages=False)
     await ctx.send(ctx.channel.mention + " Has Been **Locked** :lock: ")
     await channel1.send(embed=embed)


    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def unlock(self, ctx):
     embed = discord.Embed(title = "Channel Unlocked :unlock:", description = f"{ctx.author.mention} has unlocked the channel named \n**{ctx.channel.mention}**. ",timestamp=datetime.datetime.now(),colour=discord.Colour.gold())
     embed.set_thumbnail(url=ctx.author.display_avatar)
     channel1 = discord.utils.get(ctx.guild.text_channels, name="mod-logs")
     await ctx.channel.set_permissions(ctx.guild.default_role,send_messages=True)
     await ctx.send(ctx.channel.mention + " has been **Unlocked** :unlock:")
     await channel1.send(embed=embed)

    @commands.command(aliases=["pi"])
    async def whois(self, ctx, member: discord.Member = None):
     if not member:  # if member is no mentioned
       member = ctx.message.author  # set member as the author
     roles = [role for role in member.roles]
     embed = discord.Embed(colour=discord.Colour.gold(),timestamp=ctx.message.created_at,title=f"User Info - {member}")
     embed.set_thumbnail(url=member.display_avatar)
     embed.set_footer(text=f"Requested by {ctx.author}")

     embed.add_field(name="ID:", value=member.id, inline=False)
     embed.add_field(name="Display Name:",value=member.display_name,inline=False)

     embed.add_field(name="Created Account On:",value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"),inline=False)
     embed.add_field(name="Joined Server On:",value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"),inline=False)

     embed.add_field(name="Currently:", value=(member.status), inline=False)

     embed.add_field(name="Roles:", value="".join([role.mention for role in roles]),inline=False)
     embed.add_field(name="Highest Role:", value=member.top_role.mention)
     await ctx.send(embed=embed) 

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def role(self, ctx, member: discord.Member = None, role: discord.Role = None):
     embed = discord.Embed(title = "Role Given", description = f"{member.mention} has been given the role named **{role}**. ",timestamp=datetime.datetime.now(),colour=discord.Colour.gold())
     embed.set_thumbnail(url=member.display_avatar)
     channel1 = discord.utils.get(ctx.guild.text_channels, name="mod-logs")
     try:
       if member == ctx.message.author:
         await ctx.reply("You cannot assign roles to yourself.")
         return

       if member == None:
         await ctx.reply("You can't assign a role to nobody...")
         return 

       if role == None:
         await ctx.reply("Mention a role please!")
         return 

       await member.add_roles(role)
       await ctx.reply(f"The role ''**{role}**'' has been provided to the {member.mention}!")
       await channel1.send(embed=embed)
     except:
       await ctx.reply(f"Either {member.mention} already have that role or I don't have the sufficient permissions to provide the user with the role.")
       return


    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def derole(self, ctx, member: discord.Member = None, role: discord.Role = None):
     embed = discord.Embed(title = "Role Removed", description = f"{member.mention} has been removed from the role named **{role}**. ",timestamp=datetime.datetime.now(),colour=discord.Colour.orange())
     embed.set_thumbnail(url=member.display_avatar)
     channel1 = discord.utils.get(ctx.guild.text_channels, name="mod-logs")
     try:
       if member == ctx.message.author:
         await ctx.reply("You cannot assign roles to yourself.")
         return

       if member == None:
         await ctx.reply("You can't assign a role to nobody...")
         return 

       if role == None:
         await ctx.reply("Mention a role!")
         return 
      
       await member.remove_roles(role)
       await ctx.reply(f"{member.mention} has been demoted from the role ''**{role}**''!")
       await channel1.send(embed=embed)
     except:
       await ctx.reply(f"Either {member.mention} doesn't have that role or I don't have the sufficient permissions to remove the role from the mentioned user.")      


    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def slowmode(self, ctx, duration):
     converter = {'s': 1, 'm': 60, 'h': 3600, 'd': 86400}
     slowtime = int(duration[0]) * converter[duration[-1]]
     embed = discord.Embed(title = "Channel Edited (slowmode :alarm_clock:)", description = f"{ctx.author.mention} has edited the slowmode in {ctx.channel.mention} with a delay of {duration}. ",timestamp=datetime.datetime.now(),colour=discord.Colour.orange())
     embed.set_thumbnail(url=ctx.author.display_avatar)
     channel1 = discord.utils.get(ctx.guild.text_channels, name="mod-logs")
     try:
       await ctx.channel.edit(slowmode_delay=slowtime)
       await ctx.reply(f"Message Delay has been setted to {duration} :alarm_clock:")
       await channel1.send(embed=embed)
     except:
       await ctx.reply("I might not have the perms to do so, **OR** the slowmode has been setted.")

    @commands.command(aliases=["av"])
    async def avatar(self, ctx, member: discord.Member = None):
     if member == None:
        member = ctx.author

     icon_url = member.display_avatar

     avatarEmbed = discord.Embed(title=f"{member.name}\'s Avatar",colour=ctx.author.color)

     avatarEmbed.set_image(url=f"{icon_url}")

     avatarEmbed.timestamp = ctx.message.created_at
     avatarEmbed.set_footer(
        text="SPVM Systems 2021® All Rights Reserved.")

     await ctx.send(embed=avatarEmbed)
 
    @commands.command(aliases=['info'])
    async def serverinfo(self, ctx):
     owner = str(ctx.guild.owner)
     region = str(ctx.guild.region)
     guild_id = str(ctx.guild.id)
     memberCount = str(ctx.guild.member_count)
     icon = str(ctx.guild.icon_url)
     desc = ctx.guild.description

     embed = discord.Embed(title=ctx.guild.name + " Server Information",description=desc,colour=discord.Color.gold())
     embed.set_thumbnail(url=icon)
     embed.add_field(name="Precinct",value="Precinct 21 District",inline=False)
     embed.add_field(name="Owner", value=owner, inline=False)
     embed.add_field(name="Server ID", value=guild_id, inline=False)
     embed.add_field(name="Region", value=region, inline=False)
     embed.add_field(name="Member Count", value=memberCount, inline=False)
     embed.set_footer(text="SPVM Systems 2021® All Rights Reserved.")
     await ctx.reply(embed=embed)

def setup(bot):
    bot.add_cog(Utilities(bot))   