#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##################################################
# Discord BOT
# Title: Discord Bot for statistics of channels
# Author: Vojtěch Petrásek 
# Generated: 04/11/2021 20:55:01
##################################################

###
# imports
###

import os
import sys
import discord
from discord.ext import commands
import asyncio
import time

bot = commands.Bot(command_prefix = "/")


@bot.command("a")
async def copy(ctx):
    await ctx.send("Starting downloading!")
    print(ctx.guild)
    print(ctx.channel)
    print(ctx.cog)
    with open("file.txt", "w", encoding='utf-8') as f:
        async for message in ctx.history():
            if message.author != bot.user:
                d = []
                d.append(message.author)
                d.append(message.content)
                d.append(message.reactions)

                f.write(str(d) +"\n")

    await ctx.send("Done!")

if __name__ == '__main__':
    try:
        bot.run('')
    except Exception as e:
        print('Exited with error: {}'.format(e))
        sys.exit(1)