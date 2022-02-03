import discord
import datetime

from aiohttp import request
from discord.ext import commands
from discord.ext.commands import MissingRequiredArgument


class Top(commands.Cog):

    def __init__(self, client):
        self.client = client
    description = "Gets the top from MyAnimeList"


    @commands.command(name='top')
    async def top(self, ctx, arg: str):
        '''Pulls the right data from MAL, checks the arguments needed to use the function correctly.
        '''
        if arg.lower() in ("anime", "manga", "characters", "people", "reviews"):
            URL = f"https://api.jikan.moe/v4/top/{arg.lower()}"
        else:
            await ctx.send("I can only retrieve .top <anime, manga, characters, people or reviews>")


        # Sents get request pulling the data
        async with request("GET", URL, headers={}) as response:
            if response.status == 200:
                databox = await response.json()
                data = databox["data"]


        # creates empty list
        title = data
        titlelist = []


		# gives the top 25 anime, this includes the rank, title and score
        if arg == "anime":

            for length in range(0, len(title)):
                titlelist.append(title[length]['rank'])
                titlelist.append(title[length]['title'])
                titlelist.append(title[length]['score'])
            titles = titlelist

            await ctx.send("**The current top 25 " + str(arg) + " on MyAnimeList**" + "\n"
                            + "\n" + str(titles[0]) + ". " + str(titles[1]) + " scored a " + str(titles[2]) + "\n" + str(titles[3]) + ". " + str(titles[4]) + " scored a " + str(titles[5])
                            + "\n" + str(titles[6]) + ". " + str(titles[7]) + " scored a " + str(titles[8]) + "\n" + str(titles[9]) + ". " + str(titles[10]) + " scored a " + str(titles[11]) 
                            + "\n" + str(titles[12]) + ". " + str(titles[13]) + " scored a " + str(titles[14]) + "\n" + str(titles[15]) + ". " + str(titles[16]) + " scored a " + str(titles[17]) 
                            + "\n" + str(titles[18]) + ". " + str(titles[19]) + " scored a " + str(titles[20]) + "\n" + str(titles[21]) + ". " + str(titles[22]) + " scored a " + str(titles[23]) 
                            + "\n" + str(titles[24]) + ". " + str(titles[25]) + " scored a " + str(titles[26]) + "\n" + str(titles[27]) + ". " + str(titles[28]) + " scored a " + str(titles[29]) 
                            + "\n" + str(titles[30]) + ". " + str(titles[31]) + " scored a " + str(titles[32]) + "\n" + str(titles[33]) + ". " + str(titles[34]) + " scored a " + str(titles[35]) 
                            + "\n" + str(titles[36]) + ". " + str(titles[37]) + " scored a " + str(titles[38]) + "\n" + str(titles[39]) + ". " + str(titles[40]) + " scored a " + str(titles[41]) 
                            + "\n" + str(titles[42]) + ". " + str(titles[43]) + " scored a " + str(titles[44]) + "\n" + str(titles[45]) + ". " + str(titles[46]) + " scored a " + str(titles[47]) 
                            + "\n" + str(titles[48]) + ". " + str(titles[49]) + " scored a " + str(titles[50]) + "\n" + str(titles[51]) + ". " + str(titles[52]) + " scored a " + str(titles[53])
                            + "\n" + str(titles[54]) + ". " + str(titles[55]) + " scored a " + str(titles[56]) + "\n" + str(titles[57]) + ". " + str(titles[58]) + " scored a " + str(titles[59])
                            + "\n" + str(titles[60]) + ". " + str(titles[61]) + " scored a " + str(titles[62]) + "\n" + str(titles[63]) + ". " + str(titles[64]) + " scored a " + str(titles[65])
                            + "\n" + str(titles[66]) + ". " + str(titles[67]) + " scored a " + str(titles[68]) + "\n" + str(titles[69]) + ". " + str(titles[70]) + " scored a " + str(titles[71])
                            + "\n" + "25" + ". " + str(titles[73]) + " scored a " + str(titles[74])  + "\n" + "\n" + "*Requested by: {}*".format(ctx.author.display_name))


		# gives the top 25 manga, this includes the rank, title and score
        elif arg == "manga":

            for length in range(0, len(title)):
                titlelist.append(title[length]['rank'])
                titlelist.append(title[length]['title'])
                titlelist.append(title[length]['scored'])
            titles = titlelist

            await ctx.send("**The current top 25 " + str(arg) + " on MyAnimeList**" + "\n"
                            + "\n" + str(titles[0]) + ". " + str(titles[1]) + " scored a " + str(titles[2]) + "\n" + str(titles[3]) + ". " + str(titles[4]) + " scored a " + str(titles[5])
                            + "\n" + str(titles[6]) + ". " + str(titles[7]) + " scored a " + str(titles[8]) + "\n" + str(titles[9]) + ". " + str(titles[10]) + " scored a " + str(titles[11]) 
                            + "\n" + str(titles[12]) + ". " + str(titles[13]) + " scored a " + str(titles[14]) + "\n" + str(titles[15]) + ". " + str(titles[16]) + " scored a " + str(titles[17]) 
                            + "\n" + str(titles[18]) + ". " + str(titles[19]) + " scored a " + str(titles[20]) + "\n" + str(titles[21]) + ". " + str(titles[22]) + " scored a " + str(titles[23]) 
                            + "\n" + str(titles[24]) + ". " + str(titles[25]) + " scored a " + str(titles[26]) + "\n" + str(titles[27]) + ". " + str(titles[28]) + " scored a " + str(titles[29]) 
                            + "\n" + str(titles[30]) + ". " + str(titles[31]) + " scored a " + str(titles[32]) + "\n" + str(titles[33]) + ". " + str(titles[34]) + " scored a " + str(titles[35]) 
                            + "\n" + str(titles[36]) + ". " + str(titles[37]) + " scored a " + str(titles[38]) + "\n" + str(titles[39]) + ". " + str(titles[40]) + " scored a " + str(titles[41]) 
                            + "\n" + str(titles[42]) + ". " + str(titles[43]) + " scored a " + str(titles[44]) + "\n" + str(titles[45]) + ". " + str(titles[46]) + " scored a " + str(titles[47]) 
                            + "\n" + str(titles[48]) + ". " + str(titles[49]) + " scored a " + str(titles[50]) + "\n" + str(titles[51]) + ". " + str(titles[52]) + " scored a " + str(titles[53])
                            + "\n" + str(titles[54]) + ". " + str(titles[55]) + " scored a " + str(titles[56]) + "\n" + str(titles[57]) + ". " + str(titles[58]) + " scored a " + str(titles[59])
                            + "\n" + str(titles[60]) + ". " + str(titles[61]) + " scored a " + str(titles[62]) + "\n" + str(titles[63]) + ". " + str(titles[64]) + " scored a " + str(titles[65])
                            + "\n" + str(titles[66]) + ". " + str(titles[67]) + " scored a " + str(titles[68]) + "\n" + str(titles[69]) + ". " + str(titles[70]) + " scored a " + str(titles[71])
                            + "\n" + "25" + ". " + str(titles[73]) + " scored a " + str(titles[74]) + "\n" + "\n" + "*Requested by: {}*".format(ctx.author.display_name))


		# gives the top 25 characters, this includes the name and amount of favorites
        elif arg == "characters":

            for length in range(0, len(title)):
                titlelist.append(title[length]['name'])
                titlelist.append(title[length]['favorites'])
            titles = titlelist

            await ctx.send("**The current top 25 " + str(arg) + " on MyAnimeList**" + "\n"
                            + "\n" + "1. " + str(titles[0]) + " with " + str(titles[1]) + " favorites" + "\n" + "2. " + str(titles[2]) + " with " + str(titles[3]) + " favorites"
                            + "\n" + "3. " + str(titles[4]) + " with " + str(titles[5]) + " favorites" + "\n" + "4. " + str(titles[6]) + " with " + str(titles[7]) + " favorites"
                            + "\n" + "5. " + str(titles[8]) + " with " + str(titles[9]) + " favorites" + "\n" + "6. " + str(titles[10]) + " with " + str(titles[11]) + " favorites"
                            + "\n" + "7. " + str(titles[12]) + " with " + str(titles[13]) + " favorites" + "\n" + "8. " + str(titles[14]) + " with " + str(titles[15]) + " favorites"
                            + "\n" + "9. " + str(titles[16]) + " with " + str(titles[17]) + " favorites" + "\n" + "10. " + str(titles[18]) + " with " + str(titles[19]) + " favorites"
                            + "\n" + "11. " + str(titles[20]) + " with " + str(titles[21]) + " favorites" + "\n" + "12. " + str(titles[22]) + " with " + str(titles[23]) + " favorites"
                            + "\n" + "13. " + str(titles[24]) + " with " + str(titles[25]) + " favorites" + "\n" + "14. " + str(titles[26]) + " with " + str(titles[27]) + " favorites"
                            + "\n" + "15. " + str(titles[28]) + " with " + str(titles[29]) + " favorites" + "\n" + "16. " + str(titles[30]) + " with " + str(titles[31]) + " favorites"
                            + "\n" + "17. " + str(titles[32]) + " with " + str(titles[33]) + " favorites" + "\n" + "18. " + str(titles[34]) + " with " + str(titles[35]) + " favorites"
                            + "\n" + "19. " + str(titles[36]) + " with " + str(titles[37]) + " favorites" + "\n" + "20. " + str(titles[38]) + " with " + str(titles[39]) + " favorites"
                            + "\n" + "21. " + str(titles[40]) + " with " + str(titles[41]) + " favorites" + "\n" + "22. " + str(titles[42]) + " with " + str(titles[43]) + " favorites"
                            + "\n" + "23. " + str(titles[44]) + " with " + str(titles[45]) + " favorites" + "\n" + "24. " + str(titles[46]) + " with " + str(titles[47]) + " favorites"
                            + "\n" + "25. " + str(titles[48]) + " with " + str(titles[49]) + " favorites" + "\n" + "\n" + "*Requested by: {}*".format(ctx.author.display_name))


		# gives the top 25 anime, this includes the name and amount of favorites
        elif arg == "people":

            for length in range(0, len(title)):
                titlelist.append(title[length]['name'])
                titlelist.append(title[length]['favorites'])
            titles = titlelist

            await ctx.send("**The current top 25 " + str(arg) + " on MyAnimeList**" + "\n"
                            + "\n" + "1. " + str(titles[0]) + " with " + str(titles[1]) + " favorites" + "\n" + "2. " + str(titles[2]) + " with " + str(titles[3]) + " favorites"
                            + "\n" + "3. " + str(titles[4]) + " with " + str(titles[5]) + " favorites" + "\n" + "4. " + str(titles[6]) + " with " + str(titles[7]) + " favorites"
                            + "\n" + "5. " + str(titles[8]) + " with " + str(titles[9]) + " favorites" + "\n" + "6. " + str(titles[10]) + " with " + str(titles[11]) + " favorites"
                            + "\n" + "7. " + str(titles[12]) + " with " + str(titles[13]) + " favorites" + "\n" + "8. " + str(titles[14]) + " with " + str(titles[15]) + " favorites"
                            + "\n" + "9. " + str(titles[16]) + " with " + str(titles[17]) + " favorites" + "\n" + "10. " + str(titles[18]) + " with " + str(titles[19]) + " favorites"
                            + "\n" + "11. " + str(titles[20]) + " with " + str(titles[21]) + " favorites" + "\n" + "12. " + str(titles[22]) + " with " + str(titles[23]) + " favorites"
                            + "\n" + "13. " + str(titles[24]) + " with " + str(titles[25]) + " favorites" + "\n" + "14. " + str(titles[26]) + " with " + str(titles[27]) + " favorites"
                            + "\n" + "15. " + str(titles[28]) + " with " + str(titles[29]) + " favorites" + "\n" + "16. " + str(titles[30]) + " with " + str(titles[31]) + " favorites"
                            + "\n" + "17. " + str(titles[32]) + " with " + str(titles[33]) + " favorites" + "\n" + "18. " + str(titles[34]) + " with " + str(titles[35]) + " favorites"
                            + "\n" + "19. " + str(titles[36]) + " with " + str(titles[37]) + " favorites" + "\n" + "20. " + str(titles[38]) + " with " + str(titles[39]) + " favorites"
                            + "\n" + "21. " + str(titles[40]) + " with " + str(titles[41]) + " favorites" + "\n" + "22. " + str(titles[42]) + " with " + str(titles[43]) + " favorites"
                            + "\n" + "23. " + str(titles[44]) + " with " + str(titles[45]) + " favorites" + "\n" + "24. " + str(titles[46]) + " with " + str(titles[47]) + " favorites"
                            + "\n" + "25. " + str(titles[48]) + " with " + str(titles[49]) + " favorites" + "\n" + "\n" + "*Requested by: {}*".format(ctx.author.display_name))


		# gives the top 10 anime, this includes the username, title, total score and amount of votes
        elif arg == "reviews":
            
            for length in range(0, len(title)):
                titlelist.append(title[length]['user']['username'])
                titlelist.append(title[length]['entry']['title'])
                titlelist.append(title[length]['scores']['overall'])
                titlelist.append(title[length]['votes'])
            titles = titlelist

            await ctx.send("**The current top 10 reviews " + str(arg) + " on MyAnimeList**" + "\n"
                                        + "\n" + "1. " + str(titles[0]) + " on " + str(titles[1]) + " scored a " + str(titles[2]) + " with " + str(titles[3]) + " votes" 
                                        + "\n" + "2. " + str(titles[4]) + " on " + str(titles[5]) + " scored a " + str(titles[6]) + " with " + str(titles[7]) + " votes" 
                                        + "\n" + "3. " + str(titles[8]) + " on " + str(titles[9]) + " scored a " + str(titles[10]) + " with " + str(titles[11]) + " votes" 
                                        + "\n" + "4. " + str(titles[12]) + " on " + str(titles[13]) + " scored a " + str(titles[14]) + " with " + str(titles[15]) + " votes" 
                                        + "\n" + "5. " + str(titles[16]) + " on " + str(titles[17]) + " scored a " + str(titles[18]) + " with " + str(titles[19]) + " votes" 
                                        + "\n" + "6. " + str(titles[20]) + " on " + str(titles[21]) + " scored a " + str(titles[22]) + " with " + str(titles[23]) + " votes" 
                                        + "\n" + "7. " + str(titles[24]) + " on " + str(titles[25]) + " scored a " + str(titles[26]) + " with " + str(titles[27]) + " votes" 
                                        + "\n" + "8. " + str(titles[28]) + " on " + str(titles[29]) + " scored a " + str(titles[30]) + " with " + str(titles[31]) + " votes" 
                                        + "\n" + "9. " + str(titles[32]) + " on " + str(titles[33]) + " scored a " + str(titles[34]) + " with " + str(titles[35]) + " votes" 
                                        + "\n" + "10. " + str(titles[36]) + " on " + str(titles[37]) + " scored a " + str(titles[38]) + " with " + str(titles[39]) + " votes" + "\n" + "\n" + "*Requested by: {}*".format(ctx.author.display_name))

    # if argument has been used wrong it triggers the MissingRequiredArgument below
    @top.error
    async def top_error(self,ctx,error):
        if isinstance(error,(MissingRequiredArgument)):
            if ctx.guild:
                await ctx.send('Woopsie! use .top <anime, manga, characters, people or reviews>')
            else:
        	    return


# adding cog to bot setup
def setup(bot):
    bot.add_cog(Top(bot))
