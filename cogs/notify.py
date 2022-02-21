import discord
import aiosqlite

from aiohttp import request
from discord.ext import commands


class Notify(commands.Cog):

    def __init__(self, client):
        self.client = client
    description = "Notify airing anime."

    @commands.command(name='notify')
    async def notify(self, ctx, *, arg):
        '''Adds airing anime to the db
        '''

        URL = f"https://api.jikan.moe/v4/anime?q={arg}&status=airing,upcoming&order_by=members&sort=desc"

        async with request("GET", URL, headers={}) as response:
            if response.status == 200:
                databox = await response.json()
                data = databox['data']
                
                if not data:
                    await ctx.send(f"I couldn't add that anime to the list, try again with the alternative (synonym) or japanese title.")

                elif data[0]['status'] == 'Finished Airing':
                    await ctx.send(f"You dummy, `{data[0]['title']}` has already finished airing.")
                else:

                    async with aiosqlite.connect("main.db") as db:
                        cur = await db.execute("SELECT mal_id FROM notify")
                        row = await cur.fetchall()
                        current = []

                        for length in range(0,len(row)):
                            current.append(row[length][0])
                        
                        if data[0]['mal_id'] in current:
                            await ctx.send(f"You dummy, `{data[0]['title']}` is already in the database.")

                        else:
                            if data[0]['status'] == 'Not yet aired' or 'Currently Airing':

                                async with aiosqlite.connect("main.db") as db:
                                    async with db.cursor() as cursor:
                                        await cursor.execute('SELECT mal_id FROM notify WHERE mal_id = ?', (data[0]['mal_id'],))
                                        cur = await cursor.fetchone()

                                        if cur:
                                            await ctx.send(f"`{data[0]['title']}` is already in the database, we'll notify when it airs.")

                                        else:
                                            await cursor.execute('INSERT INTO notify (mal_id, guild, airing, title) VALUES (?, ?, ?, ?)', (data[0]['mal_id'], ctx.guild.id, data[0]['airing'], data[0]['title']))
                                            
                                            embed = discord.Embed(title=f"{data[0]['title']}", url=f"{data[0]['url']}", color=0x87CEEB)

                                            embed.add_field(name="I did it!", value=f"`{data[0]['title']}` has been added to the database and I'll announce when it airs!", inline=False)
                                            embed.set_thumbnail(url=f"{data[0]['images']['jpg']['image_url']}")
                                            embed.set_footer(text="Requested by: {}".format(ctx.author.display_name), icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
                                            await ctx.send(embed=embed)

                                    await db.commit()
                            else: 
                                await ctx.send(f"You've found a bug, please report it including what you used in the command.")
            else:
                await ctx.send(f"Aww the API is currently down, hang on we're working on a fix.")


    @commands.command(name='delete')
    async def delete(self, ctx, *, arg):
        '''Deletes anime from the db
        '''

        URL = f"https://api.jikan.moe/v4/anime?q={arg}&status=airing,upcoming&order_by=members&sort=desc"

        async with request("GET", URL, headers={}) as response:
            if response.status == 200:
                databox = await response.json()
                data = databox['data']
                
                if not data:
                    await ctx.send(f"I couldn't find that anime.")

                else:
                    async with aiosqlite.connect("main.db") as db:
                        cur = await db.execute("SELECT mal_id FROM notify")
                        row = await cur.fetchall()
                        current = []

                        for length in range(0,len(row)):
                            current.append(row[length][0])

                        if data[0]['mal_id'] in current:
                            async with db.cursor() as cursor:
                                await cursor.execute('DELETE FROM notify WHERE mal_id = ?', (data[0]['mal_id'],))
                            await db.commit()
                            
                            await ctx.send(f"I deleted `{data[0]['title']}` from the database.")

                        else:
                            await ctx.send(f"`{data[0]['title']}` if not in the database, no worries.")


    @commands.command(name='airlist')
    async def airlist(self, ctx):
        '''Shows the current list of airing anime
        '''
        async with aiosqlite.connect("main.db") as db:
            cur = await db.execute("SELECT mal_id, title FROM notify")
            row = await cur.fetchall()

            if not row:
                await ctx.send(f"You dummy, you dont have anything in here.")
            else:

                released = []
                c = 0

                for length in range(0,len(row)):
                    released.append(f'**-** *{row[length][1]}*\n')
                    c += 1
                string = ' '.join([str(item) for item in released])

                pre_string = "**This channel will be notified for these currently airing anime:**\n\n"
                post_string = f"\nFor a total of `{c}` anime."

                await ctx.send(pre_string + string + post_string)


# adding cog to bot setup
def setup(bot):
	bot.add_cog(Notify(bot))