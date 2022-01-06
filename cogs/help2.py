import typing
import traceback

import discord
from discord.ext import commands

# Defines a custom Select containing colour options
# that the user can choose. The callback function
# of this class is called when the user changes their choice
class Dropdown(discord.ui.Select):
    def __init__(self):
        

        # Set the options that will be presented inside the dropdown
        options = [
            discord.SelectOption(
                label="Moderation", description="Displays Moderation Options That Are Currently Available To Enforce Moderation.", emoji="🛡️"
            ),
            discord.SelectOption(
                label="Utilities", description="Displays Utility Options That Are Currently Available To Assist In The Server.", emoji="🛠️"
            ),
            discord.SelectOption(
                label="Miscellaneous", description="Displays Miscellaneous Options That Are Currently Available.", emoji="🍍"
            ),
        ]

        # The placeholder is what will be shown when no option is chosen
        # The min and max values indicate we can only pick one of the three options
        # The options parameter defines the dropdown options. We defined this above
        super().__init__(
            placeholder="Select an option here!",
            min_values=1,
            max_values=1,
            options=options,
        )
      
    async def callback(self, interaction: discord.Interaction):
         print(self.values[0])
         if self.values[0] == "Moderation":
            await interaction.response.send_message(content='Moderation :eyes:', ephemeral=True)
         elif self.values[0] == "Utilities":
            await interaction.response.send_message(content='Utility :eyes:', ephemeral=True)
         elif self.values[0] == "Miscellaneous":
          await interaction.response.send_message(content='Misc :eyes:', ephemeral=True)    


class DropdownView(discord.ui.View):
    def __init__(self, ctx):
        self.context = ctx
        super().__init__()
        super().__init__(timeout=20)

        async def interaction_check(self, interaction):
         if interaction.user.id != self.context.author.id:
            await interaction.response.send_message("You can't use interactions invoked by others!", ephemeral=True)
            return False
         else:
            return True

        async def on_timeout(self):
         for child in self.children:
            child.disabled = True
            await self.message.edit(view=self)
  
        
       
        # Adds the dropdown to our view object.
        self.add_item(Dropdown())
        self.add_item(discord.ui.Button(label='Join the support server!', url='https://discord.gg/CrpzQKEVWV', style=discord.ButtonStyle.url))

class Halp(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def halp(self,ctx):
      view = DropdownView(ctx)
      
      view.message = await ctx.send(embed=discord.Embed(description="Select an option to get started!").set_author(name=f"KitMod Help Centre", icon_url=str("https://media.discordapp.net/attachments/927900309236371546/928264110058135572/KidModLogo.png?width=631&height=473")).add_field(name="• Moderation",value="Displays Moderation Commands",inline=False).add_field(name="• Utilities",value="Displays Commands in the Utilities Category",inline=False).add_field(name="• Miscellaneous",value="Displays Commands in the Miscellaneous Category",inline=False),view=view)

          

    


def setup(bot):
    bot.add_cog(Halp(bot))        