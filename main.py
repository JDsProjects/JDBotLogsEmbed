import discord
from discord.ext import commands

bot = commands.Bot(command_prefix=commands.when_mentioned_or("e$"), intents=discord.Intents.all(), strip_after_prefix=True)

#so far this.
