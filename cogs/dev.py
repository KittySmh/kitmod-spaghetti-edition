import discord
from discord.ext import commands
from discord.ext import commands
import asyncio
import traceback
import discord
import inspect
import textwrap
import importlib
from contextlib import redirect_stdout
import io
import os
import re
import sys
import copy
import time
import subprocess
from typing import Union, Optional
import asyncio
import aiosqlite
import datetime
import io
import datetime
from collections import Counter

class PerformanceMocker:
    """A mock object that can also be used in await expressions."""

    def __init__(self):
        self.loop = asyncio.get_event_loop()

    def permissions_for(self, obj):
        # Lie and say we don't have permissions to embed
        # This makes it so pagination sessions just abruptly end on __init__
        # Most checks based on permission have a bypass for the owner anyway
        # So this lie will not affect the actual command invocation.
        perms = discord.Permissions.all()
        perms.administrator = False
        perms.embed_links = False
        perms.add_reactions = False
        return perms

    def __getattr__(self, attr):
        return self

    def __call__(self, *args, **kwargs):
        return self

    def __repr__(self):
        return '<PerformanceMocker>'

    def __await__(self):
        future = self.loop.create_future()
        future.set_result(self)
        return future.__await__()

    async def __aenter__(self):
        return self

    async def __aexit__(self, *args):
        return self

    def __len__(self):
        return 0

    def __bool__(self):
        return False

class GlobalChannel(commands.Converter):
    async def convert(self, ctx, argument):
        try:
            return await commands.TextChannelConverter().convert(ctx, argument)
        except commands.BadArgument:
            # Not found... so fall back to ID + global lookup
            try:
                channel_id = int(argument, base=10)
            except ValueError:
                raise commands.BadArgument(f'Could not find a channel by ID {argument!r}.')
            else:
                channel = ctx.bot.get_channel(channel_id)
                if channel is None:
                    raise commands.BadArgument(f'Could not find a channel by ID {argument!r}.')
                return 

