import discord
import os
import random
import asyncio

from discord.ext import commands

"""
Make sure to put YOUR bot token inbetween the '' otherwise the bot won't load.
"""
TOKEN = ''
client = commands.Bot(command_prefix = '.')


@client.command()
async def reload(ctx, extension):
    """
    | Reload command for cogs
    | To reload a function use .reload with the cog name - example: .reload animesearch
    """
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')


for filename in os.listdir('./cogs'):
    """
    | Loading all the available cogs
    """
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


@client.event
async def on_ready():
    """
    | Activity of the discord bot
    """
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='https://davekramer.nl'))
    print('Vignette is online.')


async def ch_pr():
    await client.wait_until_ready()
    """
    | Add multiple statuses by changing inbetween the "" or adding the , and putting more "" before the ]
    """
    statuses = ["anime", "your every move", "https://davekramer.nl", "hentai", "BLACKPINK"]

    while not client.is_closed():
        status = random.choice(statuses)
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=status))
        """
        | You can change the timer for activity by replacing the 120 (2minutes) with for example 60 (1minute) just make sure to put it in seconds.
        """
        await asyncio.sleep(120)

client.loop.create_task(ch_pr())

"""
Bot run.
"""
client.run(TOKEN)
