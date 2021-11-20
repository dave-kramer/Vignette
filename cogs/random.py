import discord
import datetime

from aiohttp import request
from discord.ext import commands
from discord.ext.commands import MissingRequiredArgument


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
					#print(data)


					if randomizer.lower() == "anime":

						embed = discord.Embed(title=data["title"], url=data["url"], description=data["synopsis"], color=0x87CEEB)
						embed.set_thumbnail(url=data["images"]['jpg']['image_url'])
						embed.add_field(name="Score", value=data["score"], inline=True)
						embed.add_field(name="Popularity", value=data["popularity"], inline=True)
						embed.add_field(name="Members", value=data["members"], inline=True)

						if data["aired"]["from"] is None:
							embed.add_field(name="Start Date", value='Unknown', inline=True)
						else:
							embed.add_field(name="Start Date", value=data["aired"]["from"][:-15], inline=True)
						if data["aired"]["to"] is None:
							embed.add_field(name="End Date", value="Unknown", inline=True)
						else:
							embed.add_field(name="End Date", value=data["aired"]["to"][:-15], inline=True)

						embed.add_field(name="Episodes", value=data["episodes"], inline=True)
						embed.add_field(name="Duration", value=data["duration"], inline=True)
						genre = data['genres']
						c = []
						
						for length in range(0,len(genre)):
							c.append(genre[length]['name'])
						
						string = ', '.join([str(item) for item in c])
						genres = string
						embed.add_field(name="Genres", value=genres, inline=False)
						embed.add_field(name="Trailer", value=data["trailer"]["url"], inline=True)
						embed.set_footer(text="Requested by: {}".format(ctx.author.display_name), icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
						embed.timestamp = datetime.datetime.utcnow()

						await ctx.send(embed=embed)


					elif randomizer.lower() == "manga":

						embed = discord.Embed(title=data["title"], url=data["url"], description=data["synopsis"], color=0x87CEEB)
						embed.set_thumbnail(url=data["images"]['jpg']['image_url'])
						embed.add_field(name="Score", value=data["scored"], inline=True)
						embed.add_field(name="Rank", value=data["rank"], inline=True)
						embed.add_field(name="Popularity", value=data["popularity"], inline=True)
						embed.add_field(name="Members", value=data["members"], inline=True)
						embed.add_field(name="Volumes", value=data["volumes"], inline=True)
						embed.add_field(name="Chapters", value=data["chapters"], inline=True)

						if data["published"]["from"] is None:
							embed.add_field(name="Published from", value='Unknown', inline=True)
						else:
							embed.add_field(name="Published from", value=data["published"]["from"][:-15], inline=True)
						if data["published"]["to"] is None:
							embed.add_field(name="Published to", value="Unknown", inline=True)
						else:
							embed.add_field(name="Published to", value=data["published"]["to"][:-15], inline=True)
						genre = data['genres']
						c = []
						
						for length in range(0,len(genre)):
							c.append(genre[length]['name'])
						
						string = ', '.join([str(item) for item in c])
						genres = string
						embed.add_field(name="Genres", value=genres, inline=False)
						embed.set_footer(text="Requested by: {}".format(ctx.author.display_name), icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
						embed.timestamp = datetime.datetime.utcnow()

						await ctx.send(embed=embed)


					elif randomizer.lower() == "characters":

						embed = discord.Embed(title=data["name"], url=data["url"], description=data["about"], color=0x87CEEB)
						embed.set_thumbnail(url=data["images"]['jpg']['image_url'])
						embed.add_field(name="Favorites", value=data["favorites"], inline=True)
						embed.set_footer(text="Requested by: {}".format(ctx.author.display_name), icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
						embed.timestamp = datetime.datetime.utcnow()

						await ctx.send(embed=embed)


					elif randomizer.lower() == "people":

						embed = discord.Embed(title=data["name"], url=data["url"], description=data["about"], color=0x87CEEB)
						embed.set_thumbnail(url=data["images"]['jpg']['image_url'])
						embed.add_field(name='Members',value=data['favorites'], inline= False)

						if data['birthday'] is None:
							embed.add_field(name="Birthday", value='Unknown', inline=True)
						else:
							embed.add_field(name='Birthday',value=data['birthday'][:-15], inline= False)

						embed.add_field(name='Given name',value=data['given_name'], inline= False)
						embed.add_field(name='Family name',value=data['family_name'], inline= False)
						embed.add_field(name='Website',value=data['website_url'], inline= False)
						embed.set_footer(text="Requested by: {}".format(ctx.author.display_name), icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
						embed.timestamp = datetime.datetime.utcnow()

						await ctx.send(embed=embed)


					elif randomizer.lower() == "users":

						embed = discord.Embed(title=data["username"], url=data["url"], color=0x87CEEB)
						embed.set_thumbnail(url=data["images"]['jpg']['image_url'])
						embed.add_field(name='Last online',value=data['last_online'][:-15], inline= False)
						embed.add_field(name='Gender',value=data['gender'], inline= False)

						if data['birthday'] is None:
							embed.add_field(name="Birthday", value='Unknown', inline=True)
						else:
							embed.add_field(name='Birthday',value=data['birthday'][:-15], inline= False)
						if data['location'] is None:
							embed.add_field(name="Location", value='Unknown', inline=True)
						else:
							embed.add_field(name='Location',value=data['location'], inline= False)

						embed.add_field(name='Joined',value=data['joined'][:-15], inline= False)
						embed.set_footer(text="Requested by: {}".format(ctx.author.display_name), icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
						embed.timestamp = datetime.datetime.utcnow()

						await ctx.send(embed=embed)


					else:
						await ctx.send(f"This command is still in work.")
				else:
					await ctx.send(f"API returned a {response.status} status and is currently not usable.")
		else:
			await ctx.send("You're only allowed to randomize anime, manga, characters, people and users.")


def setup(bot):
	bot.add_cog(Random(bot))