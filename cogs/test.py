import random
import typing

import discord
import humanize
from discord import app_commands
from discord.ext import commands


class Embed(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def cog_unload(self):
        return
        # use for later.

    @app_commands.command(description="join embed test", name="join")
    async def join(self, interaction: discord.Interaction, member: typing.Union[discord.Member, discord.User]):

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
            embed.add_field(name="Join Position:", value=f"**{humanize.ordinal(pos)}**", inline=False)

            embed.set_author(name=f"{member.guild} just received a new member", icon_url=member.display_avatar.url)

            embed.set_thumbnail(url=member.guild.icon.url if member.guild.icon else "https://i.imgur.com/3ZUrjUP.png")

            embed.set_image(url=member.display_avatar.url)

            embed.set_footer(text=f"ID: {member.id}")

            await interaction.response.send_message("There", embed=embed)

        else:
            await interaction.response.send_message("User detected, ignoring this.")

    @app_commands.command(description="leave embed test", name="leave")
    async def leave(self, interaction: discord.Interaction, member: typing.Union[discord.Member, discord.User]):

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
            embed.add_field(name="Join Position:", value=f"**{humanize.ordinal(pos)}**", inline=False)

            embed.set_author(name=f"{member.guild} just lost a member", icon_url=member.display_avatar.url)

            embed.set_thumbnail(url=member.guild.icon.url if member.guild.icon else "https://i.imgur.com/3ZUrjUP.png")

            embed.set_image(url=member.display_avatar.url)

            embed.set_footer(text=f"ID: {member.id}")

            await interaction.response.send_message("There", embed=embed)

        else:
            await interaction.response.send_message("User detected, ignoring this.")

    @app_commands.command(description="kick embed test", name="kicked")
    async def kicked(
        self,
        interaction: discord.Interaction,
        member: typing.Union[discord.Member, discord.User],
        reason: typing.Optional[str],
    ):

        reason = reason or "Test"

        member = member or interaction.user

        if isinstance(member, discord.Member):

            try:
                pos = sorted(member.guild.members, key=lambda m: m.joined_at or m.created_at).index(member) + 1

            except:
                pos = "N/A"

            # kicked embeds must be private in general (moderator only)

            timestamp = discord.utils.format_dt(member.joined_at, "F")
            embed = discord.Embed(color=16581893)

            embed.add_field(name="Name:", value=f"**{member.mention}({member})**", inline=False)
            embed.add_field(name="Join Date:", value=f"**{timestamp}**", inline=False)
            embed.add_field(name="Join Position:", value=f"**{humanize.ordinal(pos)}**", inline=False)
            embed.add_field(name="Reason:", value=f"**{reason}**")

            embed.add_field(name="Mod:", value=f"**{interaction.user.mention}({interaction.user})**")

            # Mod here would actually be the mod but grabbed from the audit log

            embed.set_author(name=f"{member.guild} just kicked a member", icon_url=member.display_avatar.url)

            embed.set_thumbnail(url=member.guild.icon.url if member.guild.icon else "https://i.imgur.com/3ZUrjUP.png")

            embed.set_image(url=member.display_avatar.url)

            embed.set_footer(text=f"ID: {member.id}")

            await interaction.response.send_message("There", embed=embed)

        else:
            await interaction.response.send_message("User detected, ignoring this.")

    @app_commands.command(description="ban embed test", name="banned")
    async def banned(
        self,
        interaction: discord.Interaction,
        member: typing.Union[discord.Member, discord.User],
        reason: typing.Optional[str],
    ):

        reason = reason or "Test"

        member = member or interaction.user

        if isinstance(member, discord.Member):

            try:
                pos = sorted(member.guild.members, key=lambda m: m.joined_at or m.created_at).index(member) + 1

            except:
                pos = "N/A"

            # banned embeds must be private in general (moderator only)

            timestamp = discord.utils.format_dt(member.joined_at, "F")
            embed = discord.Embed(color=16581893)

            embed.add_field(name="Name:", value=f"**{member.mention}({member})**", inline=False)
            embed.add_field(name="Join Date:", value=f"**{timestamp}**", inline=False)
            embed.add_field(name="Join Position:", value=f"**{humanize.ordinal(pos)}**", inline=False)
            embed.add_field(name="Reason:", value=f"**{reason}**")

            embed.add_field(name="Mod:", value=f"**{interaction.user.mention}({interaction.user})**")

            # Mod here would actually be the mod but grabbed from the audit log

            embed.set_author(name=f"{member.guild} just banned a member", icon_url=member.display_avatar.url)

            embed.set_thumbnail(url=member.guild.icon.url if member.guild.icon else "https://i.imgur.com/3ZUrjUP.png")

            embed.set_image(url=member.display_avatar.url)

            embed.set_footer(text=f"ID: {member.id}")

            await interaction.response.send_message("There", embed=embed)

        else:
            await interaction.response.send_message("User detected, ignoring this.")

    @app_commands.command(description="unban embed test", name="unbanned")
    async def unbanned(
        self,
        interaction: discord.Interaction,
        member: typing.Union[discord.Member, discord.User],
        reason: typing.Optional[str],
    ):

        reason = reason or "Test"

        member = member or interaction.user

        if isinstance(member, discord.Member):

            try:
                pos = sorted(member.guild.members, key=lambda m: m.joined_at or m.created_at).index(member) + 1

            except:
                pos = "N/A"

            # unbanned embeds must be private in general (moderator only)

            timestamp = discord.utils.format_dt(member.joined_at, "F")
            embed = discord.Embed(color=16581893)

            embed.add_field(name="Name:", value=f"**{member.mention}({member})**", inline=False)
            embed.add_field(name="Join Date:", value=f"**{timestamp}**", inline=False)
            embed.add_field(name="Join Position:", value=f"**{humanize.ordinal(pos)}**", inline=False)
            embed.add_field(name="Reason:", value=f"**{reason}**")

            embed.add_field(name="Mod:", value=f"**{interaction.user.mention}({interaction.user})**")

            # Mod here would actually be the mod but grabbed from the audit log

            embed.set_author(name=f"{member.guild} just unbanned a member", icon_url=member.display_avatar.url)

            embed.set_thumbnail(url=member.guild.icon.url if member.guild.icon else "https://i.imgur.com/3ZUrjUP.png")

            embed.set_image(url=member.display_avatar.url)

            embed.set_footer(text=f"ID: {member.id}")

            await interaction.response.send_message("There", embed=embed)

        else:
            await interaction.response.send_message("User detected, ignoring this.")

    @app_commands.command(description="member change embed test", name="member_change")
    async def member_update(
        self,
        interaction: discord.Interaction,
        before: typing.Union[discord.Member, discord.User],
        after: typing.Union[discord.Member, discord.User],
    ):

        embed = discord.Embed(
            description=f"{before.mention} **updated their profile!**",
            color=random.randint(0, 16777215),
            timestamp=discord.utils.utcnow(),
        )
        embed.set_author(name=f"{before}", icon_url=after.display_avatar.url)
        embed.set_footer(text=f"User ID: {before.id}")

        if not before.name == after.name:
            embed.add_field(name="Username", value=f"{before.name} -> {after.name}")

        if not before.display_avatar == after.display_avatar:
            embed.add_field(
                name="Avatar", value=f"[[before]]({before.display_avatar.url}) -> [[after]]({after.display_avatar.url})"
            )
            embed.set_thumbnail(url=after.display_avatar.url)
            embed.set_image(url=after.display_avatar.url)

        if not before.discriminator == after.discriminator:
            embed.add_field(name="Discriminator", value=f"#{before.discriminator} -> {after.discriminator}")

        await interaction.response.send_message(content="Work in Progress Embed:", embed=embed)

        # check https://discordpy.readthedocs.io/en/latest/api.html#discord.on_member_update for full list of changes


async def setup(bot):
    await bot.add_cog(Embed(bot))
