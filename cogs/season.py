import discord
import datetime

from aiohttp import request
from discord.ext import commands
from discord.ext.commands import MissingRequiredArgument


class Season(commands.Cog):

    def __init__(self, client):
        self.client = client
    description = "Gets the top from MyAnimeList"

    @commands.command(name='season')
    async def top(self, ctx, arg: str, arg2=None):
        if arg.lower() in ("summer", "fall", "winter", "spring"):
            URL = f"https://api.jikan.moe/v4/seasons/{arg2}/{arg.lower()}"
            URL2 = f"https://myanimelist.net/anime/season/{arg2}/{arg.lower()}"
            if arg2 is None:
                await ctx.send("You've forgotten the year.")
                return None
        else:
            await ctx.send("I can only retrieve .season <summer, fall, winter and spring> <year>")
            return None

        async with request("GET", URL, headers={}) as response:
            if response.status == 200:
                databox = await response.json()
                data = databox["data"]
                #print(data)

                listdata = []
                embed = discord.Embed(title=f"Anime in {arg.lower().title()} {arg2} ", url=URL2, color=0x87CEEB)
                for length in range(0,len(data)):
                    listdata.append(data[length]['title']) # title
                    listdata.append(data[length]['url']) # url
                    listdata.append(data[length]['aired']['from'][:-15]) # release date
                    embed.add_field(name="\u200b", value=f"[{data[length]['title']}]({data[length]['url']}) is airing on {data[length]['aired']['from'][:-15]}", inline=False)
                string = '*'.join([str(item) for item in listdata])
                x = string.split("*")
                print(x)
                embed.set_footer(text="Requested by: {}".format(ctx.author.display_name), icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
                embed.timestamp = datetime.datetime.utcnow()
                await ctx.send(embed=embed)

            else:
                await ctx.send("I can only retrieve .season <summer, fall, winter and spring> <year>")


def setup(bot):
    bot.add_cog(Season(bot))