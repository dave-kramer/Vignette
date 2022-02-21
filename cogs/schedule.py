import discord
import datetime

from datetime import datetime as date
from aiohttp import request
from discord.ext import commands
from discord.ext.commands import MissingRequiredArgument


class Schedule(commands.Cog):

    def __init__(self, client):
        self.client = client
    description = "Gets the schedule from MyAnimeList"


    @commands.command(name='schedule')
    async def schedule(self, ctx, arg: str):
        '''Pulls the right data from MAL, checks the arguments needed to use the function correctly.
        '''
        if arg.lower() in ("monday", "tuesday", "thursday", "friday", "saturday", "sunday"):
            URL = f"https://api.jikan.moe/v4/schedules/{arg.lower()}"
        elif arg.lower() == "today":
            arg = date.today().strftime("%A")
            URL = f"https://api.jikan.moe/v4/schedules/{arg}"
        else:
            await ctx.send("I can only retrieve .schedule <today> **or** <monday - sunday>")


        # Sents get request pulling the data
        async with request("GET", URL, headers={}) as response:
            if response.status == 200:
                databox = await response.json()
                data = databox['data']

            titleURL = f"https://myanimelist.net/anime/season/schedule"
            listdata = []
            embed = discord.Embed(title=f"Anime schedule for " + f"{arg.lower().title()}", description="NOTE: timezone is ALWAYS Asia/Tokyo", url=titleURL, color=0x87CEEB)
            for length in range(0,len(data)):
                if data[length]['broadcast']['time'] is None:
                    continue
                else:
                    embed.add_field(name=data[length]['title'], value=data[length]['broadcast']['time'], inline=False)
            string = '*'.join([str(item) for item in listdata])
            x = string.split("*")
            #print(x)
            embed.set_footer(text="Requested by: {}".format(ctx.author.display_name), icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
            embed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=embed)

    # if argument has been used wrong it triggers the MissingRequiredArgument below
    @schedule.error
    async def random_error(self,ctx,error):
            if isinstance(error,(MissingRequiredArgument)):
                if ctx.guild:
                    await ctx.send('Woopsie! use .schedule <today> **or** <monday - sunday>')
                else:
                    return


# adding cog to bot setup
def setup(bot):
	bot.add_cog(Schedule(bot))