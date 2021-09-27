import discord
from discord.ext import commands
import datetime
import random
import os
import asyncio

class Giveaways(commands.Cog):
    def __init__(self, bot):
        self.bot = bot



    @commands.command()
    @commands.has_role("Giveawayy")
    async def gstart(self, ctx, mins: int, *, prize: str):
     embed = discord.Embed(title="Giveaway! :tada:",
     description=f"{prize}",color=ctx.author.color)

    

     embed.add_field(name="Ends In:", value=f"{mins} Seconds")

     my_msg = await ctx.send(embed=embed)
     await my_msg.add_reaction("🎉")
     poopy = await ctx.send('||@here|| Active Giveaway Going on! :tada:')
    
     await asyncio.sleep(mins)

     new_msg = await ctx.channel.fetch_message(my_msg.id)

     users = await new_msg.reactions[0].users().flatten()

     users.pop(users.index(self.bot.user))

     winner = random.choice(users)

     await ctx.send(f"Congratulations! {winner.mention} won {prize}! :tada:")
     await poopy.edit(content='The Giveaway Has Ended. Tune in Next Time For More Exciting Giveaways!')



    @commands.command()
    @commands.has_role("Giveawayy")
    async def greroll(self, ctx, channel: discord.TextChannel, id_: int):
     try:
        new_msg = await channel.fetch_message(id_)
     except:
        await ctx.send("The ID that was entered was incorrect, make sure you have entered the correct giveaway message ID.")
     users = await new_msg.reactions[0].users().flatten()
     users.pop(users.index(self.bot.user))

     winner = random.choice(users)

     await channel.send(f"Congratulations the new winner is: {winner.mention} for the recent giveaway! :tada:")


def setup(bot):
    bot.add_cog(Giveaways(bot))      