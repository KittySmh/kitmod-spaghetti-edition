import discord
from discord.ext import commands
import datetime


class Helpcmd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot.remove_command("help")


    @commands.group()
    async def help(self, ctx):
      help = discord.Embed(
        title='SPVM Public Assistance Office',
        description=
        'Welcome to the SPVM Public Assist. Office. We are here to try and help you as much as possible!',
        timestamp=datetime.datetime.now(),
        colour=discord.Colour.gold()
      ).add_field(
        name='Miscellaneous',
        value="Displays the Miscellaneous Commands Category!\n`Usage= s!help miscellaneous `",
        inline=False
      ).add_field(
        name='Utilities',
        value="Displays the Utilities Commands Category\n`Usage= s!help utilities `",
        inline=False
      ).add_field(
        name='Moderation',
        value="Displays the Moderation Commands Category.\n`Usage= s!help moderation `",
        inline=False
      ).set_footer(
        text="SPVM Systems 2021® All Rights Reserved."

      ).set_thumbnail(
        url=
        'https://media.discordapp.net/attachments/835359268432773133/863792001065811978/SVPM_Logo_2.jpg?width=415&height=468')

      await ctx.send(embed=help)
   


    @help.command()
    async def utilities(self, ctx):
     page1 = discord.Embed(
        title='SPVM Utilities Office | **Section 1**',
        description=
        'Welcome to the SPVM Utilities Office. We will try to help you as much as possible!',
        timestamp=datetime.datetime.now(),
        colour=discord.Colour.gold()
     ).add_field(
        name='disregard',
        value='Disregards a few messages based on how much you inputed(purge)!\n`Usage= s!disregard{amount}`',
        inline=False
     ).add_field(
        name='slowmode',
        value='Adds slowmode to a certain channel (seconds)!\n`Usage= s!slowmode {seconds} `',
        inline=False
     ).add_field(
        name='lock',
        value="Locks a channel you're in!\n`Usage= s!lock `",
        inline=False
     ).add_field(
        name='unlock',
        value="Unlocks a locked channel.\n`Usage= s!unlock `",
        inline=False
     ).set_footer(
        text="SPVM Systems 2021® All Rights Reserved."

     ).set_thumbnail(
        url=
        'https://media.discordapp.net/attachments/835359268432773133/863792001065811978/SVPM_Logo_2.jpg?width=415&height=468'
     )
     page2 = discord.Embed(
        title='SPVM Utilities Office | **Section 2**',
        description=
        'Welcome to the SPVM Utilities Office. We will try to help you as much as possible!',
        timestamp=datetime.datetime.now(),
        colour=discord.Colour.gold()
     ).add_field(
        name='profileinfo',
        value="Check a user's profile information!\n.`Usage= s!profileinfo/s!pi {user}`",
        inline=False
     ).add_field(
        name='avatar',
        value="Gets the avatar of a selected user.\n`Usage= s!avatar/s!av {user}`",
        inline=False
     ).add_field(
        name='serverinfo',
        value="Displays the Information of this Server.\n`Usage= s!serverinfo`",
        inline=False
     ).set_footer(
        text="SPVM Systems 2021® All Rights Reserved."
 
     ).set_thumbnail(
        url=
        'https://media.discordapp.net/attachments/835359268432773133/863792001065811978/SVPM_Logo_2.jpg?width=415&height=468'
     )
     page3 = discord.Embed(
        title='SVPM Utilities Office | **Section 3**',
        description=
        'Welcome to the SPVM Utilities Office. We will try to help you as much as possible!',
        timestamp=datetime.datetime.now(),
        colour=discord.Colour.gold()
     ).add_field(
        name='role',
        value="Provides the user with the given role.\n`Usage= s!role {user} {role}`",
        inline=False
     ).add_field(
        name='derole',
        value="Remove a role from a mentioned user.\n`Usage= s!derole {user} {role}`",
        inline=False
     ).set_footer(
        text="SPVM Systems 2021® All Rights Reserved."
    
     ).set_thumbnail(
        url=
        'https://media.discordapp.net/attachments/835359268432773133/863792001065811978/SVPM_Logo_2.jpg?width=415&height=468'
     )

     pages = [page1, page2, page3]

     message = await ctx.send(embed=page1)
     await message.add_reaction('⏮')
     await message.add_reaction('◀')
     await message.add_reaction('▶')
     await message.add_reaction('⏭')

     def check(reaction, user):
        return user == ctx.author

     i = 0
     reaction = None

     while True:
        if str(reaction) == '⏮':
            i = 0
            await message.edit(embed=pages[i])
        elif str(reaction) == '◀':
            if i > 0:
                i -= 1
                await message.edit(embed=pages[i])
        elif str(reaction) == '▶':
            if i < 2:
                i += 1
                await message.edit(embed=pages[i])
        elif str(reaction) == '⏭':
            i = 2
            await message.edit(embed=pages[i])

        try:
            reaction, user = await self.bot.wait_for('reaction_add',
                                                   timeout=30.0,
                                                   check=check)
            await message.remove_reaction(reaction, user)
        except:
            break

     await message.clear_reactions()
     await message.delete()



    @help.command()
    async def miscellaneous(self, ctx):
     pagea = discord.Embed(
        title='SPVM Miscellaneous Office | **Section 1**',
        description=
        'Welcome to the SPVM Miscellaneous Office. We will try to help you as much as possible!',
        timestamp=datetime.datetime.now(),
        colour=discord.Colour.gold()
     ).add_field(
        name='comms',
        value="Displays the latency of the comms (ping).\n`Usage= s!comms`",
        inline=False
     ).add_field(
        name='Feditname',
        value=
        "Force Edits a User's Nickname in a server. It's defaulted to **Content Deleted**.  \n`Usage= s!Feditname {name}`",
        inline=False
     ).add_field(
        name='spotify [BUGGY, UNDER DEV]',
        value=
        "Displays what a user is currently listening to on Spotify.\n`Usage= s!spotify {user/or none}`",
        inline=False
     ).set_footer(
        text="SPVM Systems 2021® All Rights Reserved."
     ).set_image(
        url=
        'https://images-ext-2.discordapp.net/external/c1XNaTolANnIrRcBh02ISuA9aagzwF-rdFxWn7sa_QA/https/media.discordapp.net/attachments/835359268432773133/863792002431582218/SPVM_Logo.png'
     ).set_thumbnail(
        url=
        'https://media.discordapp.net/attachments/835359268432773133/863792001065811978/SVPM_Logo_2.jpg?width=415&height=468'
     )
     pageb = discord.Embed(
        title='SPVM Miscellaneous Office | **Section 2**',
        description=
        'Welcome to the SPVM Miscellaneous Office. We will try to help you as much as possible!',
        colour=discord.Colour.gold(),
        timestamp=datetime.datetime.now()
     ).add_field(
        name='guessnum',
        value=
        "Broken. Please bear with us till our team fixes it.",
        inline=False
     ).add_field(
        name='coinflip',
        value=
        "Flips a virtual coin!\n`Usage= s!coinflip`",
        inline=False
     ).add_field(
        name='meme',
        value=
        "Displays a current variety of memes.\n`Usage= s!meme`",
        inline=False
     ).set_footer(
        text="SPVM Systems 2021® All Rights Reserved."
   
     ).set_thumbnail(
        url=
        'https://media.discordapp.net/attachments/835359268432773133/863792001065811978/SVPM_Logo_2.jpg?width=415&height=468'
     )
     pagec = discord.Embed(
        title='SPVM Miscellaneous Office | **Section 3**',
        description=
        'Welcome to the SPVM Miscellaneous Office. We will try to help you as much as possible!',
        colour=discord.Colour.gold(),
        timestamp=datetime.datetime.now()
     ).add_field(
        name='UNAVALIABLE',
        value=
        "Sit tight with us while we develop more commands to help your server!",
        inline=False
     ).add_field(
        name='UNAVALIABLE',
        value=
        "Sit tight with us while we develop more commands to help your server!",
        inline=False
     ).add_field(
        name='UNAVALIABLE',
        value=
        "Sit tight with us while we develop more commands to help your server!",
        inline=False
     ).set_footer(
        text="SPVM Systems 2021® All Rights Reserved."
    
     ).set_thumbnail(
        url=
        'https://media.discordapp.net/attachments/835359268432773133/863792001065811978/SVPM_Logo_2.jpg?width=415&height=468'
     )

     pages = [pagea, pageb, pagec]

     message = await ctx.send(embed=pagea)
     await message.add_reaction('⏮')
     await message.add_reaction('◀')
     await message.add_reaction('▶')
     await message.add_reaction('⏭')

     def check(reaction, user):
        return user == ctx.author

     i = 0
     reaction = None

     while True:
        if str(reaction) == '⏮':
            i = 0
            await message.edit(embed=pages[i])
        elif str(reaction) == '◀':
            if i > 0:
                i -= 1
                await message.edit(embed=pages[i])
        elif str(reaction) == '▶':
            if i < 2:
                i += 1
                await message.edit(embed=pages[i])
        elif str(reaction) == '⏭':
            i = 2
            await message.edit(embed=pages[i])

        try:
            reaction, user = await self.bot.wait_for('reaction_add',
                                                   timeout=30.0,
                                                   check=check)
            await message.remove_reaction(reaction, user)
        except:
            break

     await message.clear_reactions()
     await message.delete()


    @help.command()
    async def moderation(self, ctx):
     page1 = discord.Embed(
        title='SPVM Moderation Help Division | **Section 1**',
        description=
        'Welcome to the SPVM Mod help Division. We will try to help you as much as possible!',
        timestamp=datetime.datetime.now(),
        colour=discord.Colour.gold()
     ).add_field(
        name='unmute',
        value="Unmute a muted user.\n`Usage= s!unmute {user} [Reason]`",
        inline=False
     ).add_field(
        name='mute',
        value="Mutes a user to prevent all sorts of trouble.\n`Usage= s!mute {user} [Reason]`",
        inline=False
     ).add_field(
        name='kick',
        value='Kick someone from this server.\n`Usage= s!kick {user} [Reason]`',
        inline=False
     ).set_footer(
        text="SPVM Systems 2021® All Rights Reserved."
   
     ).set_thumbnail(
        url=
        'https://media.discordapp.net/attachments/835359268432773133/863792001065811978/SVPM_Logo_2.jpg?width=415&height=468'
     )
     page2 = discord.Embed(
        title='SPVM Moderation Help Division | **Section 2**',
        description=
        'Welcome to the SPVM Mod help Division. We will try to help you as much as possible!',
        timestamp=datetime.datetime.now(),
        colour=discord.Colour.gold()
     ).add_field(
        name='issuewarrant [BROKEN]',
        value="Issues a warrant on a selected user. (Warn)\n`Usage:s!issuewarrant {user}`",
        inline=False
     ).add_field(
        name='warrants [BROKEN]',
        value=
        "Check a certain user's warrants. (check for the warnings basically)\n`Usage: s!warrants {user}`",
        inline=False
     ).set_footer(
        text="SPVM Systems 2021® All Rights Reserved."
    
     ).set_thumbnail(
        url=
        'https://media.discordapp.net/attachments/835359268432773133/863792001065811978/SVPM_Logo_2.jpg?width=415&height=468'
     )
     page3 = discord.Embed(
        title='SPVM Moderation Help Division | **Section 3**',
        description=
        'Welcome to the SPVM Mod help Division. We will try to help you as much as possible!',
        timestamp=datetime.datetime.now(),
        colour=discord.Colour.gold()
     ).add_field(
        name='ban',
        value="Bans someone from the server.\n`Usage= s!ban {user} [Reason]`",
        inline=False
     ).add_field(
        name='unban',
        value='Unban someone from the server. \nUsage: s!unban {user} [reason]',
        inline=False
     ).set_footer(
        text="SPVM Systems 2021® All Rights Reserved."
   
     ).set_thumbnail(
        url=
        'https://media.discordapp.net/attachments/835359268432773133/863792001065811978/SVPM_Logo_2.jpg?width=415&height=468'
     )

     pages = [page1, page2, page3]

     message = await ctx.send(embed=page1)
     await message.add_reaction('⏮')
     await message.add_reaction('◀')
     await message.add_reaction('▶')
     await message.add_reaction('⏭')

     def check(reaction, user):
        return user == ctx.author

     i = 0
     reaction = None

     while True:
        if str(reaction) == '⏮':
            i = 0
            await message.edit(embed=pages[i])
        elif str(reaction) == '◀':
            if i > 0:
                i -= 1
                await message.edit(embed=pages[i])
        elif str(reaction) == '▶':
            if i < 2:
                i += 1
                await message.edit(embed=pages[i])
        elif str(reaction) == '⏭':
            i = 2
            await message.edit(embed=pages[i])

        try:
            reaction, user = await self.bot.wait_for('reaction_add',
                                                   timeout=30.0,
                                                   check=check)
            await message.remove_reaction(reaction, user)
        except:
            break

     await message.clear_reactions()
     await message.delete()


def setup(bot):
    bot.add_cog(Helpcmd(bot))    