import discord
import time
import datetime

from aiohttp import request
from discord.ext import commands
from discord.ext.commands import MissingRequiredArgument


class Trace(commands.Cog):

    def __init__(self, client):
        self.client = client
    description = "Helps you find the episode through a image scan by trace.moe"


    @commands.command(name='trace')
    async def trace(self, ctx, arg: str):
        '''Uses trace.moe to check for the image
        '''
        URL = f"https://api.trace.moe/search?url={arg}"
        async with request("GET", URL, headers={}) as response:
            if response.status == 200:
                databox = await response.json()
                data = databox['result']

            n = 0

            # Loops through the data, creates embed field for 5 of them, cuts off the rest.
            embed = discord.Embed(title=f"trace.moe", url=f"https://trace.moe/?url={arg}",  color=0x87CEEB)
            for i in data:
                if n == 5:
                    continue
                else:
                    embed.add_field(name=f"{data[n]['filename']}", value=f"Episode {data[n]['episode']} at {time.strftime('%H:%M:%S', time.gmtime(data[n]['from']))} to {time.strftime('%H:%M:%S', time.gmtime(data[n]['to']))} with a similarity of {round(data[n]['similarity'], 2)}%\n[Video]({data[n]['video']}) - [Image]({data[n]['image']}) - [AniList](https://anilist.co/anime/{data[n]['anilist']})", inline=False)
                    n += 1

            embed.set_thumbnail(url=arg)
            embed.set_footer(text="Requested by: {}".format(ctx.author.display_name), icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
            embed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=embed)

    # if argument has been used wrong it triggers the MissingRequiredArgument below
    @trace.error
    async def trace_error(self, ctx, error):
        if isinstance(error, (MissingRequiredArgument)):
            if ctx.guild:
                await ctx.send('Woopsie! do as following: .trace yourimagelinkhere')
            else:
        	    return


def setup(bot):
    bot.add_cog(Trace(bot))