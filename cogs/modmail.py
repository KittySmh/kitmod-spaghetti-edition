import typing
import traceback
import asyncio
import discord
from discord.ext import commands

class modmail(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    

    @commands.command()
    async def modmail(self, ctx):
     
     sent_users = []
     
     if ctx.guild: # ensure the channel is a DM
        return

     if ctx.author == self.bot.user:
        return

     if ctx.author.id in sent_users: # Ensure the intial message hasn't been sent before
        return

     modmail_channel = self.bot.get_channel(917029987675160647)
     

     

     embed = discord.Embed(color=0x00FFFF)
     embed.set_author(name=f"KitGang Modmail BETA", icon_url="https://cdn.discordapp.com/icons/690937143522099220/34fbd058360c3d4696848592ff1c5191.webp?size=1024")
     embed.add_field(name='Report a member:', value=f"React with 1️⃣ if you want to report a member.")
     embed.add_field(name='Report a Staff Member:', value=f"React with 2️⃣ if you want to report a Staff Member.")
     embed.add_field(name='Warn Appeal:', value=f"React with 3️⃣ if you would like to appeal a warning.")
     embed.add_field(name='Question:', value=f"React with 4️⃣ if you have a general question about the server.")
     embed.set_footer(text="Abuse of this syetem will result in moderation actions | KitGang Systems 2022® All Rights Reserved.")
     msg = await ctx.author.send(embed=embed)
     await msg.add_reaction("1️⃣")
     await msg.add_reaction("2️⃣")
     await msg.add_reaction("3️⃣")
     await msg.add_reaction("4️⃣")

     sent_users.append(ctx.author.id) # add this user to the list of sent users

     try:
        def check(reaction, user):
            return user == ctx.message.author and str(reaction.emoji) in ["1️⃣", "2️⃣", "3️⃣", "4️⃣"]

        reaction, user = await self.bot.wait_for("reaction_add", timeout=60, check=check)

        if str(reaction.emoji) == "1️⃣":
            embed = discord.Embed(color=0x00FFFF)
            embed.set_author(name=f"KitGang Modmail BETA", icon_url="https://media.discordapp.net/attachments/863776301436502037/917031076080275516/unknown.png")
            embed.add_field(name='How to Report:', value="Send the ID of the person you are reporting and attach add a screen shot of them breaking a rule (can be ToS or a server rule).")
            embed.set_footer(text="KitGang Systems | [1] Report a member")
            await ctx.author.send(embed=embed)

            message = await self.bot.wait_for("message", timeout=60, check=lambda m: m.channel == message.channel and m.author == message.author)
            membed = discord.Embed(title=f"Member Report | Medium Priority", description = f"Report Details: **{message.content}**", color=0x00FFFF)
            await modmail_channel.send(embed=membed)

        if str(reaction.emoji) == "2️⃣":
            embed = discord.Embed(color=0xFF7400)
            embed.set_author(name=f"KitGang Modmail BETA", icon_url="https://media.discordapp.net/attachments/863776301436502037/917031076080275516/unknown.png")
            embed.add_field(name='How to Report:', value="Send the ID of the staff you are reporting and attach add a screen shot of them breaking a rule (can be ToS or a server rule).")
            embed.set_footer(text="KitGang Systems | [2] Report a STAFF member")
            await message.author.send(embed=embed)

            message = await self.bot.wait_for("message", timeout=60, check=lambda m: m.channel == message.channel and m.author == message.author)
            embed = discord.Embed(title=f"Staff Member Report | High Priority", description = f"Report Details: **{message.content}**", color=0xFF7400)
            await modmail_channel.send(embed=embed)

        if str(reaction.emoji) == "3️⃣":
            embed = discord.Embed(color=0xFFF745)
            embed.set_author(name=f"KitGang Modmail BETA", icon_url="https://media.discordapp.net/attachments/863776301436502037/917031076080275516/unknown.png")
            embed.add_field(name='How to Appeal:', value="__**Appeal Format**__:\nUsername:\nID:\nWarnings Number:\nReason of the Warn:\nWhy would you want to appeal it:")
            embed.set_footer(text="KitGang Systems | [3] Appeal a Warning")
            await message.author.send(embed=embed)

            message = await self.bot.wait_for("message", timeout=60, check=lambda m: m.channel == message.channel and m.author == message.author)
            embed = discord.Embed(title=f"Warning Appeal | Low Priority", description = f"Appeal: **{message.content}**", color=0xFFF745)
            await modmail_channel.send(embed=embed)

        if str(reaction.emoji) == "4️⃣":
            embed = discord.Embed(color=0xFF6EF4)
            embed.set_author(name=f"KitGang Modmail BETA", icon_url="https://media.discordapp.net/attachments/863776301436502037/917031076080275516/unknown.png")
            embed.add_field(name='General Question:', value="Simply ask the question you'd like to know the answer of the server here! ")
            embed.set_footer(text="KitGang Systems | [4] General Question")
            await message.author.send(embed=embed)

            message = await self.bot.wait_for("message", timeout=60, check=lambda m: m.channel == message.channel and m.author == message.author)
            embed = discord.Embed(title=f"General Question | Low Priority", description=f"Question: **{message.content}**", color=0xFF6EF4)
            await modmail_channel.send(embed=embed)            


     except asyncio.TimeoutError:
        await message.delete()

def setup(bot):
    bot.add_cog(modmail(bot))            