import discord
import datetime

from aiohttp import request
from discord.ext import commands
from discord.ext.commands import MissingRequiredArgument


class Recommendations(commands.Cog):
    
	def __init__(self, client):
		self.client = client
	description = "Gets the recommendations from MyAnimeList"

	@commands.command(name='recommendations')
	async def recommendations(self, ctx, arg: str):
		if arg.lower() in ("anime", "manga"):
			URL = f"https://api.jikan.moe/v4/recommendations/{arg.lower()}"
		else:
			await ctx.send("To use this command do as following: .recommendations <anime> or <manga> - I don't support other recommendations")

		async with request("GET", URL, headers={}) as response:
			if response.status == 200:
				databox = await response.json()
				data = databox['data']
				#print(data)


				if arg.lower() == "anime":

					embed = discord.Embed(title="Anime Recommendations", url="https://myanimelist.net/recommendations.php?s=recentrecs&t=anime", description="Currently only holds the link to the anime recommendations, I'll be adding this fuction later.", color=0x87CEEB)
					embed.set_image(url="https://64.media.tumblr.com/b30b76d4c326e588b73ddc273fc201ea/tumblr_oltergOh6u1sej1ryo1_250.gifv")
					embed.set_footer(text="Requested by: {}".format(ctx.author.display_name), icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
					embed.timestamp = datetime.datetime.utcnow()

				elif arg.lower() == "manga":

					embed = discord.Embed(title="Manga Recommendations", url="https://myanimelist.net/recommendations.php?s=recentrecs&t=manga", description="Currently only holds the link to the manga recommendations, I'll be adding this fuction later.", color=0x87CEEB)
					embed.set_image(url="https://64.media.tumblr.com/b30b76d4c326e588b73ddc273fc201ea/tumblr_oltergOh6u1sej1ryo1_250.gifv")
					embed.set_footer(text="Requested by: {}".format(ctx.author.display_name), icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
					embed.timestamp = datetime.datetime.utcnow()

				else:
					await ctx.send('To use this command do as following: .recommendations <argument>')
					
				await ctx.send(embed=embed)


	@recommendations.error
	async def recommendation_error(self,ctx,error):
		if isinstance(error,(MissingRequiredArgument)):
			if ctx.guild:
				await ctx.send('To use this command do as following: .recommendations <anime or manga>')
			else:
				return

def setup(bot):
    bot.add_cog(Recommendations(bot))