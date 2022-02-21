import discord
import datetime

from aiohttp import request
from discord.ext import commands
from discord.ext.commands import MissingRequiredArgument


class Season(commands.Cog):

    def __init__(self, client):
        self.client = client
    description = "Gets the seasons from MyAnimeList"


    @commands.command(name='season')
    async def top(self, ctx, arg: str, arg2=None):
        if arg.lower() in ("summer", "fall", "winter", "spring"):
            URL = f"https://api.jikan.moe/v4/seasons/{arg2}/{arg.lower()}"
            URL2 = f"https://myanimelist.net/anime/season/{arg2}/{arg.lower()}"
            if arg2 is None:
                await ctx.send("You've forgotten the year.")
                return None
        elif arg.lower() == "upcoming":
            URL = f"https://api.jikan.moe/v4/seasons/{arg.lower()}"
            URL2 = f"https://myanimelist.net/anime/season/later"
        else:
            await ctx.send("I can only retrieve .season <summer, fall, winter and spring> <year>")
            return None

        async with request("GET", URL, headers={}) as response:
            if response.status == 200:
                databox = await response.json()
                listnumber = 0
                if arg.lower() == "upcoming":
                    data = databox["data"]

                    listdata = []
                    for length in range(0,len(data)):
                        listnumber += 1
                        listdata.append(f"{listnumber}. **{data[length]['title']}** is airing on `unknown`\n") # title
                    string = ' '.join([str(item) for item in listdata])
                    await ctx.send(f"**Anime released later**\n\n{string}")

                else:
                    data = databox["data"]
                    listdata = []
                    for length in range(0,len(data)):
                        listnumber += 1
                        listdata.append(f"{listnumber}. **{data[length]['title']}** is airing on `{data[length]['aired']['from'][:-15]}`\n") # title
                    string = ' '.join([str(item) for item in listdata])

                    URL = URL + "?page=2"

                    async with request("GET", URL, headers={}) as response:
                        if response.status == 200:
                            databox2 = await response.json()
                            data2 = databox2['data']

                            if not data2:
                                await ctx.send(f"**{arg.capitalize()} season for {arg2}**\n\n{string}")

                            else:
                                listdata2 = []

                                for length in range(0,len(data2)):
                                    listnumber += 1
                                    listdata2.append(f"{listnumber}. **{data2[length]['title']}** is airing on `{data2[length]['aired']['from'][:-15]}`\n") # title
                                string2 = ' '.join([str(item) for item in listdata2])

                                await ctx.send(f"**{arg.capitalize()} season for {arg2}**\n\n{string}")
                                await ctx.send(string2)

                        else:
                            await ctx.send(f"**{arg.capitalize()} season for {arg2}**\n\n{string}")
            else:
                await ctx.send("I can only retrieve .season <summer, fall, winter and spring> <year>")


def setup(bot):
    bot.add_cog(Season(bot))