import discord
import datetime

from aiohttp import request
from discord.ext import commands
from discord.ext.commands import MissingRequiredArgument


class Random(commands.Cog):
    
	def __init__(self, client):
		self.client = client
	description = 'Randomized anime, manga, characters, people or users for fun!.'
    
	@commands.command(name='random')
	async def random(self, ctx, arg: str):
		'''Pulls the right data from MAL, checks the arguments needed to use the function correctly.
        '''
		if arg.lower() in ("anime", "manga", "characters", "people", "users"):
			URL = f"https://api.jikan.moe/v4/random/{arg.lower()}"
		else:
			await ctx.send('Woopsie! use .random <anime, manga, characters, people or users>')
			return None


        # Sents get request pulling the data
		async with request("GET", URL, headers={}) as response:
			if response.status == 200:
				databox = await response.json()
				data = databox['data']


				# sents a random user, includes: title, url, synopsis, image, score
				# popularity, members, dates, episodes, duration, genres and trailer
				if arg.lower() == "anime":

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
					embed.add_field(name="Genres", value=genres, inline=True)
					embed.add_field(name="Trailer", value=data["trailer"]["url"], inline=True)
					embed.set_footer(text="Requested by: {}".format(ctx.author.display_name), icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
					embed.timestamp = datetime.datetime.utcnow()

					await ctx.send(embed=embed)


				# sents a random user, includes: title, url, synopsis, image, score
				# popularity, members, volumes, chapters, published date and genres
				elif arg.lower() == "manga":

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
					embed.add_field(name="Genres", value=genres, inline=True)
					embed.set_footer(text="Requested by: {}".format(ctx.author.display_name), icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
					embed.timestamp = datetime.datetime.utcnow()

					await ctx.send(embed=embed)


				# sents a random character, includes: name, url, about and amount of favorites by users
				elif arg.lower() == "characters":

					embed = discord.Embed(title=data["name"], url=data["url"], description=data["about"], color=0x87CEEB)
					embed.set_thumbnail(url=data["images"]['jpg']['image_url'])
					embed.add_field(name="Favorites", value=data["favorites"], inline=True)
					embed.set_footer(text="Requested by: {}".format(ctx.author.display_name), icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
					embed.timestamp = datetime.datetime.utcnow()

					await ctx.send(embed=embed)


				# sents a random person, includes: name, url, about, image, members, birhtday
				# given name, family name and their website
				elif arg.lower() == "people":

					embed = discord.Embed(title=data["name"], url=data["url"], description=data["about"], color=0x87CEEB)
					embed.set_thumbnail(url=data["images"]['jpg']['image_url'])
					embed.add_field(name='Members',value=data['favorites'], inline= True)

					if data['birthday'] is None:
						embed.add_field(name="Birthday", value='Unknown', inline=True)
					else:
						embed.add_field(name='Birthday',value=data['birthday'][:-15], inline= True)

					embed.add_field(name='Given name',value=data['given_name'], inline= True)
					embed.add_field(name='Family name',value=data['family_name'], inline= True)
					embed.add_field(name='Website',value=data['website_url'], inline= True)
					embed.set_footer(text="Requested by: {}".format(ctx.author.display_name), icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
					embed.timestamp = datetime.datetime.utcnow()

					await ctx.send(embed=embed)


				# sents a random user, includes: username, url, image, last online, gender
				# birthday, location and join date.
				elif arg.lower() == "users":

					embed = discord.Embed(title=data["username"], url=data["url"], color=0x87CEEB)
					embed.set_thumbnail(url=data["images"]['jpg']['image_url'])
					embed.add_field(name='Last online',value=data['last_online'][:-15], inline=True)
					embed.add_field(name='Gender',value=data['gender'], inline=True)

					if data['birthday'] is None:
						embed.add_field(name="Birthday", value='Unknown', inline=True)
					else:
						embed.add_field(name='Birthday',value=data['birthday'][:-15], inline=True)
					if data['location'] is None:
						embed.add_field(name="Location", value='Unknown', inline=True)
					else:
						embed.add_field(name='Location',value=data['location'], inline=True)

					embed.add_field(name='Joined',value=data['joined'][:-15], inline=True)
					embed.set_footer(text="Requested by: {}".format(ctx.author.display_name), icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
					embed.timestamp = datetime.datetime.utcnow()

					await ctx.send(embed=embed)


				else:
					await ctx.send(f"This command is still in work.")
			else:
				await ctx.send(f"API returned a {response.status} status and is currently not usable.")

	# if argument has been used wrong it triggers the MissingRequiredArgument below
	@random.error
	async def random_error(self,ctx,error):
			if isinstance(error,(MissingRequiredArgument)):
				if ctx.guild:
					await ctx.send('Woopsie! use .random <anime, manga, characters, people or users>')
				else:
					return


# adding cog to bot setup
def setup(bot):
	bot.add_cog(Random(bot))