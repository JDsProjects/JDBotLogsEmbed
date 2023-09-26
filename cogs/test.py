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

            timestamp = discord.utils.format_dt(member.created_at, "F")
            embed = discord.Embed(color=240396, timestamp=member.joined_at)

            embed.add_field(name="Name:", value=f"**{member.mention}({member})**", inline=False)
            embed.add_field(name="Creation Date:", value=f"**{timestamp}**", inline=False)
            embed.add_field(name="Position:", value=f"**{humanize.ordinal(pos)}**", inline=False)

            embed.set_author(name=f"{member.guild} just received a new member", icon_url=member.display_avatar.url)

            embed.set_thumbnail(url=member.guild.icon.url if member.guild.icon else "https://i.imgur.com/3ZUrjUP.png")

            embed.set_image(url=member.display_avatar.url)

            embed.set_footer(text=f"ID: {member.id}")

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


            timestamp = discord.utils.format_dt(member.joined_at, "F")
            embed = discord.Embed(color=16581893)

            embed.add_field(name="Name:", value=f"**{member.mention}({member})**", inline=False)
            embed.add_field(name="Join Date:", value=f"**{timestamp}**", inline=False)
            embed.add_field(name="Position:", value=f"**{humanize.ordinal(pos)}**", inline=False)

            embed.set_author(name=f"{member.guild} just lost a member", icon_url=member.display_avatar.url)

            embed.set_thumbnail(url=member.guild.icon.url if member.guild.icon else "https://i.imgur.com/3ZUrjUP.png")

            embed.set_image(url=member.display_avatar.url)

            embed.set_footer(text=f"ID: {member.id}")

            await interaction.response.send_message("There", embed=embed)

        else:
            await interaction.response.send_message("User detected, ignoring this.")
    
async def setup(bot):
    await bot.add_cog(Embed(bot))