
from discord.ext import commands
import re
import datetime
import asyncio
import discord

time_regex = re.compile("(?:(\d{1,5})(h|s|m|d))+?")
time_dict = {"h": 3600, "s": 1, "m": 60, "d": 86400}


class TimeConverter(commands.Converter):
    async def convert(self, ctx, argument):
        args = argument.lower()
        matches = re.findall(time_regex, args)
        time = 0
        for key, value in matches:
            try:
                time += time_dict[value] * float(key)
            except KeyError:
                raise commands.BadArgument(
                    f"{value} is an invalid time key! h|m|s|d are valid arguments"
                )
            except ValueError:
                raise commands.BadArgument(f"{key} is not a number!")
        return round(time)

class Sinner(commands.Converter):
    async def convert(self, ctx, argument):
        argument = await commands.MemberConverter().convert(ctx, argument) # gets a member object
        permission = argument.guild.get_role(848916235869224970) # can change into any permission
        if not permission: # checks if user has the permission
            return argument # returns user object
        else:
            raise commands.BadArgument("You cannot punish other staff members") # tells user that target is a staff member



class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(kick_members=True)
    async def unmute(self, ctx, member: discord.Member,*, reason = "No Reason Provided"):
        embed = discord.Embed(title = "User Unmuted", description = f"{member.mention} has been unmuted for {reason}. ",timestamp=datetime.datetime.now(),colour=discord.Colour.red())
        embed.set_thumbnail(url=member.display_avatar)
        channel1 = discord.utils.get(ctx.guild.text_channels, name="mod-logs")
        embed.add_field(name="Moderator:", value=f"{ctx.author}", inline=True)
         
      
        role = discord.utils.get(ctx.guild.roles, name="Muted")
        if not role:
          await ctx.reply("No muted role was found! Please create one called `Muted`")
          return


        if role not in member.roles:
          await ctx.reply("This member is not muted.")
          return

        await member.remove_roles(role)
        await ctx.send(f"Unmuted `{member.display_name}` for {reason}.")
        await channel1.send(embed=embed)
        
        try:
         await member.send(f"You have been unmuted in {ctx.guild.name} for "+ reason)
        except:
          await ctx.send(f"Unable to notify {member.display_name} in DMs.") 

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(kick_members=True)
    async def mute(self, ctx, member: discord.Member,*, reason = "No Reason Provided"):
     embed = discord.Embed(title = "User Muted", description = f"{member.mention} has been timemuted for {reason}. ",timestamp=datetime.datetime.now(),colour=discord.Colour.red()).set_thumbnail(url=member.display_avatar).add_field(name="Moderator:", value=f"{ctx.author}", inline=True)
     channel1 = discord.utils.get(ctx.guild.text_channels, name="mod-logs") 
     if member.guild_permissions.kick_members:
        await ctx.reply("User has mod perms, I'm unable to mute them.") 
        return
     else: 
       role = discord.utils.get(ctx.guild.roles, name="Muted")
       if not role:
            await ctx.reply("No muted role was found! Please create one called `Muted`")
            return

       if role in member.roles:
            await ctx.reply("This member is muted.")
            return
        
       else: 
         await member.add_roles(role)
         await ctx.send(f"Muted `{member.display_name}` for {reason}.")
         await channel1.send(embed=embed)
       
         try:
           await member.send(f"You have been muted in {ctx.guild.name} for "+ reason)
         except:
           await ctx.send(f"Unable to notify {member.display_name} in DMs.") 



    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason='No Reason Provided.'):
     embed = discord.Embed(title = "User Kicked", description = f"{member.mention} has been kicked for {reason}. ",timestamp=datetime.datetime.now(),colour=discord.Colour.red())
     embed.set_thumbnail(url=member.display_avatar)
     channel1 = discord.utils.get(ctx.guild.text_channels, name="mod-logs")
     embed.add_field(name="Moderator:", value=f"{ctx.author}", inline=True)
     if member.guild_permissions.kick_members:
      await ctx.reply("User had mod perms. I am unable to kick them.")
     else:
       try:
        invite = await ctx.channel.create_invite(max_uses=1)
        await ctx.send(member.name +
        f' has been kicked from **{ctx.guild.name}** for ' + reason)
        await member.send(f'You Have been kicked from **{ctx.guild.name}** for ' + reason)
        await member.send(f"Here's your invite if you're willing to take the chance.")
        await member.send(f"**Invite:** {invite}")    
        await member.kick(reason=reason)
        await channel1.send(embed=embed)
       except:
         await ctx.send('Unable to Notify in DMs.')
         await member.kick(reason=reason)
         await channel1.send(embed=embed)




    @commands.command()
    @commands.guild_only()
    @commands.has_role('Override Perms')
    @commands.has_permissions(kick_members=True)
    async def unban(self, ctx, member: discord.Member, reason = "No Reason Provided"):
     embed = discord.Embed(title = "User Unbanned", description = f"{member.mention} has been unbanned for {reason}. ",timestamp=datetime.datetime.now(),colour=discord.Colour.red())
     embed.set_thumbnail(url=ctx.author.display_avatar)
     channel1 = discord.utils.get(ctx.guild.text_channels, name="mod-logs")
     embed.add_field(name="Moderator:", value=f"{ctx.author}", inline=True)
     user = await self.bot.fetch_user(member)
     await ctx.guild.unban(user)
     await channel1.send(embed=embed)
     await ctx.reply(f"{member.name} has been unbanned.")
    
    @commands.command(pass_context=True)
    @commands.has_permissions(kick_members=True)
    async def softban(self, ctx, user: discord.Member = None,*, reason = "No Reason Provided"):
     embed = discord.Embed(title = "User Softbanned", description = f"{user.mention} has been softbanned. ",timestamp=datetime.datetime.now(),colour=discord.Colour.red())
     embed.set_thumbnail(url=user.display_avatar)
     embed.add_field(name="Moderator:", value=f"{ctx.author}", inline=True)
     embed.add_field(name="Reason", value=f"{reason}")
     channel1 = discord.utils.get(ctx.guild.text_channels, name="mod-logs")
     role = discord.utils.get(ctx.guild.roles, name="Override Perms")
     hidmod = discord.utils.get(ctx.guild.roles, name="Hidden Moderator")
     inv = await ctx.channel.create_invite(max_uses=1)
     
     if user == None:
       await ctx.reply("Mention a user please!")
       return
    
     elif role in user.roles:
       while True:
         return

     elif hidmod in user.roles:
       while True:
         return

     try:
          await user.send(f"You have been softbanned from {ctx.author.guild} for the Reason: {reason}\nJoin again with this link: {inv}.")
          await ctx.guild.ban(user, reason=reason, delete_message_days=7)
          await asyncio.sleep(0.1)
          await ctx.guild.unban(user)
          await ctx.send(f"**{user.mention}** has been successfully softbanned for {reason}.")
          await channel1.send(embed=embed)
          return
     except:
          brr = await ctx.reply("Softbanning User...")
          await ctx.guild.ban(user, reason=reason, delete_message_days=7)
          await asyncio.sleep(0.1)
          await ctx.guild.unban(user)
          await brr.edit(f"Their DMs Are Closed. Looks like they won't be returning anytime soon. Reason for softban: {reason}")
          await channel1.send(embed=embed)
          return
    
            


    @commands.command()
    @commands.guild_only()
    @commands.has_role("Override Perms")
    async def purge(self, ctx, amount: int = 1):
        await ctx.message.delete()
        await ctx.channel.purge(limit=amount)
        e = await ctx.send(f" **{amount} messages were cleared!**")
        await asyncio.sleep(5)
        await e.delete()
    
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx,member: discord.Member,*,reason='No reason provided.'):
     embed = discord.Embed(title = "User TimeMuted", description = f"{member.mention} has been banned for {reason}. ",timestamp=datetime.datetime.now(),colour=discord.Colour.red())
     embed.set_thumbnail(url=member.display_avatar)
     embed.add_field(name="Moderator:", value=f"{ctx.author}", inline=True)
     channel1 = discord.utils.get(ctx.guild.text_channels, name="mod-logs")
     if member.guild_permissions.kick_members:
       await ctx.reply("User has mod perms. I am unable to ban them.")
     else:
       await ctx.send(member.name +f' has been banned from **{ctx.guild.name}**. Reason: ' +reason)
       await channel1.send(embed=embed)
       try:
         await member.send(f'You have been banned from **{ctx.guild.name}**. Reason: ' +reason)
         await member.ban(reason=reason, delete_message_days=7)
       except:
         await ctx.send('Unable to Notify in DMs.')
         await member.ban(reason=reason, delete_message_days=7)

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def tmute(self, ctx, member: discord.Member, duration = None):
     embed = discord.Embed(title = "User TimeMuted", description = f"{member.mention} has been timemuted for {duration}. ",timestamp=datetime.datetime.now(),colour=discord.Colour.red())
     embed.set_thumbnail(url=member.display_avatar)
     embed.add_field(name="Moderator:", value=f"{ctx.author}", inline=True)
     converter = {'s': 1, 'm': 60, 'h': 3600, 'd': 86400}
     mutetime = int(duration[0]) * converter[duration[-1]]
     channel1 = discord.utils.get(ctx.guild.text_channels, name="mod-logs")
     await ctx.send(f"{member.mention} has been placed on a timed hold for {duration}.")
     muted_role = discord.utils.get(ctx.guild.roles, name="Muted")
     await member.add_roles(muted_role)
     await ctx.send(f"{member.mention} has been successfully placed on a timed hold.")
     try: 
       await member.send(f"You have been placed on a timed hold in {ctx.guild.name} for {duration} seconds.")
       await channel1.send(embed=embed)
       await asyncio.sleep(mutetime)
       await member.remove_roles(muted_role)
       await ctx.send(f"{member.mention} has been removed from their timed hold.")
       await member.send(f"Timed hold in {ctx.guild.name} is now completed. You may speak as usual.")
       return
     except:
       await channel1.send(embed=embed)
       await asyncio.sleep(mutetime)
       await member.remove_roles(muted_role)
       await ctx.send(f"{member.mention} has been removed from their timed hold.")
       return

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def tban(self, ctx, member: discord.Member, duration = None):
     embed = discord.Embed(title = "User TimeBanned", description = f"{member.mention} has been timebanned for {duration}. ",timestamp=datetime.datetime.now(),colour=discord.Colour.red())
     embed.set_thumbnail(url=member.display_avatar)
     embed.add_field(name="Moderator:", value=f"{ctx.author}", inline=True)
     channel1 = discord.utils.get(ctx.guild.text_channels, name="mod-logs")
     converter = {'s': 1, 'm': 60, 'h': 3600, 'd': 86400}
     bantime = int(duration[0]) * converter[duration[-1]]

     await ctx.send(f"{member.mention} has been placed on a timed ban for {duration}.")
     await channel1.send(embed=embed)
     await member.ban()
     await ctx.send(f"{member.mention} has been successfully placed on a timed ban.")
     await channel1.send(embed=embed)
     try: 
       await member.send(f"You have been placed on a timed ban in {ctx.guild.name} for {duration}.")
       await asyncio.sleep(bantime)
       await ctx.send(f"{member.mention} has been removed from their timed ban.")
       return
     except:
       await asyncio.sleep(bantime)
       await ctx.send(f"{member.mention} has been removed from their timed ban.")
       return   

    

def setup(bot):
    bot.add_cog(Moderation(bot))    