import discord
import html

from discord.ext import commands
from aiohttp import request
from discord_components import Button, ButtonStyle


class Trivia(commands.Cog):

    def __init__(self, client):
        self.client = client
    description = "Trivia"


    @commands.command(name='trivia')
    async def trivia(self, ctx, arg=None, arg2=None):
        if arg in ("easy", "medium", "hard"):
            if arg2 in ("1", "2", "3", "4", "5"):
                URL = f"https://opentdb.com/api.php?amount={arg2}&category=31&difficulty={arg}&type=boolean"
            else:
                await ctx.send(f"You've forgotten to choose an amount (1-5)")
                return

            async with request("GET", URL, headers={}) as response:
                if response.status == 200:
                    databox = await response.json()
                    data = databox['results']
                    n = 0
                    score = 0
                for i in data:
                    if n == {arg2}:
                        break
                    else:
                        question = html.unescape(data[n]['question'])
                        button_1 = Button(label=f"True", style=ButtonStyle.green, custom_id="button1")
                        button_2 = Button(label=f"False", style=ButtonStyle.red, custom_id="button2")
                        await ctx.send(f"{question}", components = [[button_1, button_2]])
                        interaction = await self.client.wait_for("button_click")
                        if data[n]['correct_answer'] == "True":
                            if interaction.custom_id == "button1":
                                score += 1
                                await interaction.send(content=f"Correct answer! `{score}/{arg2} points.`", ephemeral=False)
                            else:
                                await interaction.send(content=f"Wrong answer `{score}/{arg2} points.`", ephemeral=False)
                        elif data[n]['correct_answer'] == "False":
                            if interaction.custom_id == "button2":
                                score += 1
                                await interaction.send(content=f"Correct answer! `{score}/{arg2} points.`", ephemeral=False)
                            else:
                                await interaction.send(content=f"Wrong answer `{score}/{arg2} points.`", ephemeral=False)
                        else:
                            await ctx.send("Wow, dunno how you came here but tell me!")
                        n += 1

        else:
            await ctx.send(f"Woopsie! choose a difficulity .trivia <easy, medium, hard> <1-5>")


def setup(bot):
	bot.add_cog(Trivia(bot))