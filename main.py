import os
import traceback
from typing import Any

import discord
from discord.ext import commands
from dotenv import load_dotenv

from cogs import EXTENSIONS


class EmbedBot(commands.Bot):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

    async def setup_hook(self) -> None:
        for cog in EXTENSIONS:
            try:
                await self.load_extension(f"{cog}")
            except commands.errors.ExtensionError:
                traceback.print_exc()

        await self.load_extension("jishaku")


bot = EmbedBot(command_prefix=commands.when_mentioned_or("e$"), intents=discord.Intents.all(), strip_after_prefix=True)

@bot.event
async def on_ready():
    print(bot.user)
    print(bot.id)

# so far this.

load_dotenv()
bot.run(os.environ["TOKEN"])
