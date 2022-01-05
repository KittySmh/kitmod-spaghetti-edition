from discord.ext import commands
import discord
import json

class economy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    global amounts
    try:
        with open('amounts.json') as f:
            amounts = json.load(f)
    except FileNotFoundError:
        print("Could not load amounts.json")
        amounts = {}    

     

    @commands.command(aliases=["bal"])
    async def balance(self, ctx):
     id = str(ctx.message.author.id)
     if id in amounts:
       if ctx.author.id == 484318483258015754: 
         await ctx.reply("You have **{}$** in the bank 💰. Thanks for developing SPVM Systems!".format(amounts[id]))
       else:
         await ctx.reply("You have **{}$** in the bank 💰.".format(amounts[id]))  
     else:
        await ctx.reply("You do not have an account! Register for one by running `s!register`") 


    @commands.command()
    async def register(self, ctx):
     id = str(ctx.message.author.id)
     if id not in amounts:
        amounts[id] = 100
        await ctx.reply("You are now registered!")
        with open('amounts.json', 'w+') as f:
         json.dump(amounts, f) 
     else:
        await ctx.reply("You already have an account!")

    @commands.command()
    async def transfer(self, ctx, amount: int = None, other: discord.Member = None):
     primary_id = str(ctx.author.id)
     other_id = str(other.id)
     if primary_id not in amounts:
        await ctx.reply("You do not have an account! Register for one by running `s!register`")
     elif other_id not in amounts:
        await ctx.reply("The other party does not have an account.")
     elif amount == None:
       await ctx.reply("You did not mention an amount to transfer.")
     elif other == None:
       await ctx.reply("Please mention a user to transfer the money to.")
     elif amounts[primary_id] < amount:
        await ctx.reply("You cannot afford this transaction.")
     else:
        amounts[primary_id] -= amount
        amounts[other_id] += amount
        await ctx.reply("Transaction complete.")
     
     with open('amounts.json', 'w+') as f:
        json.dump(amounts, f) 

def setup(bot):
  bot.add_cog(economy(bot))   