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
    async def waifu(self, ctx):
        '''Returns an image from the waifu.im API
        '''
        URL = f"https://api.waifu.im/sfw/waifu"
        
        async with request("GET", URL, headers={}) as response:
            if response.status == 200:
                databox = await response.json()
                data = databox['images'][0]

                embed = discord.Embed(title=f"Waifu {data['image_id']}", url=f"{data['url']}", color=0x87CEEB)
                embed.set_image(url=data['url'])
                embed.set_footer(text="Requested by: {}".format(ctx.author.display_name), icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
                embed.timestamp = datetime.datetime.utcnow()
                await ctx.send(embed=embed)
    @waifu.error
    async def waifu_error(self, ctx, error):
        if isinstance(error, (MissingRequiredArgument)):
            if ctx.guild:
                await ctx.send('Woopsie! do as following: .waifu or .maid')
            else:
                return


    @commands.command(name='maid')
    async def maid(self, ctx):
        '''Returns an image from the waifu.im API
        '''
        URL = f"https://api.waifu.im/sfw/maid"
        
        async with request("GET", URL, headers={}) as response:
            if response.status == 200:
                databox = await response.json()
                data = databox['images'][0]

                embed = discord.Embed(title=f"Maid {data['image_id']}", url=f"{data['url']}", color=0x87CEEB)
                embed.set_image(url=data['url'])
                embed.set_footer(text="Requested by: {}".format(ctx.author.display_name), icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
                embed.timestamp = datetime.datetime.utcnow()
                await ctx.send(embed=embed)


    @maid.error
    async def waifu_error(self, ctx, error):
        if isinstance(error, (MissingRequiredArgument)):
            if ctx.guild:
                await ctx.send('Woopsie! do as following: .waifu or .maid')
            else:
                return


# adding cog to bot setup
def setup(bot):
	bot.add_cog(Waifu(bot))