import discord
import os
import random
import asyncio
import datetime
import aiosqlite
import pytz

from dotenv import load_dotenv
from aiohttp import request
from datetime import datetime, timedelta
from discord.ext import tasks, commands
from discord_components import DiscordComponents

"""
Ssecurely hide your token, you can do so in a .env file.
1. Create a .env in the same directory as bot.py
2. In the .env file format your variables like this: DISCORD_TOKEN=your_token_here
3. Start the bot
"""
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
client = commands.Bot(command_prefix = '.')
DiscordComponents(client)


@client.command()
@commands.is_owner()
async def reload(ctx, extension):
    """
    | Reload command for cogs
    | To reload a function use .reload with the cog name - example: .reload search
    """
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    print(f"Reloaded {extension}")


for filename in os.listdir('./cogs'):
    """
    | Loading all the available cogs
    """
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


@client.event
async def on_ready():
    """
    | Activity of the discord bot
    """
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='anime'))
    print('Vignette is online.')
    async with aiosqlite.connect("main.db") as db:
        async with db.cursor() as cursor:
            await cursor.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER , user TEXT , guild INTEGER , points INTEGER)')
            await cursor.execute('CREATE TABLE IF NOT EXISTS notify (mal_id INTEGER , guild INTEGER , airing BOOLEAN, title TEXT)')
        await db.commit()


async def ch_pr():
    await client.wait_until_ready()
    """
    | Add multiple statuses by changing inbetween the "" or adding the , and putting more "" before the ]
    """
    statuses = ["anime", "your every move", "hentai", "BLACKPINK"]

    while not client.is_closed():
        status = random.choice(statuses)
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=status))
        """
        | You can change the timer for activity by replacing the 120 (2minutes) with for example 60 (1minute) just make sure to put it in seconds.
        """
        await asyncio.sleep(120)


@tasks.loop(seconds=600)
async def get():
    """
    | Announce airing anime.
    | Checks weekday name and sets in URL
    """
    channel = client.get_channel(819284431914270732)
    weekdays = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    date = datetime.now()
    tz = pytz.timezone('Asia/Tokyo')
    today = date.astimezone(tz)
    print(today)

    todayplus = datetime.now(pytz.timezone('Asia/Tokyo'))
    todayplus += timedelta(minutes=10)
    if today.date() == todayplus.date():
        URL = f"https://api.jikan.moe/v4/schedules/{weekdays[today.weekday()].lower()}"
    else:
        URL = f"https://api.jikan.moe/v4/schedules/{weekdays[todayplus.weekday()].lower()}"

    '''Sents request to pull all mal_ids and airing time from the TODAY schedule page
    '''
    async with request("GET", URL, headers={}) as response:
        if response.status == 200:
            databox = await response.json()
            data = databox['data']

            release = []
            for length in range(0,len(data)):
                release.append({"mal_id": data[length]['mal_id'], "time": data[length]['broadcast']['time']})

            '''Opens DB and selects all mal_ids
            '''
            async with aiosqlite.connect("main.db") as db:
                cur = await db.execute("SELECT mal_id FROM notify")
                row = await cur.fetchall()
                released = []
                for length in range(0,len(row)):
                    released.append(row[length][0])

                ''' Checks if pulled mal_ids from scheduled page are in database
                If they are then checks if the mal_id is within 10 minutes of airing
                If this is the case then it announces the anime airing with an embed
                '''
                for length in range(0,len(release)):
                    
                    if int(release[length]['mal_id']) in released:
                        if release[length]['time'] >= today.strftime('%H:%M') and release[length]['time'] <= todayplus.strftime('%H:%M'):
                            URL = f"https://api.jikan.moe/v4/anime/{release[length]['mal_id']}"

                            async with request("GET", URL, headers={}) as response:
                                if response.status == 200:
                                    databox = await response.json()
                                    data = databox['data']
                                        
                                    embed = discord.Embed(title=f"{data['title']}", description=f"A new episode of `{data['title']}` is now airing!", url=f"{data['url']}", color=0x87CEEB)
                                    embed.add_field(name="Duration", value=f"{data['duration']}", inline=False)
                                    embed.set_thumbnail(url=f"{data['images']['jpg']['image_url']}")
                                    await channel.send(embed=embed)
                                    print(data['title'] + ' aired')

                        else:
                            continue     
                    else:
                        continue
        else:
            await channel.send("API is down, couldn't request airing notifications")


@get.before_loop
async def before_get():
    await client.wait_until_ready()


get.start()
client.loop.create_task(ch_pr())


"""
Bot run.
"""
client.run(TOKEN)
