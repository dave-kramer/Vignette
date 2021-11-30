import discord
import datetime
import asyncio

from aiohttp import request
from discord.ext import commands
from discord.ext.commands import MissingRequiredArgument


class User(commands.Cog):
    
	def __init__(self, client):
		self.client = client
	description = "Check user's MAL about, clubs, favorites, friends, history, recommendations, reviews, statistics and userupdates!"
    
	@commands.command(name='user')
	async def user(self, ctx, name: str, arg=None, arg2=None):
            '''Pulls the right data from MAL, checks the arguments needed to use the function correctly.
            '''
            check = ("about", "statistics", "favorites", "history", "userupdates", "friends", "reviews", "recommendations", "clubs")
            if arg is None:
                URL = f"https://api.jikan.moe/v4/users/{name}"
            else:
                if arg in check:
                    if arg2 is None:
                        URL = f"https://api.jikan.moe/v4/users/{name}/{arg.lower()}"
                    elif arg2 == "anime" or "manga":
                        URL = f"https://api.jikan.moe/v4/users/{name}/{arg.lower()}/{arg2}"
                    else:
                        await ctx.send(f"I'm not sure what you did, but you've done it wrong!")
                        return None


            # Sents get request pulling the data
            async with request("GET", URL, headers={}) as response:
                if response.status == 200:
                    databox = await response.json()
                    data = databox['data']


                    # to remember name and creates direct profile url
                    titleName = name
                    titleURL = f"https://myanimelist.net/profile/{name}"


                    # creates embed for searched user includes owner of vignette
                    # username, url, description, image, joindate, gender, birthday, location and last online
                    if arg is None:
                        if name == "davekramer":
                            embed = discord.Embed(title=data["username"], url=data["url"],description="The creator of Vignette says Hi, hope you're liking the bot, dont forget to comment on my MAL or get more info about Vignette on https://davekramer.nl", color=0x800000)
                            embed.set_thumbnail(url=data["images"]['jpg']['image_url'])
                            embed.add_field(name='Joined',value=data['joined'][:-15], inline= True)
                            embed.add_field(name='Gender',value=data['gender'], inline= True)

                            if data['birthday'] is None:
                                embed.add_field(name="Birthday", value='Unknown', inline=True)
                            else:
                                embed.add_field(name='Birthday',value=data['birthday'][:-15], inline= True)
                            if data['location'] is None:
                                embed.add_field(name="Location", value='Unknown', inline=True)
                            else:
                                embed.add_field(name='Location',value=data['location'], inline= True)

                            embed.add_field(name='Last online',value=data['last_online'][:-15], inline= True)
                            embed.set_image(url="https://i.pinimg.com/originals/6f/45/86/6f45868016994a389ebdb0170bd91287.gif")
                            embed.set_footer(text="Thank you {},".format(ctx.author.display_name), icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
                            embed.timestamp = datetime.datetime.utcnow()

                        else:
                            embed = discord.Embed(title=data["username"], url=data["url"], color=0x87CEEB)
                            if data["images"]['jpg']['image_url'] is None:
                                embed.set_thumbnail(url="https://media.tenor.com/images/9f2cd5e5d080e5e8519893d0c0d2f3bd/tenor.gif")
                            else:
                                embed.set_thumbnail(url=data["images"]['jpg']['image_url'])
                            embed.add_field(name='Joined',value=data['joined'][:-15], inline= True)
                            embed.add_field(name='Gender',value=data['gender'], inline= True)

                            if data['birthday'] is None:
                                embed.add_field(name="Birthday", value='Unknown', inline=True)
                            else:
                                embed.add_field(name='Birthday',value=data['birthday'][:-15], inline= True)
                            if data['location'] is None:
                                embed.add_field(name="Location", value='Unknown', inline=True)
                            else:
                                embed.add_field(name='Location',value=data['location'], inline= True)

                            embed.add_field(name='Last online',value=data['last_online'][:-15], inline= True)
                            embed.set_footer(text="Requested by: {}".format(ctx.author.display_name), icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
                            embed.timestamp = datetime.datetime.utcnow()


                    # creates embed for user's about page
                    # includes user name, url and description (custom if empty)
                    # also if about is too long it cuts to 1900 length
                    elif arg == "about":
                        if data["about"] is None:
                                embed = discord.Embed(title=titleName, url=titleURL, description="User's  about page is empty.", color=0x87CEEB)
                                embed.set_footer(text="Requested by: {}".format(ctx.author.display_name), icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
                                embed.timestamp = datetime.datetime.utcnow()
                        else:
                            if len(data["about"])>2000:
                                message = await ctx.send("Oh no too much to handle, hang on I'll create a short summary.")
                                data["about"]= data["about"][:1900]
                                await asyncio.sleep(6)
                                embed = discord.Embed(title=titleName, url=titleURL, description=data["about"], color=0x87CEEB)
                                embed.set_footer(text="Requested by: {}".format(ctx.author.display_name), icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
                                embed.timestamp = datetime.datetime.utcnow()
                                await message.delete()

                            else:
                                embed = discord.Embed(title=titleName, url=titleURL, description=data["about"], color=0x87CEEB)
                                embed.set_footer(text="Requested by: {}".format(ctx.author.display_name), icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
                                embed.timestamp = datetime.datetime.utcnow()
                            

                    # creates embed for users anime and mangastatistics
                    # embed for anime includes days watched, mean score, completed, watching, on hold, dropped, plan to watch, total anime
                    # embed for mang includes days read, mean score, completed, reading, on hold, dropped, plan to read, total manga, reread, chapters read, volumes read
                    elif arg == "statistics":

                        embed = discord.Embed(title=titleName + " Anime Statistics", url=titleURL, color=0x87CEEB)
                        embed.add_field(name='Days watched',value=data['anime']['days_watched'], inline= True)
                        embed.add_field(name='Mean score',value=data['anime']['mean_score'], inline= True)
                        embed.add_field(name='Completed',value=data['anime']['completed'], inline= True)
                        embed.add_field(name='Watching',value=data['anime']['watching'], inline= True)
                        embed.add_field(name='On hold',value=data['anime']['on_hold'], inline= True)
                        embed.add_field(name='Dropped',value=data['anime']['dropped'], inline= True)
                        embed.add_field(name='Plan to watch',value=data['anime']['plan_to_watch'], inline= True)
                        embed.add_field(name='Total anime',value=data['anime']['total_entries'], inline= True)
                        embed.add_field(name='Rewatched',value=data['anime']['rewatched'], inline= True)
                        embed.add_field(name='Total episodes',value=data['anime']['episodes_watched'], inline= True)
                        embed.set_footer(text="Requested by: {}".format(ctx.author.display_name), icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
                        embed.timestamp = datetime.datetime.utcnow()
                        await ctx.send(embed=embed)

                        embed = discord.Embed(title=titleName + " Manga Statistics", url=titleURL, color=0x87CEEB)
                        embed.add_field(name='Days read',value=data['manga']['days_read'], inline= True)
                        embed.add_field(name='Mean score',value=data['manga']['mean_score'], inline= True)
                        embed.add_field(name='Completed',value=data['manga']['completed'], inline= True)
                        embed.add_field(name='Reading',value=data['manga']['reading'], inline= True)
                        embed.add_field(name='On hold',value=data['manga']['on_hold'], inline= True)
                        embed.add_field(name='Dropped',value=data['manga']['dropped'], inline= True)
                        embed.add_field(name='Plan to read',value=data['manga']['plan_to_read'], inline= True)
                        embed.add_field(name='Total manga',value=data['manga']['total_entries'], inline= True)
                        embed.add_field(name='Reread',value=data['manga']['reread'], inline= True)
                        embed.add_field(name='Chapters read',value=data['manga']['chapters_read'], inline= True)
                        embed.add_field(name='Volumes read',value=data['manga']['volumes_read'], inline= True)
                        embed.set_footer(text="Requested by: {}".format(ctx.author.display_name), icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
                        embed.timestamp = datetime.datetime.utcnow()


                    # creates embed for users favorites
                    # loops through anime, manga, characters and favorites
                    elif arg == "favorites":
                        embed = discord.Embed(title=titleName + "'s Favorites", url=titleURL, color=0x87CEEB)
                        titles = []
                        for length in range(0,len(data['anime'])):
                            titles.append(data['anime'][length]['title'])
                        string = '\n'.join([str(item) for item in titles])
                        data['anime'] = string
                        if not titles:
                            pass
                        else:
                            embed.add_field(name="Anime", value=data['anime'], inline=True)

                        mtitles = []
                        for length in range(0,len(data['manga'])):
                            mtitles.append(data['manga'][length]['title'])
                        string = '\n'.join([str(item) for item in mtitles])
                        data['manga'] = string
                        if not mtitles:
                            pass
                        else:
                            embed.add_field(name="Manga", value=data['manga'], inline=True)

                        chars = []
                        for length in range(0,len(data['characters'])):
                            chars.append(data['characters'][length]['name'])
                        string = '\n'.join([str(item) for item in chars])
                        data['characters'] = string
                        if not chars:
                            pass
                        else:
                            embed.add_field(name="Characters", value=data['characters'], inline=True)

                        ppl = []
                        for length in range(0,len(data['people'])):
                            ppl.append(data['people'][length]['name'])
                        string = '\n'.join([str(item) for item in ppl])
                        data['people'] = string
                        if not ppl:
                            pass
                        else:
                            embed.add_field(name="People", value=data['people'], inline=False)
                                
                        embed.set_footer(text="Requested by: {}".format(ctx.author.display_name), icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
                        embed.timestamp = datetime.datetime.utcnow()


                    # placeholder
                    elif arg == "userupdates":
                            
                        embed = discord.Embed(title="Vignette", url="https://github.com/dave-kramer/vignette", description="Woopsie! I'm still working on this command, give me some time!", color=0x87CEEB)
                        embed.set_image(url="https://i.pinimg.com/originals/9f/20/76/9f2076c3c2eff838420384629496466e.gif")
                        embed.set_footer(text="Requested by: {}".format(ctx.author.display_name), icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
                        embed.timestamp = datetime.datetime.utcnow()


                    # placeholder
                    elif arg == "history":

                        if arg2 == "anime":

                            embed = discord.Embed(title="Vignette", url="https://github.com/dave-kramer/vignette", description="Woopsie! I'm still working on this command, give me some time!", color=0x87CEEB)
                            embed.set_image(url="https://i.pinimg.com/originals/9f/20/76/9f2076c3c2eff838420384629496466e.gif")
                            embed.set_footer(text="Requested by: {}".format(ctx.author.display_name), icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
                            embed.timestamp = datetime.datetime.utcnow()

                        if arg2 == "manga":
                            
                            embed = discord.Embed(title="Vignette", url="https://github.com/dave-kramer/vignette", description="Woopsie! I'm still working on this command, give me some time!", color=0x87CEEB)
                            embed.set_image(url="https://i.pinimg.com/originals/9f/20/76/9f2076c3c2eff838420384629496466e.gif")
                            embed.set_footer(text="Requested by: {}".format(ctx.author.display_name), icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
                            embed.timestamp = datetime.datetime.utcnow()
                            

                    # placeholder
                    elif arg == "friends":
                            
                        embed = discord.Embed(title="Vignette", url="https://github.com/dave-kramer/vignette", description="Woopsie! I'm still working on this command, give me some time!", color=0x87CEEB)
                        embed.set_image(url="https://i.pinimg.com/originals/9f/20/76/9f2076c3c2eff838420384629496466e.gif")
                        embed.set_footer(text="Requested by: {}".format(ctx.author.display_name), icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
                        embed.timestamp = datetime.datetime.utcnow()


                    # placeholder
                    elif arg == "reviews":

                        embed = discord.Embed(title="Vignette", url="https://github.com/dave-kramer/vignette", description="Woopsie! I'm still working on this command, give me some time!", color=0x87CEEB)
                        embed.set_image(url="https://i.pinimg.com/originals/9f/20/76/9f2076c3c2eff838420384629496466e.gif")
                        embed.set_footer(text="Requested by: {}".format(ctx.author.display_name), icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
                        embed.timestamp = datetime.datetime.utcnow()


                    # placeholder
                    elif arg == "recommendations":

                        embed = discord.Embed(title="Vignette", url="https://github.com/dave-kramer/vignette", description="Woopsie! I'm still working on this command, give me some time!", color=0x87CEEB)
                        embed.set_image(url="https://i.pinimg.com/originals/9f/20/76/9f2076c3c2eff838420384629496466e.gif")
                        embed.set_footer(text="Requested by: {}".format(ctx.author.display_name), icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
                        embed.timestamp = datetime.datetime.utcnow()


                    # placeholder
                    elif arg == "clubs":

                        embed = discord.Embed(title="Vignette", url="https://github.com/dave-kramer/vignette", description="Woopsie! I'm still working on this command, give me some time!", color=0x87CEEB)
                        embed.set_image(url="https://i.pinimg.com/originals/9f/20/76/9f2076c3c2eff838420384629496466e.gif")
                        embed.set_footer(text="Requested by: {}".format(ctx.author.display_name), icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
                        embed.timestamp = datetime.datetime.utcnow()

                    await ctx.send(embed=embed)


                # sent an embed when typing in a username that doesn't exist
                else:

                    embed = discord.Embed(description="Woopsie! That user couldn't be found, try again :)", color=0x87CEEB)
                    embed.set_author(name="Vignette", url="https://github.com/dave-kramer/vignette", icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
                    embed.set_image(url="https://i.pinimg.com/originals/9f/20/76/9f2076c3c2eff838420384629496466e.gif")
                    embed.set_footer(text="Requested by: {}".format(ctx.author.display_name), icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
                    embed.timestamp = datetime.datetime.utcnow()
                    
                    await ctx.send(embed=embed)


	# if argument has been used wrong it triggers the MissingRequiredArgument below
	@user.error
	async def user_error(self,ctx,error):
		if isinstance(error,(MissingRequiredArgument)):
			if ctx.guild:
				await ctx.send('To use this command do as following: .user <argument> <argument>')
			else:
				return


# adding cog to bot setup
def setup(bot):
	bot.add_cog(User(bot))