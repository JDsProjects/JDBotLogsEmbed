from discord.ext import commands

import discord

import random
import typing

from discord import app_commands

class Embed(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    async def cog_unload(self):
        return
        #use for later.

    @app_commands.command(description="join embed test", name="join")
    async def join(self, interaction: discord.Interaction, member : typing.Union[discord.Member, discord.User]):

        
        member = member or interaction.user

        if isinstance(member, discord.Member):

            embed = discord.Embed(title=f"{member} just joined {member.guild.name}", timestamp=member.joined_at,color=random.randint(0, 16777215))

            embed.set_footer(text=f"User ID: {member.id}")

            embed.set_image(url=interaction.user.display_avatar.url)

            await interaction.response.send_message("There", embed=embed)

        else:
            await interaction.response.send_message("User detected, ignoring this.")
    
async def setup(bot):
    await bot.add_cog(Embed(bot))