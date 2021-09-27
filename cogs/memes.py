import discord
from discord.ext import commands
import datetime
import praw
import random

reddit = praw.Reddit(client_id='-8HslMDM7ekiSuZfqe1-bQ',client_secret='ItBzxk6daL3UaC_iJBc2HPhImkDt4Q',user_agent='u/Technical_Sherbert65')

class Memes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    


    @commands.group()
    async def meme(self, ctx):
     memecheck = discord.Embed(title = "Looking For Some Memes???",
     description = "Use the command `s!meme memes` for the memes in the SubReddit r/Memes or `s!meme jack` for memes in the SubReddit r/Jacksucksatlife!",
     colour=discord.Color.gold(),
     timestamp=datetime.datetime.now()).set_footer(
            text="Memes4Life! $$$")
  

     await ctx.send(embed=memecheck)

    @meme.command()
    async def memes(self, ctx):
     jacky = await ctx.send("Please Hold On! I'm getting some of the Juicy Memes from the Memes SubReddit!")

     subreddit = reddit.subreddit("memes")
     all_subs = []

     top = subreddit.top(limit=50)

     for submission in top:
       all_subs.append(submission)

     random_sub = random.choice(all_subs)

     name = random_sub.title
     url = random_sub.url

     idot = discord.Embed(title=name,description=f"**LINK:** {url}",colour=discord.Color.gold(),timestamp=datetime.datetime.now()).set_footer(text="This Meme is from https://reddit.com/r/memes")
     idot.set_image(url=url)

     await jacky.edit(content="Here's One Of The **Top 50 posts** of the week in this Subreddit!")
     await ctx.send(embed=idot)


    @meme.command()
    async def jack(self, ctx):
     jacky = await ctx.send("Please Hold On! I'm getting some of the Juicy Memes from the Jacksucksatlife SubReddit!")

     subreddit = reddit.subreddit("Jacksucksatlife")
     all_subs = []

     top = subreddit.top(limit=50)

     for submission in top:
       all_subs.append(submission)

     random_sub = random.choice(all_subs)

     name = random_sub.title
     url = random_sub.url

     idot = discord.Embed(title=name,description=f"**LINK:** {url}",colour=discord.Color.gold(),timestamp=datetime.datetime.now()).set_footer(text="This Meme is from https://reddit.com/r/Jacksucksatlife")
     idot.set_image(url=url)

     await jacky.edit(content="Here's One Of The **Top 50 posts** of the week in this Subreddit!")
     await ctx.send(embed=idot)

def setup(bot):
    bot.add_cog(Memes(bot))       