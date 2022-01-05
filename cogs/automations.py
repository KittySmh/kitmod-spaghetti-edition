import discord
from discord.ext import commands
import asyncio
import datetime
import time
from datetime import timezone
import json

class automations(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload: discord.RawReactionActionEvent):

     if payload.member.bot:
        pass

     else:
        with open('reactrole.json') as react_file:
            data = json.load(react_file)
            for x in data:
                if x['emoji'] == payload.emoji.name:
                    role = discord.utils.get(self.bot.get_guild(
                        payload.guild_id).roles, id=x['role_id'])

                    await payload.member.add_roles(role)


    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload: discord.RawReactionActionEvent):

     with open('reactrole.json') as react_file:
        data = json.load(react_file)
        for x in data:
            if x['emoji'] == payload.emoji.name:
                role = discord.utils.get(self.bot.get_guild(
                    payload.guild_id).roles, id=x['role_id'])

                
                await self.bot.get_guild(payload.guild_id).get_member(payload.user_id).remove_roles(role)


def setup(bot):
  bot.add_cog(automations(bot))   