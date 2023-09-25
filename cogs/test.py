from discord.ext import commands

import discord
import humanize

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

            try:
                pos = sorted(member.guild.members, key=lambda m: m.joined_at or m.created_at).index(member) + 1

            except:
                pos = "N/A"

            timestamp = discord.utils.format_dt(member.joined_at, "F")
            embed = discord.Embed(description=f"{member} was the {humanize.ordinal(pos)} member to join \nJoin Date: {timestamp}", color=240396)

            embed.set_footer(text=f"ID: {member.id}")

            embed.set_author(name=f"{member.guild} just received a new member", icon_url=member.display_avatar.url)

            embed.set_thumbnail(url=member.guild.icon.url if member.guild.icon else "https://i.imgur.com/3ZUrjUP.png")

            embed.set_image(url=member.display_avatar.url)

            await interaction.response.send_message("There", embed=embed)

        else:
            await interaction.response.send_message("User detected, ignoring this.")


    @app_commands.command(description="leave embed test", name="leave")
    async def leave(self, interaction: discord.Interaction, member : typing.Union[discord.Member, discord.User]):

        
        member = member or interaction.user

        if isinstance(member, discord.Member):

            try:
                pos = sorted(member.guild.members, key=lambda m: m.joined_at or m.created_at).index(member) + 1

            except:
                pos = "N/A"

            embed = discord.Embed(description=f"This person was the {humanize.ordinal(pos)} out of {len(member.guild.members)} members to join.",timestamp=member.joined_at,color=16581893 )

            embed.set_footer(text=f"ID: {member.id}")

            embed.set_author(name=f"{member} just left {member.guild.name}")

            embed.set_image(url=member.display_avatar.url)

            embed.set_thumbnail(url=member.guild.icon.url if member.guild.icon else "https://i.imgur.com/3ZUrjUP.png")

            await interaction.response.send_message("There", embed=embed)

        else:
            await interaction.response.send_message("User detected, ignoring this.")
    
async def setup(bot):
    await bot.add_cog(Embed(bot))