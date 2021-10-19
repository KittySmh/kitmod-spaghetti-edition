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

    async def select_callback(self, select, interaction):
        # Use the interaction object to send a response message containing
        # the user's favourite colour or choice. The self object refers to the
        # Select object, and the values attribute gets a list of the user's
        # selected options. We only want the first one.
        print(self.values)
        if self.values[0] == "Moderation":
            await interaction.response.send_message('Moderation :eyes:', ephemeral=True)
        elif self.values[0] == "Utilities":
            await interaction.response.send_message('Utility :eyes:', ephemeral=True)
        elif self.values[0] == "Miscellaneous":
          await interaction.response.send_message('Misc :eyes:', ephemeral=True)    


class DropdownView(discord.ui.View):
    def __init__(self):
        super().__init__()

        # Adds the dropdown to our view object.
        self.add_item(Dropdown())

class Halp(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def halp(self,ctx):
      view = DropdownView()
      await ctx.send(embed=discord.Embed(description="Select an option to get started!").set_author(name=f"SPVM Public Assistance Office", icon_url=str("https://media.discordapp.net/attachments/835359268432773133/863792001065811978/SVPM_Logo_2.jpg?width=415&height=468")).add_field(name="• Moderation",value="Displays Moderation Commands",inline=False).add_field(name="• Utilities",value="Displays Commands in the Utilities Category",inline=False).add_field(name="• Miscellaneous",value="Displays Commands in the Miscellaneous Category",inline=False),view=view)

          

    


def setup(bot):
    bot.add_cog(Halp(bot))        