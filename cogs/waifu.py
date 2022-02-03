import discord
import datetime

from aiohttp import request
from discord.ext import commands
from discord.ext.commands import MissingRequiredArgument


class Waifu(commands.Cog):

    def __init__(self, client):
        self.client = client
    description = "Returns a waifu or maid."

    @commands.command(name='waifu')
    async def waifu(self, ctx, arg=None):
        '''Returns an image from the waifu.pics API
        '''
        if arg is None:
            URL = f"https://api.waifu.pics/sfw/waifu"
        elif arg in ("neko", "shinobu", "megumin", "bully", "cuddle", "cry", "hug", "awoo", "kiss", "lick", "pat", "smug", "bonk", "yeet", "blush", "smile", "wave", "highfive", "handhold", "nom", "bite", "glomp", "slap", "kill", "kick", "happy", "wink", "poke", "dance", "cringe"):
            URL = f"https://api.waifu.pics/sfw/{arg}"
        else:
            await ctx.send('Woopsie! do as following: .waifu cry - for A LOT more like kiss & cry through .commands')
            return None

        async with request("GET", URL, headers={}) as response:
            if response.status == 200:
                data = await response.json()
                await ctx.send(data['url'])

    @waifu.error
    async def waifu_error(self, ctx, error):
        if isinstance(error, (MissingRequiredArgument)):
            if ctx.guild:
                await ctx.send('Woopsie! do as following: .waifu or .maid')
            else:
                return

# adding cog to bot setup
def setup(bot):
	bot.add_cog(Waifu(bot))