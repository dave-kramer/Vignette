import discord

from discord.ext import commands
from discord_components import Button


class Info(commands.Cog):

    def __init__(self, client):
        self.client = client
    description = "More information about Vignette"

    @commands.command(name='info')
    async def info(self, ctx):
        
        story = ("At the time of making this I'm a beginner programmer, as you could see from the source code, its not too shabby.\nI'm happy with the result, currently you're able to get anime, manga, users, people, characters & more info.\nYou're able to get the daily schedule, see whats announcing this season, see the top on MAL and most important I managed to create a working anime airing notifier function.\nThanks to Jikan, trace.moe, anichan, waifu.pics as most of it wouldn't be possible without their API's.\nAlso **not** to forget, if you're using Vignette now, you definitely have `great taste`.")
        button_website = Button(label="Website", style=5, url='https://davekramer.nl')
        button_github = Button(label="GitHub", style=5, url='https://github.com/dave-kramer/vignette')

        await ctx.send(f"{story}", components = [[button_website, button_github]])


def setup(bot):
    bot.add_cog(Info(bot))