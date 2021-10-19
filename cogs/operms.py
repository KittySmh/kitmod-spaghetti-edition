import discord
from discord.ext import commands
import os
import asyncio
import datetime

class operms(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group()
    @commands.has_role("Override Perms")
    async def force(self, ctx):
     print(f"{ctx.author.name} has triggered the override cmd")

    @force.command()
    @commands.has_role("Override Perms")
    async def kick(self, ctx, member: discord.Member, *, reason='No Reason Provided.'):
     embed = discord.Embed(title = "User Force Kicked", description = f"{member.mention} has been forced kicked by {ctx.author.mention} for {reason}. ",timestamp=datetime.datetime.now(),colour=discord.Colour.red())
     embed.set_thumbnail(url=member.display_avatar)
     channel1 = discord.utils.get(ctx.guild.text_channels, name="mod-logs")
     try:
      ack = await ctx.reply("Overriding Evict Cmd...")
      await asyncio.sleep(2)
      await ack.edit(content="Evict Cmd Successfully Overriden, Evicting User.")
      await asyncio.sleep(1)
      await member.send(f"You have been force evicted from **{ctx.guild.name}** for {reason}")
      await member.kick()
      await channel1.send(embed=embed)
      await ack.edit(content=f"Member Successfully **Forced-Evicted** and **DM-ed** Reason:{reason}")
      await asyncio.sleep(10)
      await ack.delete()
     except:
       r = await ctx.reply("Overriding Evict Cmd...")
       await asyncio.sleep(2)
       await r.edit(content="Evict Cmd Successfully Overriden, Evicting User.")
       await asyncio.sleep(1)
       await member.kick()
       await r.edit(content=f"Member Successfully **Forced-Evicted**. **DMs Unavaliable.** Reason:{reason}")
       await channel1.send(embed=embed)
       await asyncio.sleep(10)
       await r.delete()

    @force.command()
    @commands.has_role("Override Perms")
    async def mute(self, ctx, member: discord.Member, *, reason='No Reason Provided.'):
     embed = discord.Embed(title = "User Force Muted", description = f"{member.mention} has been Force Muted for {reason}.",timestamp=datetime.datetime.now(),
     colour=discord.Colour.red())
     embed.set_thumbnail(url=member.display_avatar)
     channel1 = discord.utils.get(ctx.guild.text_channels, name="mod-logs")
     muted_role = discord.utils.get(ctx.guild.roles, name="Muted")
     ack = await ctx.reply("Overriding Hold(mute) Cmd...")
     await asyncio.sleep(2)
     await ack.edit(content="Hold Cmd Successfully Overriden, Force-Holding User.")
     await asyncio.sleep(1)
     await member.send(f"You have been forced onto Hold In **{ctx.guild.name}** for {reason}")
     await ack.edit(content=f"Member Successfully **Forced-Holded** and **DM-ed** Reason:{reason}")
     await member.add_roles(muted_role) 
     await channel1.send(embed=embed)
     await asyncio.sleep(10)
     await ack.delete()  

    @force.command()
    @commands.has_role("Override Perms")
    async def ban(self, ctx, member: discord.Member, *, reason='No Reason Provided.'):
     embed = discord.Embed(title = "User Force Banned", description = f"{member.mention} has been Force Banned for {reason}.",timestamp=datetime.datetime.now(),
     colour=discord.Colour.red())
     embed.set_thumbnail(url=member.display_avatar)
     channel1 = discord.utils.get(ctx.guild.text_channels, name="mod-logs")
     ack = await ctx.reply("Overriding Custody(Jail) Cmd...")
     await asyncio.sleep(2)
     await ack.edit(content="Jail Cmd Successfully Overriden, Evicting User.")
     await asyncio.sleep(1)
     await member.send(f"You have been force jailed from **{ctx.guild.name}** for {reason}")
     await member.ban()
     await ack.edit(content=f"Member Successfully **Forced-Jailed** and **DM-ed** Reason:{reason}")
     await channel1.send(embed=embed)
     await asyncio.sleep(10)
     await ack.delete()  

    @commands.command()
    @commands.has_role("Override Perms")
    async def invite(self, ctx):
     invite = await ctx.channel.create_invite(max_uses=1)     
     embed = discord.Embed(title = "Invite Created", description = f"{ctx.author.mention} has created an invite. ",timestamp=datetime.datetime.now(),colour=discord.Colour.gold())
     embed.set_thumbnail(url=ctx.author.display_avatar)
     embed.add_field(name="Link:",value=f"{invite}")
     channel1 = discord.utils.get(ctx.guild.text_channels, name="mod-logs")
     await ctx.send(f"Here's your **One-time Use Only** invite:")
     await ctx.send(f"{invite}")
     await channel1.send(embed=embed)
       

    @commands.command()
    @commands.has_role("Override Perms")
    async def rainbowvibes(self, ctx):
     bruh = await ctx.send("<a:RainbowParrot:852400732324888586>")
     await bruh.reply("Rainbow Vibes")

    @commands.command()
    @commands.has_role("Override Perms")
    async def pipa(self, ctx):
     await ctx.send("pipapapalapum pipapapalapum pipapapalapum pipapapalapum pipapapalapum pipapapalapum pipapapalapum pipapapalapum pipapapalapum pipapapalapum pipapapalapum pipapapalapum pipapapalapum pipapapalapum pipapapalapum pipapapalapum pipapapalapum pipapapalapum pipapapalapum pipapapalapum pipapapalapum pipapapalapum pipapapalapum pipapapalapum pipapapalapum pipapapalapum pipapapalapum pipapapalapum pipapapalapum pipapapalapum \n <a:RainbowParrot:852400732324888586> <a:RainbowParrot:852400732324888586> <a:RainbowParrot:852400732324888586> <a:RainbowParrot:852400732324888586>")
     return

    @commands.command()
    @commands.has_role("Override Perms")
    async def pampam(self, ctx):
     await ctx.send("papapalapum papapalapum papapalapum papapalapum papapalapum papapalapum papapalapum papapalapum papapalapum papapalapum papapalapum papapalapum papapalapum papapalapum papapalapum papapalapum papapalapum papapalapum papapalapum papapalapum papapalapum papapalapum papapalapum papapalapum papapalapum papapalapum papapalapum papapalapum papapalapum papapalapum papapalapum papapalapum papapalapum papapalapum papapalapum  \n <a:RainbowParrot:852400732324888586> <a:RainbowParrot:852400732324888586> <a:RainbowParrot:852400732324888586> <a:RainbowParrot:852400732324888586>")


def setup(bot):
    bot.add_cog(operms(bot))      