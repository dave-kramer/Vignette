import discord
import os
import json
import requests
import random
import asyncio

from discord.ext import commands

# Put your bot token in here.
TOKEN = 'OTA0NjY1NDI2Mzg5MjU0MTU0.YX-1VQ.Tk-mutatB_VRoofJdsDL8TMBg9U'
client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='https://davekramer.nl'))
    print('Vignette is online.')

# Changes activity every 120 seconds, to customize this change statuses to strings you like, to change the type of activity read up the discord doc.
async def ch_pr():
    await client.wait_until_ready()

    statuses = ["anime", "your every move", "https://davekramer.nl"]

    while not client.is_closed():
        status = random.choice(statuses)
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=status))
        await asyncio.sleep(120)

client.loop.create_task(ch_pr())

# Runs the bot.
client.run(TOKEN)
