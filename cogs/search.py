import discord
import datetime
import asyncio

from aiohttp import request
from discord.ext import commands
from discord.ext.commands import MissingRequiredArgument


class Search(commands.Cog):
    
    def __init__(self, client):
        self.client = client
    description = 'Get information about an anime, manga, characters, people, producer, magazine & user through MyAnimeList.'

    @commands.command(name='anime')
    async def anime(self, ctx, *, name):
        '''Retrieves anime from MAL with selection process.
        '''
        URL = f'https://api.jikan.moe/v4/anime?q={name}&order_by=members&sort=desc&page=1'

        # Sents get request pulling the data
        async with request("GET", URL, headers={}) as response:
            if response.status == 200:
                databox = await response.json()
                data = databox['data']
                data_length = len(databox['data'])

            if data_length == 1:
                n = 0 

            elif data_length == 0:
                await ctx.send("I can't find that anime.")
                return

            else:
                output_result = get_results(data, 'title', name, 'animes')
                output = await ctx.send(output_result)
                result = await get_selection(self, ctx, output, data_length, 'anime')
                if result:
                    n = result - 1
                else:
                    return
        

            listdata = databox['data'][n]
            
            # Sents selected anime including title, url, description, image, score
            # members, episodes, aired from, aired to, type, genres & rating
            embed=discord.Embed(title=listdata["title"], url=listdata["url"], description=listdata['synopsis'], color=0xf37a12)

            embed.set_thumbnail(url=listdata["images"]['jpg']['image_url'])
            embed.add_field(name="Score", value=listdata["score"], inline=True)
            embed.add_field(name="Members", value=listdata["members"], inline=True)
            embed.add_field(name="Episodes", value=listdata["episodes"], inline=True)
    
            if listdata["aired"]["from"] is None:
                embed.add_field(name="Start Date", value='Unknown', inline=True)
            else:
                embed.add_field(name="Start Date", value=listdata["aired"]["from"][:-15], inline=True)
            if listdata["aired"]["to"] is None:
                embed.add_field(name="End Date", value="Unknown", inline=True)
            else:
                embed.add_field(name="End Date", value=listdata["aired"]["to"][:-15], inline=True)
    
            embed.add_field(name="Type", value=listdata["type"], inline=True)
            
            genre = listdata['genres']
            c = []
            for length in range(0,len(genre)):
                c.append(genre[length]['name'])
            string = ', '.join([str(item) for item in c])
            genres = string

            embed.add_field(name="Genres", value=genres, inline=False)
            embed.add_field(name="Rating", value=listdata["rating"], inline=True)

            embed.set_footer(text="Requested by: {}".format(ctx.author.display_name), icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
            embed.timestamp = datetime.datetime.utcnow()

            await ctx.send(embed=embed)

    # if argument has been used wrong it triggers the MissingRequiredArgument below
    @anime.error
    async def anime_error(self, ctx, error):
        if isinstance(error, (MissingRequiredArgument)):
            if ctx.guild:
                await ctx.send('To use this command do as following: .anime <name>')
        else:
            return


    @commands.command(name='manga')
    async def manga(self, ctx, *, name):
        '''Retrieves manga from MAL with selection process.
        '''
        URL = f'https://api.jikan.moe/v4/manga?q={name}&order_by=members&sort=desc&page=1'

        async with request("GET", URL, headers={}) as response:
            if response.status == 200:
                databox = await response.json()
                data = databox['data']
                data_length = len(databox['data'])

            if data_length == 1:
                n = 0

            elif data_length == 0:
                await ctx.send("I can't find that manga.")
                return

            else:
                output_result = get_results(data, 'title', name, 'mangas')
                output = await ctx.send(output_result)
                result = await get_selection(self, ctx, output, data_length, 'manga')
                if result:
                    n = result - 1
                else:
                    return

            listdata = databox['data'][n]

            # Sents selected manga including title, url, description, image, score
            # members, total chapters, volumes, published from, aired to, type & genres
            embed=discord.Embed(title=listdata["title"], url=listdata["url"] , description=listdata['synopsis'], color=0xf37a12)

            embed.set_thumbnail(url=listdata["images"]['jpg']['image_url'])
            embed.add_field(name="Score", value=listdata["scored"], inline=True)
            embed.add_field(name="Members", value=listdata["members"], inline=True)
            embed.add_field(name="Total Chapters", value=listdata["chapters"], inline=True)
            embed.add_field(name="Volumes", value=listdata["volumes"], inline=True)
            if listdata["published"]["from"] is None:
                embed.add_field(name="Start Date", value='Unknown', inline=True)
            else:
                embed.add_field(name="Start Date", value=listdata["published"]["from"][:-15], inline=True)
            if listdata["published"]["to"] is None:
                embed.add_field(name="End Date", value="Unknown", inline=True)
            else:
                embed.add_field(name="End Date", value=listdata["published"]["to"][:-15], inline=True)

            embed.add_field(name="Type", value=listdata["type"], inline=True)

            genre = listdata['genres']
            c = []
            for length in range(0,len(genre)):
                c.append(genre[length]['name'])
            string = ', '.join([str(item) for item in c])
            genres = string

            embed.add_field(name="Genres", value=genres, inline=False)

            embed.set_footer(text="Requested by: {}".format(ctx.author.display_name), icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
            embed.timestamp = datetime.datetime.utcnow()

            await ctx.send(embed=embed)

    @manga.error
    async def manga_error(self, ctx, error):
        if isinstance(error, (MissingRequiredArgument)):
            if ctx.guild:
                await ctx.send('To use this command do as following: .manga <name>')
        else:
            return


    @commands.command(name='character')
    async def character(self, ctx, *, name):
        '''Retrieves character from MAL with selection process.
        '''
        URL = f'https://api.jikan.moe/v4/characters?q={name}&order_by=favorites&sort=desc&page=1'
    
        # Sents get request pulling the data
        async with request("GET", URL, headers={}) as response:
            if response.status == 200:
                databox = await response.json()
                data = databox['data']
                data_length = len(databox['data'])

            if data_length == 1:
                n = 0 

            elif data_length == 0:
                await ctx.send("I can't find that character.")
                return

            else:
                output_result = get_results(data, 'name', name, 'characters')
                output = await ctx.send(output_result)
                result = await get_selection(self, ctx, output, data_length, 'character')
                if result:
                    n = result - 1
                else:
                    return
        

            listdata = databox['data'][n]
            char_about = listdata['about']
    
            # Sents selected anime including title, url, description, image, members
            if len(char_about)>4000:
                message = await ctx.send('Too much information about this character for Vignette to handle, good luck with what I can give you.')
                char_about= char_about[:3900]
                await asyncio.sleep(6)

                embed=discord.Embed(title=listdata['name'], url=listdata["url"], description=char_about+'...', color=0x8a7bff)

                embed.add_field(name='Members',value=listdata['favorites'], inline= False)
                embed.set_image(url=listdata['images']['jpg']['image_url'])

                await message.delete()
                
                embed.set_footer(text="Requested by: {}".format(ctx.author.display_name), icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
                embed.timestamp = datetime.datetime.utcnow()

                await ctx.send(embed=embed)

            else:
                char_about = char_about

                embed=discord.Embed(title=listdata['name'], url=listdata["url"], description=char_about, color=0x8e37b0)
                
                embed.add_field(name='Members',value=listdata['favorites'], inline= False)
                embed.set_image(url=listdata['images']['jpg']['image_url'])

                embed.set_footer(text="Requested by: {}".format(ctx.author.display_name), icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
                embed.timestamp = datetime.datetime.utcnow()
                await ctx.send(embed=embed)
  
    @character.error
    async def char_error(self, ctx, error):
        if isinstance(error, (MissingRequiredArgument)):
            if ctx.guild:
                await ctx.send('To use this command do as following: .character <name>')
            else:
                return


    @commands.command(name='person')
    async def person(self, ctx, *, name):
        '''Retrieves person from MAL with selection process.
        '''
        URL = f'https://api.jikan.moe/v4/people?q={name}&order_by=favorites&sort=desc&page=1'
        async with request("GET", URL, headers={}) as response:
            if response.status == 200:
                databox = await response.json()
                data = databox['data']
                data_length = len(databox['data'])

            if data_length == 1:
                n = 0 

            elif data_length == 0:
                await ctx.send("I can't find that anime.")
                return

            else:
                output_result = get_results(data,'name',name,'peoples')
                output = await ctx.send(output_result)
                result = await get_selection(self, ctx, output, data_length, 'people')
                if result:
                    n = result - 1
                else:
                    return


            listdata = databox['data'][n]
            char_about = listdata['about']

            # Sents selected person including name, url, description, members,
            # birthday, given name, family name & website if available.
            if len(char_about)>4000:
                message = await ctx.send('Too much information about this person for the bot to handle, good luck with what I can give you.')
                char_about= char_about[:3900]

                await asyncio.sleep(6)

                embed=discord.Embed(title=listdata['name'], url=listdata["url"], description=char_about+'...', color=0x8a7bff)

                embed.add_field(name='Members',value=listdata['favorites'], inline= False)
                embed.add_field(name='Birthday',value=listdata['birthday'][:-15], inline= False)
                embed.add_field(name='Given name',value=listdata['given_name'], inline= False)
                embed.add_field(name='Family name',value=listdata['family_name'], inline= False)
                embed.add_field(name='Website',value=listdata['website_url'], inline= False)

                embed.set_image(url=listdata['images']['jpg']['image_url'])

                await message.delete()

                embed.set_footer(text="Requested by: {}".format(ctx.author.display_name), icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
                embed.timestamp = datetime.datetime.utcnow()

                await ctx.send(embed=embed)

            else:
                char_about = char_about

                embed=discord.Embed(title=listdata['name'], url=listdata["url"], description=char_about, color=0x8e37b0)

                embed.add_field(name='Members',value=listdata['favorites'], inline= False)
                embed.add_field(name='Birthday',value=listdata['birthday'][:-15], inline= False)
                embed.add_field(name='Given name',value=listdata['given_name'], inline= False)
                embed.add_field(name='Family name',value=listdata['family_name'], inline= False)
                embed.add_field(name='Website',value=listdata['website_url'], inline= False)

                embed.set_image(url=listdata['images']['jpg']['image_url'])

                embed.set_footer(text="Requested by: {}".format(ctx.author.display_name), icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
                embed.timestamp = datetime.datetime.utcnow()

                await ctx.send(embed=embed)

    # if argument has been used wrong it triggers the MissingRequiredArgument below
    @person.error
    async def person_error(self, ctx, error):
        if isinstance(error, (MissingRequiredArgument)):
            if ctx.guild:
                await ctx.send('To use this command do as following: .person <name>')
        else:
            return


    @commands.command(name='producer')
    async def producer(self, ctx, *, name):
        URL = f'https://api.jikan.moe/v4/producers?q={name}&order_by=members&sort=desc&page=1'
        
        # Sents get request pulling the data
        async with request("GET", URL, headers={}) as response:
            if response.status == 200:
                databox = await response.json()
                data = databox['data']
                data_length = len(databox['data'])

            if data_length == 1:
                n = 0 
            elif data_length == 0:
                await ctx.send("I can't find that producer.")
                return
            else:
                output_result = get_results(data, 'name', name, 'producers')
                output = await ctx.send(output_result)
                result = await get_selection(self, ctx, output, data_length, 'producer')
                if result:
                    n = result - 1
                else:
                    return


            listdata = databox['data'][n]

            # Sents selected producer including name, url, MAL id and Titles
            embed=discord.Embed(title=listdata["name"], url=listdata["url"], color=0xf37a12)

            embed.add_field(name="MAL id", value=listdata["mal_id"], inline=True)
            embed.add_field(name="Titles made", value=listdata["count"], inline=True)

            embed.set_footer(text="Requested by: {}".format(ctx.author.display_name), icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
            embed.timestamp = datetime.datetime.utcnow()

            await ctx.send(embed=embed)

    # if argument has been used wrong it triggers the MissingRequiredArgument below
    @producer.error
    async def producer_error(self, ctx, error):
        if isinstance(error, (MissingRequiredArgument)):
            if ctx.guild:
                await ctx.send('To use this command do as following: .producer <name>')
        else:
            return


    @commands.command(name='magazine')
    async def magazine(self, ctx, *, name):
        URL = f'https://api.jikan.moe/v4/magazines?q={name}&order_by=members&sort=desc&page=1'

        # Sents get request pulling the data
        async with request("GET", URL, headers={}) as response:
            if response.status == 200:
                databox = await response.json()
                data = databox['data']
                data_length = len(databox['data'])

            if data_length == 1:
                n = 0 
            elif data_length == 0:
                await ctx.send("I can't find that magazine.")
                return
            else:
                output_result = get_results(data, 'name', name, 'magazines')
                output = await ctx.send(output_result)
                result = await get_selection(self, ctx, output, data_length, 'magazine')
                if result:
                    n = result - 1
                else:
                    return
      
      
            listdata = databox['data'][n]

            embed=discord.Embed(title=listdata["name"], url=listdata["url"], color=0xf37a12)

            embed.add_field(name="MAL id", value=listdata["mal_id"], inline=True)
            embed.add_field(name="Titles", value=listdata["count"], inline=True)

            embed.set_footer(text="Requested by: {}".format(ctx.author.display_name), icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
            embed.timestamp = datetime.datetime.utcnow()

            await ctx.send(embed=embed)

    # if argument has been used wrong it triggers the MissingRequiredArgument below
    @magazine.error
    async def magazine_error(self, ctx, error):
        if isinstance(error, (MissingRequiredArgument)):
            if ctx.guild:
                await ctx.send('To use this command do as following: .magazine <name>')
            else:
                return


async def get_selection(self, ctx, message, data_length, type):
    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel
      
    while True:
        try:
            msg = await self.client.wait_for('message', check=check, timeout=20)
        except asyncio.TimeoutError:
            await ctx.send("You didn't reply within the 20 second period.")
            return None
        
        if msg.content.isdigit():
            if int(msg.content) in [*range(1, data_length + 1)]:
                await message.delete()
                await msg.delete()
                return int(msg.content)
            else:
                continue    
        elif msg.content.lower() == 'stfu':
            await message.delete()
            await msg.delete()
            return None
        else:
            continue


def get_results(data, name, query, type):
    result_list = [f'{str(n + 1)}.   {data[n][name]}' for n in range(0, len(data))]
    cancel_message = 'Tell me the number or type `stfu` to shut me up.'

    result_message = '\n '.join(result_list)
    output = f'```\n {result_message}\n```\n {cancel_message}'

    return output


def setup(bot):
    bot.add_cog(Search(bot))
