import discord
import aiosqlite
import random

from discord.ext import commands
from discord_components import Button, ButtonStyle
from load import *


class Guess(commands.Cog):

    def __init__(self, client):
        self.client = client
    description = "Guess game"


    @commands.command(name='guess')
    async def guess(self, ctx, arg=None):
        if ctx.channel.id != 913836567125196811:
            await ctx.send("Please use this in `#guess-the-character` channel")
        else:
            if arg == "char":
                random_number = random.randint(0, 999)
                saved_number = random_number
                n = random.randint(1, 4)
                if n == 1:
                    button_1 = Button(label=f"{chardata[saved_number]['name']}", style=ButtonStyle.green, custom_id="1")
                    button_2 = Button(label=f"{chardata[random.randint(0, 999)]['name']}", style=ButtonStyle.green, custom_id="2")
                    button_3 = Button(label=f"{chardata[random.randint(0, 999)]['name']}", style=ButtonStyle.green, custom_id="3")
                    button_4 = Button(label=f"{chardata[random.randint(0, 999)]['name']}", style=ButtonStyle.green, custom_id="4")
                elif n == 2:
                    button_1 = Button(label=f"{chardata[random.randint(0, 999)]['name']}", style=ButtonStyle.green, custom_id="1")
                    button_2 = Button(label=f"{chardata[saved_number]['name']}", style=ButtonStyle.green, custom_id="2")
                    button_3 = Button(label=f"{chardata[random.randint(0, 999)]['name']}", style=ButtonStyle.green, custom_id="3")
                    button_4 = Button(label=f"{chardata[random.randint(0, 999)]['name']}", style=ButtonStyle.green, custom_id="4")
                elif n == 3:
                    button_1 = Button(label=f"{chardata[random.randint(0, 999)]['name']}", style=ButtonStyle.green, custom_id="1")
                    button_2 = Button(label=f"{chardata[random.randint(0, 999)]['name']}", style=ButtonStyle.green, custom_id="2")
                    button_3 = Button(label=f"{chardata[saved_number]['name']}", style=ButtonStyle.green, custom_id="3")
                    button_4 = Button(label=f"{chardata[random.randint(0, 999)]['name']}", style=ButtonStyle.green, custom_id="4")
                else:
                    button_1 = Button(label=f"{chardata[random.randint(0, 999)]['name']}", style=ButtonStyle.green, custom_id="1")
                    button_2 = Button(label=f"{chardata[random.randint(0, 999)]['name']}", style=ButtonStyle.green, custom_id="2")
                    button_3 = Button(label=f"{chardata[random.randint(0, 999)]['name']}", style=ButtonStyle.green, custom_id="3")
                    button_4 = Button(label=f"{chardata[saved_number]['name']}", style=ButtonStyle.green, custom_id="4")

                await ctx.send(f"{chardata[saved_number]['images']['jpg']['image_url']}", components = [[button_1, button_2, button_3, button_4]])

                interaction = await self.client.wait_for("button_click")

                if int(interaction.custom_id) == n:

                    async with aiosqlite.connect("main.db") as db:
                        async with db.cursor() as cursor:
                            await cursor.execute('SELECT id FROM users WHERE id = ?', (ctx.author.id,))
                            data = await cursor.fetchone()

                            if data:
                                await cursor.execute('UPDATE users SET points = points + 1 WHERE id = ?', (ctx.author.id,))

                            else:
                                await cursor.execute('INSERT INTO users (id, user, guild, points) VALUES (?, ?, ?, ?)', (ctx.author.id, ctx.author.display_name, ctx.guild.id, 1))

                        await db.commit()

                        cur = await db.execute("SELECT points FROM users WHERE id = ?", (ctx.author.id,))
                        points = await cur.fetchone()

                    await interaction.send(content=f"`{chardata[saved_number]['name']}` was the **CORRECT ANSWER!!**\n{ctx.author.display_name} has `{points[0]}` points.", ephemeral=False)

                else:
                    async with aiosqlite.connect("main.db") as db:
                        async with db.cursor() as cursor:
                            await cursor.execute('SELECT id FROM users WHERE id = ?', (ctx.author.id,))
                            data = await cursor.fetchone()

                            if data:
                                await cursor.execute('UPDATE users SET points = points - 2 WHERE id = ?', (ctx.author.id,))

                            else:
                                await cursor.execute('INSERT INTO users (id, user, guild, points) VALUES (?, ?, ?, ?)', (ctx.author.id, ctx.author.display_name, ctx.guild.id, 0))
                        await db.commit()

                        cur = await db.execute("SELECT points FROM users WHERE id = ?", (ctx.author.id,))
                        points = await cur.fetchone()

                    await interaction.send(content=f"Woopsie, **wrong** answer! the correct answer was `{chardata[saved_number]['name']}`\n{ctx.author.display_name} has `{points[0]}` points.", ephemeral=False)
            
            elif arg == "anime":
                random_number = random.randint(0, 499)
                saved_number = random_number
                n = random.randint(1, 4)
                if n == 1:
                    button_1 = Button(label=f"{animedata[saved_number]['title']}", style=ButtonStyle.green, custom_id="1")
                    button_2 = Button(label=f"{animedata[random.randint(0, 499)]['title']}", style=ButtonStyle.green, custom_id="2")
                    button_3 = Button(label=f"{animedata[random.randint(0, 499)]['title']}", style=ButtonStyle.green, custom_id="3")
                    button_4 = Button(label=f"{animedata[random.randint(0, 499)]['title']}", style=ButtonStyle.green, custom_id="4")
                elif n == 2:
                    button_1 = Button(label=f"{animedata[random.randint(0, 499)]['title']}", style=ButtonStyle.green, custom_id="1")
                    button_2 = Button(label=f"{animedata[saved_number]['title']}", style=ButtonStyle.green, custom_id="2")
                    button_3 = Button(label=f"{animedata[random.randint(0, 499)]['title']}", style=ButtonStyle.green, custom_id="3")
                    button_4 = Button(label=f"{animedata[random.randint(0, 499)]['title']}", style=ButtonStyle.green, custom_id="4")
                elif n == 3:
                    button_1 = Button(label=f"{animedata[random.randint(0, 499)]['title']}", style=ButtonStyle.green, custom_id="1")
                    button_2 = Button(label=f"{animedata[random.randint(0, 499)]['title']}", style=ButtonStyle.green, custom_id="2")
                    button_3 = Button(label=f"{animedata[saved_number]['title']}", style=ButtonStyle.green, custom_id="3")
                    button_4 = Button(label=f"{animedata[random.randint(0, 499)]['title']}", style=ButtonStyle.green, custom_id="4")
                else:
                    button_1 = Button(label=f"{animedata[random.randint(0, 499)]['title']}", style=ButtonStyle.green, custom_id="1")
                    button_2 = Button(label=f"{animedata[random.randint(0, 499)]['title']}", style=ButtonStyle.green, custom_id="2")
                    button_3 = Button(label=f"{animedata[random.randint(0, 499)]['title']}", style=ButtonStyle.green, custom_id="3")
                    button_4 = Button(label=f"{animedata[saved_number]['title']}", style=ButtonStyle.green, custom_id="4")

                await ctx.send(f"{animedata[saved_number]['images']['jpg']['image_url']}", components = [[button_1, button_2, button_3, button_4]])

                interaction = await self.client.wait_for("button_click")

                if int(interaction.custom_id) == n:

                    async with aiosqlite.connect("main.db") as db:
                        async with db.cursor() as cursor:
                            await cursor.execute('SELECT id FROM users WHERE id = ?', (ctx.author.id,))
                            data = await cursor.fetchone()

                            if data:
                                await cursor.execute('UPDATE users SET points = points + 1 WHERE id = ?', (ctx.author.id,))

                            else:
                                await cursor.execute('INSERT INTO users (id, user, guild, points) VALUES (?, ?, ?, ?)', (ctx.author.id, ctx.author.display_name, ctx.guild.id, 1))

                        await db.commit()

                        cur = await db.execute("SELECT points FROM users WHERE id = ?", (ctx.author.id,))
                        points = await cur.fetchone()

                    await interaction.send(content=f"`{animedata[saved_number]['title']}` was the **CORRECT ANSWER!!**\n{ctx.author.display_name} has `{points[0]}` points.", ephemeral=False)

                else:
                    async with aiosqlite.connect("main.db") as db:
                        async with db.cursor() as cursor:
                            await cursor.execute('SELECT id FROM users WHERE id = ?', (ctx.author.id,))
                            data = await cursor.fetchone()

                            if data:
                                await cursor.execute('UPDATE users SET points = points - 2 WHERE id = ?', (ctx.author.id,))

                            else:
                                await cursor.execute('INSERT INTO users (id, user, guild, points) VALUES (?, ?, ?, ?)', (ctx.author.id, ctx.author.display_name, ctx.guild.id, 0))
                        await db.commit()

                        cur = await db.execute("SELECT points FROM users WHERE id = ?", (ctx.author.id,))
                        points = await cur.fetchone()
                    await interaction.send(content=f"Woopsie, **wrong** answer! the correct answer was `{animedata[saved_number]['title']}`\n{ctx.author.display_name} has `{points[0]}` points.", ephemeral=False)
            else:
                await ctx.send("Dummy, you can only .guess `anime` or `char`")


    @commands.command(name='leaderboards')
    async def leaderboards(self, ctx):
        async with aiosqlite.connect("main.db") as db:
            cur = await db.execute("SELECT * FROM users ORDER BY points DESC LIMIT 10")
            row = await cur.fetchall()

            leaderboard = []
            c = 0
            count = 1
            embed = discord.Embed(title="Top 10 Leaderboards",url="https://www.youtube.com/watch?v=dQw4w9WgXcQ", color=0x87CEEB)
            for i in row:
                if count == 10:
                    continue
                else:
                    leaderboard.append(f"{count}. **{row[c][1]}** with `{row[c][3]}` points.\n")
                    c += 1
                    count += 1
            string = ''.join([str(item) for item in leaderboard])
            
            embed.add_field(name=f"Guess the Anime & Characters", value=f"{string}", inline=False)

            embed.set_image(url="https://i.pinimg.com/originals/d5/da/53/d5da5398e5a193120690d0f0ca64d2ed.gif")
            embed.set_footer(text="Requested by: {}".format(ctx.author.display_name), icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")

            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Guess(bot))