import discord
from discord.ext import commands
import asyncio

bot = commands.Bot(command_prefix = "{")

@bot.command()
async def copy(ctx):
    with open("file.txt", "w") as f:
        async for message in ctx.history(limit=1000):
            f.write(message.content + "\n")

    await ctx.send("Done!")