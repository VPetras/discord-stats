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
import matplotlib.pyplot as plt

bot = commands.Bot(command_prefix = "/")

@bot.command("channels")
async def channels(ctx):
    channels = ctx.guild.text_channels
    ch = []
    for channel in channels:
        ch.append(channel.name)
    await ctx.send(ch)

@bot.command("stats")
async def stats(ctx):
    msg = ctx.message.content.split(' ')
    if len(msg) == 1:
        await ctx.send('i need specific channel to make stats')
    else:
        channels = ctx.guild.text_channels
        channel = None
        for ch in channels:
            if msg[1] == ch.name:
                print('found')
                channel = ch
                break
            print('a')
        if id == None:
            await ctx.send("Channel not found. Try /channels")
        else:
            await ctx.send("Channel found. Please wait. " + str(channel.id))
            with open(channel.name + ".txt", "w", encoding='utf-8') as f:
                users = {}
                c = 0
                async for message in channel.history(limit=999999999):
                    #if message.author != bot.user:
                        c +=1
                        d = []
                        if message.author.name not in users:
                            users[message.author.name] = 0
                        users[message.author.name] += 1
                        d.append(message.author)
                        d.append(message.content)
                        d.append(message.reactions)

                        f.write(str(d) +"\n")
                await ctx.send(users)
                await ctx.send(c)

                user = []
                count = []
                coord = []
                c = 0
                for usr in users:
                    user.append(usr)
                    count.append(users[usr])
                    coord.append(c)
                    c +=1
                
                plt.bar(user,count, color=['blue'], width = 0.8)
                plt.title(channel.name)
                plt.savefig(channel.name + ".png")
                with open(channel.name + ".png", 'rb') as f:
                    graph = discord.File(f)
                    await ctx.send(file=graph)
                print(user,count)



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
        with open('token') as t:
            token = t.readline()
            print(token)
        t.close()
        bot.run(token)
    except Exception as e:
        print('Exited with error: {}'.format(e))
        sys.exit(1)