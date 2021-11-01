import discord
import json
import requests

from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('Vignette is on.')

# PUT BOT TOKEN
client.run('TOKEN')
