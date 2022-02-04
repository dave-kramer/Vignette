import discord
import datetime
import random

from aiohttp import request
from discord.ext import commands
from discord.ext.commands import MissingRequiredArgument


class Recommendation(commands.Cog):
    
	def __init__(self, client):
		self.client = client
	description = "Gets a anime or manga recommendation from MyAnimeList"

	@commands.command(name='recommendation')
	async def recommendation(self, ctx, arg: str):
		'''Pulls one random anime or manga recommendation from MyAnimeList
		'''
		if arg.lower() in ("anime", "manga"):
			URL = f"https://api.jikan.moe/v4/recommendations/{arg.lower()}"
		else:
			await ctx.send("To use this command do as following: .recommendations <anime> or <manga> - I don't support other recommendations")

		async with request("GET", URL, headers={}) as response:
			if response.status == 200:
				databox = await response.json()
				data = databox['data']

				i = random.randint(0, 99)

				if arg.lower() == "anime":

					embed = discord.Embed(title="Anime Recommendation", url=f"https://myanimelist.net/profile/{data[i]['user']['username']}/recommendations",  color=0x87CEEB)
					
					embed.add_field(name=f"According to {data[i]['user']['username']}", value=f"If you liked [{data[i]['entry'][0]['title']}]({data[i]['entry'][0]['url']}) you should try [{data[i]['entry'][1]['title']}]({data[i]['entry'][1]['url']})\n\n_{data[i]['content']}_", inline=False)
					
					embed.set_thumbnail(url=data[i]['entry'][0]['images']['jpg']['image_url'])
					embed.set_image(url=data[i]['entry'][1]['images']['jpg']['image_url'])
					embed.set_footer(text="Requested by: {}".format(ctx.author.display_name), icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
					embed.timestamp = datetime.datetime.utcnow()

					await ctx.send(embed=embed)

				elif arg.lower() == "manga":

					embed = discord.Embed(title="Manga Recommendation", url=f"https://myanimelist.net/profile/{data[i]['user']['username']}/recommendations",  color=0x87CEEB)
					
					embed.add_field(name=f"According to {data[i]['user']['username']}", value=f"If you liked [{data[i]['entry'][0]['title']}]({data[i]['entry'][0]['url']}) you should try [{data[i]['entry'][1]['title']}]({data[i]['entry'][1]['url']})\n\n_{data[i]['content']}_", inline=False)
					
					embed.set_thumbnail(url=data[i]['entry'][0]['images']['jpg']['image_url'])
					embed.set_image(url=data[i]['entry'][1]['images']['jpg']['image_url'])
					embed.set_footer(text="Requested by: {}".format(ctx.author.display_name), icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
					embed.timestamp = datetime.datetime.utcnow()
					
					await ctx.send(embed=embed)

				else:
					await ctx.send('To use this command do as following: .recommendations <anime or manga>')


	@recommendation.error
	async def recommendation_error(self,ctx,error):
		if isinstance(error,(MissingRequiredArgument)):
			if ctx.guild:
				await ctx.send('To use this command do as following: .recommendations <anime or manga>')
			else:
				return


def setup(bot):
    bot.add_cog(Recommendation(bot))