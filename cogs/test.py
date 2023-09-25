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

            embed = discord.Embed(title=f"{member} just joined {member.guild.name}", description=f"This person joined {humanize.ordinal(pos)} out of {humanize.ordinal(len(member.guild.members))} members",timestamp=member.joined_at,color=random.randint(0, 16777215))

            embed.set_footer(text=f"User ID: {member.id}")

            embed.set_image(url=member.display_avatar.url)

            embed.set_thumbnail(url=member.guild.icon.url if member.guild.icon else "https://i.imgur.com/3ZUrjUP.png")

            await interaction.response.send_message("There", embed=embed)

        else:
            await interaction.response.send_message("User detected, ignoring this.")
    
async def setup(bot):
    await bot.add_cog(Embed(bot))