class dev(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_result = None
        self.sessions = set()

    @property
    def display_emoji(self) -> discord.PartialEmoji:
        return discord.PartialEmoji(name='stafftools', id=314348604095594498)

    async def run_process(self, command):
        try:
            process = await asyncio.create_subprocess_shell(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            result = await process.communicate()
        except NotImplementedError:
            process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            result = await self.bot.loop.run_in_executor(None, process.communicate)

        return [output.decode() for output in result]

    def cleanup_code(self, content):
        """Automatically removes code blocks from the code."""
        # remove ```py\n```
        if content.startswith('```') and content.endswith('```'):
            return '\n'.join(content.split('\n')[1:-1])

        # remove `foo`
        return content.strip('` \n')

    async def cog_check(self, ctx):
        return await self.bot.is_owner(ctx.author)

    def get_syntax_error(self, e):
        if e.text is None:
            return f'```py\n{e.__class__.__name__}: {e}\n```'
        return f'```py\n{e.text}{"^":>{e.offset}}\n{e.__class__.__name__}: {e}```'
    
    @commands.check
    def developer_check(ctx):
      dev = [484318483258015754]
      return ctx.author.id not in dev
      
    @commands.command(hidden=True)
    async def sh(self, ctx, *, command):
        """Runs a shell command."""
        from cogs.utils.paginator import TextPageSource, RoboPages

        async with ctx.typing():
            stdout, stderr = await self.run_process(command)

        if stderr:
            text = f'stdout:\n{stdout}\nstderr:\n{stderr}'
        else:
            text = stdout

        pages = RoboPages(TextPageSource(text), ctx=ctx)
        await pages.start()

    @commands.command(hidden=True)
    async def perf(self, ctx, *, command):
        """Checks the timing of a command, attempting to suppress HTTP and DB calls."""

        msg = copy.copy(ctx.message)
        msg.content = ctx.prefix + command

        new_ctx = await self.bot.get_context(msg, cls=type(ctx))
        new_ctx._db = PerformanceMocker()

        # Intercepts the Messageable interface a bit
        new_ctx._state = PerformanceMocker()
        new_ctx.channel = PerformanceMocker()

        if new_ctx.command is None:
            return await ctx.send('No command found')

        start = time.perf_counter()
        try:
            await new_ctx.command.invoke(new_ctx)
        except commands.CommandError:
            end = time.perf_counter()
            success = False
            try:
                await ctx.send(f'```py\n{traceback.format_exc()}\n```')
            except discord.HTTPException:
                pass
        else:
            end = time.perf_counter()
            success = True

        await ctx.send(f'Status: {ctx.tick(success)} Time: {(end - start) * 1000:.2f}ms')
      
    @commands.command(pass_context=True, hidden=True, name='eval')
    async def _eval(self, ctx, *, body: str):
        """Evaluates a code"""

        env = {
            'bot': self.bot,
            'ctx': ctx,
            'channel': ctx.channel,
            'author': ctx.author,
            'guild': ctx.guild,
            'message': ctx.message,
            '_': self._last_result
        }

        env.update(globals())

        body = self.cleanup_code(body)
        stdout = io.StringIO()

        to_compile = f'async def func():\n{textwrap.indent(body, "  ")}'

        try:
            exec(to_compile, env)
        except Exception as e:
              e3 = discord.Embed(title="ERROR Raised [E3]", description=f"** **\n** **\nError Log:\n```py\n{e.__class__.__name__}: {e}\n```")
              return await ctx.send(embed=e3)

        func = env['func']
        try:
            with redirect_stdout(stdout):
                ret = await func()
        except Exception as e:
            value = stdout.getvalue()
            errorembed = discord.Embed(title="ERROR Raised [E4]",description=f"\n** **\n**Error Log:**\n```py\n{value}{traceback.format_exc()}\n```")
            await ctx.send(embed=errorembed)
        else:
            value = stdout.getvalue()
            try:
                await ctx.message.add_reaction('\u2705')
            except:
                pass

            if ret is None:
                if value:
                    e1 = discord.Embed(title="Script Evaluation Success [S1]", description = f"** **\nScript has been runned with a success.\n** **\n** **\n**Output**:\n```py\n{value}\n```")
                    await ctx.send(embed=e1)
            else:
                self._last_result = ret
                e2 = discord.Embed(title="Script Evaluation [S2]", description = f"** **\nScript has been runned with a success.\n** **\n** **\n**Output**:\n```py\n{value}\n```")
                await ctx.send(embed=e2)  

    @commands.command()
    @commands.guild_only()
    async def devmute(self, ctx, member: discord.Member,*, reason = "No Reason Provided"):
     embed = discord.Embed(title = "User Muted [Developer Override]", description = f"{member.mention} has been muted for {reason}. ",timestamp=datetime.datetime.now(),colour=discord.Colour.red()).set_thumbnail(url=member.display_avatar).add_field(name="Moderator:", value=f"{ctx.author}", inline=True)
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
    async def devkick(self, ctx, member: discord.Member, *, reason='No Reason Provided.'):
     embed = discord.Embed(title = "User Kicked [Developer Override]", description = f"{member.mention} has been kicked for {reason}. ",timestamp=datetime.datetime.now(),colour=discord.Colour.red())
     embed.set_thumbnail(url=member.display_avatar)
     channel1 = discord.utils.get(ctx.guild.text_channels, name="mod-logs")
     embed.add_field(name="Moderator:", value=f"{ctx.author}", inline=True)
     if member.guild_permissions.kick_members:
      await ctx.reply("User had mod perms. I am unable to kick them.")
     else:
       try:
        await ctx.send(member.name +
        f' has been kicked from **{ctx.guild.name}** for ' + reason)
        await member.send(f'You Have been kicked from **{ctx.guild.name}** for ' + reason) 
        await member.kick(reason=reason)
        await channel1.send(embed=embed)
       except:
         await ctx.send('Unable to Notify in DMs.')
         await member.kick(reason=reason)
         await channel1.send(embed=embed)

    @commands.command(hidden=True)
    async def sudo(self, ctx, channel: Optional[GlobalChannel], who: Union[discord.Member, discord.User], *, command: str):
        """Run a command as another user optionally in another channel."""
        msg = copy.copy(ctx.message)
        channel = channel or ctx.channel
        msg.channel = channel
        msg.author = who
        msg.content = ctx.prefix + command
        new_ctx = await self.bot.get_context(msg, cls=type(ctx))
        new_ctx._db = ctx._db
        await self.bot.invoke(new_ctx)
    
    @commands.command(pass_context=True)
    async def devsoftban(self, ctx, user: discord.Member = None,*, reason = "No Reason Provided"):
     embed = discord.Embed(title = "User Softbanned [Developer Override]", description = f"{user.mention} has been softbanned. ",timestamp=datetime.datetime.now(),colour=discord.Colour.red())
     embed.set_thumbnail(url=user.display_avatar)
     embed.add_field(name="Moderator:", value=f"{ctx.author}", inline=True)
     embed.add_field(name="Reason", value=f"{reason}")
     channel1 = discord.utils.get(ctx.guild.text_channels, name="mod-logs")
     role = discord.utils.get(ctx.guild.roles, name="Override Perms")
     hidmod = discord.utils.get(ctx.guild.roles, name="Hidden Moderator")
     
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
          await user.send(f"You have been softbanned from {ctx.author.guild} for the Reason: {reason}.")
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
          await brr.edit(f"Their DMs Are Closed. Reason for softban: {reason}")
          await channel1.send(embed=embed)
          return
    
            


    
    @commands.command()
    async def devban(self, ctx, member,*,reason='No reason provided'):
      m = await self.bot.fetch_user(member)
      embed = discord.Embed(title = "User Banned [Developer Override]", description = f"{m.name} [{m.mention}] has been banned.",timestamp=datetime.datetime.now(),colour=discord.Colour.red())
      embed.set_thumbnail(url=m.avatar)
      embed.add_field(name="Moderator:", value=f"{ctx.author}", inline=True)
      embed.add_field(name="Reason:", value=f"{reason}", inline=True)
      channel1 = discord.utils.get(ctx.guild.text_channels, name="mod-logs")
      await ctx.send(m.name +f' [{m.mention}] has been banned from **{ctx.guild.name}**. Reason: ' +reason)
      await channel1.send(embed=embed)
      try:
         await m.send(f'You have been banned from **{ctx.guild.name}**. Reason: ' +reason)
         await ctx.guild.ban(m, reason=reason, delete_message_days=7)
      except:
         await ctx.send('Unable to Notify in DMs.')
         await ctx.guild.ban(m,reason=reason, delete_message_days=7)

    @commands.command()
    async def devtmute(self, ctx, member: discord.Member, duration = None,*, reason = "No Reason provided"):
     embed = discord.Embed(title = "User TimeMuted [Developer Override]", description = f"{member.mention} has been timemuted for {duration}. ",timestamp=datetime.datetime.now(),colour=discord.Colour.red())
     embed.set_thumbnail(url=member.display_avatar)
     embed.add_field(name="Moderator:", value=f"{ctx.author}", inline=True)
     embed.add_field(name="Reason",value=f"{reason}",inline=True)
     converter = {'s': 1, 'm': 60, 'h': 3600, 'd': 86400}
     mutetime = int(duration[0]) * converter[duration[-1]]
     channel1 = discord.utils.get(ctx.guild.text_channels, name="mod-logs")
     await ctx.send(f"{member.mention} has been placed on a timed hold for {duration}. Reason: {reason}.")
     muted_role = discord.utils.get(ctx.guild.roles, name="Muted")
     await member.add_roles(muted_role)
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
    async def devtban(self, ctx, member, duration = None,*,reason = "No reason provided"):
     m = await self.bot.fetch_user(member)
     embed = discord.Embed(title = "User TimeBanned [Developer Override]", description = f"{m.mention} [{m.name}] has been timebanned for {duration}. ",timestamp=datetime.datetime.now(),colour=discord.Colour.red())
     embed.set_thumbnail(url=m.avatar)
     embed.add_field(name="Moderator:", value=f"{ctx.author}", inline=True)
     embed.add_field(name="Reason",value=f"{reason}",inline=True)
     channel1 = discord.utils.get(ctx.guild.text_channels, name="mod-logs")
     converter = {'s': 1, 'm': 60, 'h': 3600, 'd': 86400}
     bantime = int(duration[0]) * converter[duration[-1]]

     await ctx.send(f"{m.mention} [{m.name}] has been placed on a timed ban for {duration}. Reason: {reason}.")
     await channel1.send(embed=embed)
     await ctx.guild.ban(m, reason=reason)
     await channel1.send(embed=embed)
     try: 
       await member.send(f"You have been placed on a timed ban in {ctx.guild.name} for {duration}.")
       await asyncio.sleep(bantime)
       await ctx.guild.unban(m)
       return
     except:
       await asyncio.sleep(bantime)
       await ctx.guild.unban(m)
       return   

  
    @commands.command()
    @commands.guild_only()
    async def devwarn(self, ctx, member:discord.Member, *, reason):
        channel1 = discord.utils.get(ctx.guild.text_channels, name="mod-logs")
        warndb = await aiosqlite.connect("warnData.db")
        try:    
            await warndb.execute('INSERT OR IGNORE INTO warningsData (guild_id, admin_id, user_id, reason) VALUES (?,?,?,?)', (ctx.guild.id, ctx.author.id, member.id, reason))
            await warndb.commit()
            emb = discord.Embed(title="Warning [Developer Override]",color=0xff0000)
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
        except:
          await ctx.reply("Something went wrong.")

   
    
def setup(bot):      
  bot.add_cog(dev(bot))