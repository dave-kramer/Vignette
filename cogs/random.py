import discord

from aiohttp import request
from discord.ext import commands


class Random(commands.Cog):
    
	def __init__(self, client):
		self.client = client
	description = 'Get information about an user through MyAnimeList.'
    
	@commands.command(name='random')
	async def random(self, ctx, randomizer: str):
		if randomizer.lower() in ("anime", "manga", "characters", "people", "users"):
			URL = f"https://api.jikan.moe/v4/random/{randomizer.lower()}"

			async with request("GET", URL, headers={}) as response:
				if response.status == 200:
					databox = await response.json()
					data = databox['data']
					print(data)

					embed = discord.Embed(title=data["title"], url=data["url"], description=data["synopsis"], color=0xf37a12)
					embed.set_thumbnail(url=data["images"]['jpg']['image_url'])
					embed.add_field(name="Score", value=data["score"], inline=True)
					embed.add_field(name="Popularity", value=data["popularity"], inline=True)
					embed.add_field(name="Members", value=data["members"], inline=True)
					embed.add_field(name="Duration", value=data["duration"], inline=True)
					embed.add_field(name="Episodes", value=data["episodes"], inline=True)

					await ctx.send(embed=embed)
				else:
					await ctx.send(f"API returned a {response.status} status.")

		else:
			await ctx.send("You can't use the command like that.")

def setup(bot):
	bot.add_cog(Random(bot))