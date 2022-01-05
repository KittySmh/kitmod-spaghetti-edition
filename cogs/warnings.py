import discord
from discord.ext import commands
import asyncio
import aiosqlite
import datetime

class warnings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(kick_members=True)
    async def warn(self, ctx, member:discord.Member, *, reason):
        role = discord.utils.get(ctx.guild.roles, name="Override Perms")
        hidmod = discord.utils.get(ctx.guild.roles, name="Moderation Supervisor || SHR")
        channel1 = discord.utils.get(ctx.guild.text_channels, name="mod-logs")
        warndb = await aiosqlite.connect("warnData.db")
        
        if member == ctx.author:
            await ctx.reply("Why are you trying to warn yourself....??")
            return
        
        elif hidmod in member.roles:
          while True:
            await ctx.reply("I am not allowed to warn this user.")
            return  

        elif member.guild_permissions.kick_members:
         await ctx.reply("User has mod perms. I am unable to warn them.")    
         return

        elif role in member.roles:
          while True:
             await ctx.reply("I am not allowed to warn this user.")
             return
        
        else:
            await warndb.execute('INSERT OR IGNORE INTO warningsData (guild_id, admin_id, user_id, reason) VALUES (?,?,?,?)', (ctx.guild.id, ctx.author.id, member.id, reason))
            await warndb.commit()
            emb = discord.Embed(title="Warning Added",color=0xff0000)
            emb.add_field(name='Moderator:',value=ctx.message.author.mention,inline=True)
            emb.add_field(name='User:',value=member.mention,inline=True)
            emb.set_thumbnail(url=member.display_avatar)
            emb.add_field(name='Reason:',value=reason,inline=False)
            await channel1.send(embed=emb)
            try:
              await member.send(embed=emb)
              await ctx.send(f"Warning added for {member.display_name}. Reason: {reason}. Moderator: {ctx.author.mention}. Status: **DMed**")
            except:
              await ctx.send(f"Warning added for {member.display_name}. Reason: {reason}. Moderator: {ctx.author.mention}. Status: **Not DMed**")  

    @commands.command()
    @commands.guild_only()
    @commands.has_role("Override Perms")
    async def clearwarns(self, ctx, member:discord.Member):
        channel1 = discord.utils.get(ctx.guild.text_channels, name="mod-logs")
        warndb = await aiosqlite.connect("warnData.db")
        if member == ctx.author:
            await ctx.send("Why are you trying to unwarn yourself........???")
            return
        else:
            await warndb.execute("DELETE FROM warningsData WHERE guild_id = ? AND user_id = ?", (ctx.guild.id, member.id))
            await warndb.commit()
            emb = discord.Embed(title="All Warnings Removed",color=0xff0000)
            emb.add_field(name='Moderator:',value=ctx.message.author.mention,inline=True)
            emb.add_field(name='User:',value=member.mention,inline=True)
            emb.set_thumbnail(url=member.display_avatar)
            await channel1.send(embed=emb)
            await ctx.send(f"All Warnings for **{member.display_name}** has been removed by {ctx.author.display_name}.")

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(kick_members=True)
    async def warnings(self, ctx, member:discord.Member):
        warndb = await aiosqlite.connect("warnData.db")
        index = 0
        embed=discord.Embed(title=f"Warnings {member.name}", description="", color=0x000000)
        embed.set_thumbnail(url=member.display_avatar)
        msg = await ctx.send(embed=embed)
        async with warndb.execute('SELECT admin_id, reason FROM warningsData WHERE guild_id = ? AND user_id = ?', (ctx.guild.id, member.id,)) as cursor:
            async for entry in cursor:
                index += 1
                admin_id, reason = entry
                admin_name = ctx.guild.get_member(admin_id)
                embed.description += f"Warn: {index} | Moderator: {admin_name.mention} | Reason: {reason}\n"
            await msg.edit(embed=embed)

def setup(bot):      
  bot.add_cog(warnings(bot))                