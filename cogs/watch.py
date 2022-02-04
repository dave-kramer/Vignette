import discord
import datetime

from aiohttp import request
from discord.ext import commands


class Watch(commands.Cog):
    def __init__(self, client):
        self.client = client
    description = "Gets the recently and popular released anime episodes from the MAL watch page"


    @commands.command(name='watch')
    async def watch(self, ctx, arg=None):
        '''Pulls the right data from MAL, checks the arguments needed to use the function correctly.
        '''

        if arg == "recent":
            URL = f"https://api.jikan.moe/v4/watch/episodes"
            URL2 = "https://myanimelist.net/watch/episode"
            setTitle = "Latest 6 released anime episodes on MyAnimeList"
            setImage = "http://static.zerochan.net/Tsukinose.Vignette.April.full.2657880.gif"

        elif arg == "popular":
            URL = f"https://api.jikan.moe/v4/watch/episodes/popular"
            URL2 = "https://myanimelist.net/watch/episode/popular"
            setTitle = "Latest 6 released popular anime episodes on MyAnimeList"
            setImage = "http://i.imgur.com/2KCjOZB.gif"

        elif arg is None:
            await ctx.send("I can only retrieve .watch <recent or popular>")
            return None

        else:
            await ctx.send("I can only retrieve .watch <recent or popular>")
            return None


        # Sents get request pulling the data
        async with request("GET", URL, headers={}) as response:
            if response.status == 200:
                databox = await response.json()
                data = databox["data"]


            # creates a list, loops through the data, adds it to the list
            # then splits it correctly, the "*" is used because there are anime
            # that uses the ","
            listdata = []
            i = 0

            embed=discord.Embed(title=setTitle, url=URL2, color=0xf37a12)

            for length in range(0,len(data)):
                if i == 6:
                    continue
                else:
                    if data[length]['episodes'][0]['premium'] == True:
                        listdata.append(f"[{data[length]['entry']['title']}]({data[length]['episodes'][0]['url']}) released **{data[length]['episodes'][0]['title']}** and is `paid` to watch.\n")
                    else:
                        listdata.append(f"[{data[length]['entry']['title']}]({data[length]['episodes'][0]['url']}) released **{data[length]['episodes'][0]['title']}** and is `free` to watch.\n")
                    i += 1

            string = ' '.join([str(item) for item in listdata])

            embed.add_field(name="\u200b", value=f"{string}", inline=False)

            embed.set_image(url=setImage)
            embed.set_footer(text="Requested by: {}".format(ctx.author.display_name), icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
            embed.timestamp = datetime.datetime.utcnow()

            await ctx.send(embed=embed)


# adding cog to bot setup
def setup(bot):
    bot.add_cog(Watch(bot))
