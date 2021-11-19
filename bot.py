import discord
import os
import random
import asyncio

from discord.ext import commands

# Put your bot token in here
# Make sure to put it between the '' otherwise the bot won't work
TOKEN = ''
client = commands.Bot(command_prefix = '.')

# Reload command for cogs
# To reload a function use .reload with the cog name - example: .reload animesearch
@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')

# Loading all the available cogs
for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
    client.load_extension(f'cogs.{filename[:-3]}')

# Activity of the discord bot
# Add your own statuses to make your bot change activity.
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='https://davekramer.nl'))
    print('Vignette is online.')

async def ch_pr():
    await client.wait_until_ready()
    # Add multiple statuses with "", 
    statuses = ["anime", "your every move", "https://davekramer.nl"]

    while not client.is_closed():
        status = random.choice(statuses)
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=status))
        # You can change your own timer by replacing the 120 (2minutes) with for example 60 (1minute) just make sure to put it in seconds.
        await asyncio.sleep(120)

client.loop.create_task(ch_pr())

# Leave this to let the bot run
client.run(TOKEN)
