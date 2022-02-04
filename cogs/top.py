import discord
import datetime

from aiohttp import request
from discord.ext import commands
from discord.ext.commands import MissingRequiredArgument


class Top(commands.Cog):

    def __init__(self, client):
        self.client = client
    description = "Gets the top from MyAnimeList"


    @commands.command(name='top')
    async def top(self, ctx, arg: str):
        '''Pulls the right data from MAL, checks the arguments needed to use the function correctly.
        '''
        if arg.lower() in ("anime", "manga", "characters", "people", "reviews"):
            URL = f"https://api.jikan.moe/v4/top/{arg.lower()}"
        else:
            await ctx.send("I can only retrieve .top <anime, manga, characters, people or reviews>")


        # Sents get request pulling the data
        async with request("GET", URL, headers={}) as response:
            if response.status == 200:
                databox = await response.json()
                data = databox["data"]


        # creates empty list
        title = data
        titlelist = [f'**Top 25 {arg.capitalize()} on MyAnimelist**\n\n']


		# gives the top 25 anime, this includes the rank, title and score
        if arg == "anime":

            for length in range(0, len(title)):
                titlelist.append(f"{title[length]['rank']}. **{title[length]['title']}** scored: `{title[length]['score']}`\n")
            string = ' '.join([str(item) for item in titlelist])

            await ctx.send(string)


		# gives the top 25 manga, this includes the rank, title and score
        elif arg == "manga":

            for length in range(0, len(title)):
                titlelist.append(f"{title[length]['rank']}. **{title[length]['title']}** scored: `{title[length]['scored']}`\n")
            string = ' '.join([str(item) for item in titlelist])

            await ctx.send(string)


		# gives the top 25 characters, this includes the name and amount of favorites
        elif arg == "characters":
            
            n = 1
            for length in range(0, len(title)):
                titlelist.append(f"{n}. **{title[length]['name']}** with `{title[length]['favorites']}` favorites\n")
                n += 1
            string = ' '.join([str(item) for item in titlelist])

            await ctx.send(string)


		# gives the top 25 anime, this includes the name and amount of favorites
        elif arg == "people":
            
            n = 1
            for length in range(0, len(title)):
                titlelist.append(f"{n}. **{title[length]['name']}** with `{title[length]['favorites']}` favorites\n")
                n += 1
            string = ' '.join([str(item) for item in titlelist])

            await ctx.send(string)


		# gives the top 10 anime, this includes the username, title, total score and amount of votes
        elif arg == "reviews":
            
            n = 1
            for length in range(0, len(title)):
                if n == 26:
                    continue
                else:
                    titlelist.append(f"{n}. **{title[length]['user']['username']}** - {title[length]['entry']['title']} a `{title[length]['scores']['overall']}` with `{title[length]['votes']}` helpful votes.\n")
                    n += 1
            string = ' '.join([str(item) for item in titlelist])

            await ctx.send(string)

        else:
            await ctx.send("Wow, dunno how you came here but tell me!")


    # if argument has been used wrong it triggers the MissingRequiredArgument below
    @top.error
    async def top_error(self,ctx,error):
        if isinstance(error,(MissingRequiredArgument)):
            if ctx.guild:
                await ctx.send('Woopsie! use .top <anime, manga, characters, people or reviews>')
            else:
        	    return


# adding cog to bot setup
def setup(bot):
    bot.add_cog(Top(bot))
