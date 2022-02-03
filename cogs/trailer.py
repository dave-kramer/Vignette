import discord
import datetime

from aiohttp import request
from discord.ext import commands
from discord.ext.commands import MissingRequiredArgument


class Trailer(commands.Cog):

    def __init__(self, client):
        self.client = client
    description = "Gets the watch page from MyAnimeList"

    @commands.command(name='trailer')
    async def trailer(self, ctx, arg=None):
        if arg == "recent":
            URL = f"https://api.jikan.moe/v4/watch/promos"
            URL2 = "https://myanimelist.net/watch/promotion"
            setTitle = "Latest 25 released anime trailers on MyAnimeList"
            setImage = "http://static.zerochan.net/Tsukinose.Vignette.April.full.2657880.gif"
        elif arg == "popular":
            URL = f"https://api.jikan.moe/v4/watch/promos/popular"
            URL2 = "https://myanimelist.net/watch/promotion/popular"
            setTitle = "Latest 25 released popular anime trailers on MyAnimeList"
            setImage = "http://i.imgur.com/2KCjOZB.gif"
        elif arg is None:
            await ctx.send("I can only retrieve .trailer <recent or popular>")
            return None
        else:
            await ctx.send("I can only retrieve .trailer <recent or popular>")
            return None

        async with request("GET", URL, headers={}) as response:
            if response.status == 200:
                databox = await response.json()
                data = databox['data']
                #print(data)

            embed = discord.Embed(title="Vignette", url="https://github.com/dave-kramer/vignette", description="Woopsie! I'm still working on this command, give me some time!", color=0x87CEEB)
            embed.set_image(url="https://i.pinimg.com/originals/9f/20/76/9f2076c3c2eff838420384629496466e.gif")
            embed.set_footer(text="Requested by: {}".format(ctx.author.display_name), icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
            embed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Trailer(bot))
