import discord
import datetime
import asyncio

from aiohttp import request
from discord.ext import commands
from discord_components import Button, ButtonStyle


class User(commands.Cog):
    
    def __init__(self, client):
        self.client = client
    description = "Check user's MAL about, clubs, favorites, friends, history, recommendations, reviews, statistics and userupdates!"
    
    @commands.command(name='user')
    async def usert(self, ctx, arg=None):

        URL = f"https://api.jikan.moe/v4/users/{arg}"
        titleURL = f"https://myanimelist.net/profile/{arg}"

        async with request("GET", URL, headers={}) as response:
            if response.status == 200:
                databox_pull = await response.json()
                data_pull = databox_pull['data']

                button_about = Button(label=f"About", style=ButtonStyle.green, custom_id="about")
                button_statistics = Button(label=f"Statistics", style=ButtonStyle.green, custom_id="statistics")
                button_favorites = Button(label=f"History", style=ButtonStyle.green, custom_id="history")
                button_updates = Button(label=f"Updates", style=ButtonStyle.green, custom_id="updates")
                button_friends = Button(label=f"Friends", style=ButtonStyle.green, custom_id="friends")
                button_reviews = Button(label=f"Reviews", style=ButtonStyle.green, custom_id="reviews")
                button_recommendations = Button(label=f"Recommendations", style=ButtonStyle.green, custom_id="recommendations")
                button_clubs = Button(label=f"Clubs", style=ButtonStyle.green, custom_id="clubs")

                if arg == "davekramer":

                    embed = discord.Embed(title=data_pull["username"], url=data_pull["url"],description="The creator of Vignette says Hi, hope you're liking the bot, dont forget to comment on my MAL or get more info about Vignette on https://davekramer.nl", color=0x800000)
                    embed.set_thumbnail(url=data_pull["images"]['jpg']['image_url'])
                    embed.add_field(name='Joined',value=data_pull['joined'][:-15], inline= True)
                    embed.add_field(name='Gender',value=data_pull['gender'], inline= True)
                    if data_pull['birthday'] is None:
                        embed.add_field(name="Birthday", value='Unknown', inline=True)
                    else:
                        embed.add_field(name='Birthday',value=data_pull['birthday'][:-15], inline= True)
                    embed.add_field(name='Location',value=data_pull['location'], inline= True)
                    embed.add_field(name='Last online',value=data_pull['last_online'][:-15], inline= True)
                    embed.set_image(url="https://i.pinimg.com/originals/6f/45/86/6f45868016994a389ebdb0170bd91287.gif")
                    embed.set_footer(text="Thank you {}".format(ctx.author.display_name), icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")

                else:

                    embed = discord.Embed(title=data_pull["username"], url=data_pull["url"], color=0x87CEEB)
                    if data_pull["images"]['jpg']['image_url'] is None:
                        embed.set_thumbnail(url="https://media.tenor.com/images/9f2cd5e5d080e5e8519893d0c0d2f3bd/tenor.gif")
                    else:
                        embed.set_thumbnail(url=data_pull["images"]['jpg']['image_url'])
                    embed.add_field(name='Joined',value=data_pull['joined'][:-15], inline= True)
                    embed.add_field(name='Gender',value=data_pull['gender'], inline= True)
                    if data_pull['birthday'] is None:
                        embed.add_field(name="Birthday", value='Unknown', inline=True)
                    else:
                        embed.add_field(name='Birthday',value=data_pull['birthday'][:-15], inline= True)
                    if data_pull['location'] is None:
                        embed.add_field(name="Location", value='Unknown', inline=True)
                    else:
                        embed.add_field(name='Location',value=data_pull['location'], inline= True)
                    embed.add_field(name='Last online',value=data_pull['last_online'][:-15], inline= True)
                    embed.set_footer(text="Requested by: {}".format(ctx.author.display_name), icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")

                msg = await ctx.send(embed=embed, components = [[button_about, button_statistics, button_favorites, button_updates],[button_friends, button_reviews, button_recommendations, button_clubs]])
                interaction = await self.client.wait_for("button_click")

                URL = f"https://api.jikan.moe/v4/users/{arg}/{interaction.custom_id}"

                async with request("GET", URL, headers={}) as response:
                    if response.status == 200:
                        databox = await response.json()
                        data = databox['data']

                if interaction.custom_id == "about":
                    if data["about"] is None:
                            embed = discord.Embed(title=arg, url=titleURL, description="User's  about page is empty.", color=0x87CEEB)
                            embed.set_footer(text="Requested by: {}".format(ctx.author.display_name), icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
                            embed.timestamp = datetime.datetime.utcnow()
                            await msg.edit(embed=embed, components=[])
                    else:
                        if len(data["about"])>2000:
                            message = await ctx.send("Oh no too much to handle, hang on I'll create a short summary.")
                            data["about"]= data["about"][:1900]
                            await asyncio.sleep(6)
                            embed = discord.Embed(title=arg, url=titleURL, description=data["about"], color=0x87CEEB)
                            embed.set_footer(text="Requested by: {}".format(ctx.author.display_name), icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
                            embed.timestamp = datetime.datetime.utcnow()
                            await msg.edit(embed=embed, components=[])
                            await message.delete()
                        else:
                            embed = discord.Embed(title=arg, url=titleURL, description=data["about"], color=0x87CEEB)
                            embed.set_footer(text="Requested by: {}".format(ctx.author.display_name), icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
                            embed.timestamp = datetime.datetime.utcnow()
                            await msg.edit(embed=embed, components=[])
                            

                # creates embed for users anime and mangastatistics
                # embed for anime includes days watched, mean score, completed, watching, on hold, dropped, plan to watch, total anime
                # embed for mang includes days read, mean score, completed, reading, on hold, dropped, plan to read, total manga, reread, chapters read, volumes read
                elif interaction.custom_id == "statistics":

                    embed = discord.Embed(title=arg + " Anime Statistics", url=titleURL, color=0x87CEEB)
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
                    await msg.edit(embed=embed, components=[])

                    embed = discord.Embed(title=arg + " Manga Statistics", url=titleURL, color=0x87CEEB)
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
                    await ctx.send(embed=embed)

                # creates embed for users favorites
                # loops through anime, manga, characters and favorites
                elif interaction.custom_id == "favorites":
                    embed = discord.Embed(title=arg + "'s Favorites", url=titleURL, color=0x87CEEB)
                    
                    if not data['anime']:
                        pass
                    else:
                        embed.set_thumbnail(url=data['anime'][0]['images']['jpg']['image_url'])
                    if not data['characters']:
                       pass
                    else:
                        embed.set_image(url=data['characters'][0]['images']['jpg']['image_url'])
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
                    
                    await msg.edit(embed=embed, components=[])

                # creates embed for userupdates anime (manga yet to be made)
                # embed for anime includes title, status, episode seen (int) and total episodes (int)
                # embed for manga includes nothing yet

                elif interaction.custom_id == "updates":
                    embed = discord.Embed(title=arg + "'s anime updates", url=titleURL, description="Can't update often yet so we've disabled this one.", color=0x87CEEB)
                    
                    embed.set_footer(text="Requested by: {}".format(ctx.author.display_name), icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
                    embed.timestamp = datetime.datetime.utcnow()

                    await msg.edit(embed=embed, components=[])

                # creates embed for history anime (manga yet to be made)
                # embed for anime includes title, increment, time and date
                # embed for manga includes nothing yet

                elif interaction.custom_id == "history":

                    if not data:
                        await msg.edit(f"This user has no recent anime history or has been set to private.", components=[])
                    else:
                        listdata = []
                        i = 0
                        for length in range(0,len(data)):
                            if i == 20:
                                continue
                            else:
                                i += 1
                                listdata.append(f"- `{data[length]['entry']['name']}` Episode `{data[length]['increment']}` at {data[length]['date'][11:][:-9]} on {data[length]['date'][:-15]}\n")
                        string = ''.join([str(item) for item in listdata])

                        await msg.delete()

                        await ctx.send(f"**{arg}'s anime watch history**\n\n{string}")

                    #if arg2 == "manga":
                    #    
                    #    if not data:
                    #        await ctx.send(f"This user has no recent manga history or has been set to private.")
                    #    else:
                    #        listdata = []
                    #        i = 0
                    #        for length in range(0,len(data)):
                    #            if i == 20:
                    #                continue
                    #            else:
                    #                i += 1
                    #                listdata.append(f"- `{data[length]['entry']['name']}` Chapter `{data[length]['increment']}` at {data[length]['date'][11:][:-9]} on {data[length]['date'][:-15]}\n")
                    #        string = ''.join([str(item) for item in listdata])
                    #        await ctx.send(f"**{arg}'s manga watch history**\n\n{string}")
                       
                # creates embed for friends
                # embed includes username, user url and friends since all in same embed.

                elif interaction.custom_id == "friends":

                    if not data:
                        embed = discord.Embed(title=arg + "'s friends", url=titleURL, description="no friends, that poor human..", color=0x87CEEB)
                        embed.set_image(url="https://i.pinimg.com/originals/b2/a9/f9/b2a9f96c4faa61463d625876e1666b68.gif")
                        embed.set_footer(text="Requested by: {}".format(ctx.author.display_name), icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
                        embed.timestamp = datetime.datetime.utcnow()

                        await msg.edit(embed=embed, components=[])

                    else:
                        listdata = []
                        embed = discord.Embed(title=arg + "'s friends", url=titleURL, description="A maximum of 12 shown.", color=0x87CEEB)
                        i = 0
                        for length in range(0,len(data)):
                            if i == 12:
                                continue
                            else:
                                i += 1
                                listdata.append(f"**{data[length]['user']['username']}** been friends since `{data[length]['friends_since'][:-15]}`\n") # title
                        string = ''.join([str(item) for item in listdata])

                        embed.add_field(name="\u200b", value=string, inline=False)
                        embed.set_footer(text="Requested by: {}".format(ctx.author.display_name), icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
                        embed.timestamp = datetime.datetime.utcnow()

                        await msg.edit(embed=embed, components=[])

                # creates embed for reviews
                # embed for title, url, overall score and date, also includes image as thumbnail

                elif interaction.custom_id == "reviews":

                    if not data:
                        embed = discord.Embed(title=arg + "'s reviews", url=titleURL, description="Oh no, this user has no reviews.", color=0x87CEEB)

                        embed.set_image(url="https://i.pinimg.com/originals/b2/a9/f9/b2a9f96c4faa61463d625876e1666b68.gif")
                        embed.set_footer(text="Requested by: {}".format(ctx.author.display_name), icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
                        embed.timestamp = datetime.datetime.utcnow()

                        await msg.edit(embed=embed, components=[])
                    
                    else:

                        listdata = []
                        titleURL = f"https://myanimelist.net/profile/{arg}/reviews"
                        embed = discord.Embed(title=arg + "'s reviews", url=titleURL, color=0x87CEEB)
                        embed.set_thumbnail(url=data[0]['entry']['images']['jpg']['small_image_url'])
                        i = 0
                        for length in range(0,len(data)):
                            if i == 5:
                                continue
                            else:
                                i += 1
                                listdata.append(f"[{data[length]['entry']['title']}]({data[length]['entry']['url']}) was given a score of {data[length]['scores']['overall']} on {data[length]['date'][:-15]}\n") # title
                        string = ' '.join([str(item) for item in listdata])

                        embed.add_field(name="\u200b", value=string, inline=False)
                        embed.set_footer(text="Requested by: {}".format(ctx.author.display_name), icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
                        embed.timestamp = datetime.datetime.utcnow()

                        await msg.edit(embed=embed, components=[])

                # creates embed for reccomendations
                # embed for title, url for first anime and title url for recommended anime

                elif interaction.custom_id == "recommendations":

                    if not data:

                        embed = discord.Embed(title=arg + "'s recommendations", url=titleURL, description="Oh no, this user has no recommendations.", color=0x87CEEB)

                        embed.set_image(url="https://i.pinimg.com/originals/b2/a9/f9/b2a9f96c4faa61463d625876e1666b68.gif")
                        embed.set_footer(text="Requested by: {}".format(ctx.author.display_name), icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
                        embed.timestamp = datetime.datetime.utcnow()

                        await msg.edit(embed=embed, components=[])

                    else:

                        titleURL = f"https://myanimelist.net/profile/{arg}/recommendations"
                        listdata = []
                        i = 0
                        embed = discord.Embed(title=arg + "'s recommendations", url=titleURL, color=0x87CEEB)
                        for length in range(0,len(data)):
                            if i == 5:
                                continue
                            else:
                                i += 1
                                listdata.append(f"- [{data[length]['entry'][0]['title']}]({data[length]['entry'][0]['url']}) try [{data[length]['entry'][1]['title']}]({data[length]['entry'][1]['url']})\n")
                        string = ' '.join([str(item) for item in listdata])

                        embed.add_field(name="\u200b", value=string, inline=False)
                        embed.set_footer(text="Requested by: {}".format(ctx.author.display_name), icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
                        embed.timestamp = datetime.datetime.utcnow()

                        await msg.edit(embed=embed, components=[])

                # creates embed for clubs
                # embed for name and url.

                elif interaction.custom_id == "clubs":

                    listdata = []
                    titleURL = f"https://myanimelist.net/profile/{arg}/clubs"
                    embed = discord.Embed(title=arg + "'s club", url=titleURL, description=f"This user is in the following clubs:", color=0x87CEEB)

                    for length in range(0,len(data)):
                        listdata.append(data[length]['name']) # title
                        listdata.append(data[length]['url']) # url
                        embed.add_field(name=f"{data[length]['name']}", value=f"[Click]({data[length]['url']})", inline=True)
                    string = '*'.join([str(item) for item in listdata])
                    x = string.split("*")

                    embed.set_footer(text="Requested by: {}".format(ctx.author.display_name), icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
                    embed.timestamp = datetime.datetime.utcnow()

                    await msg.edit(embed=embed, components=[])

            elif response.status == 404:
                await ctx.send("Thats not an user.")

            else:
                await ctx.send("Server is down, try again later.")


def setup(bot):
	bot.add_cog(User(bot))