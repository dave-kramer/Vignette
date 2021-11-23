import discord
import datetime

from aiohttp import request
from discord.ext import commands



class Watch(commands.Cog):
    def __init__(self, client):
        self.client = client
    description = "Gets the watch page from MyAnimeList"

    @commands.command(name='watch')
    async def watch(self, ctx, arg=None):
        '''Pulls the right data from MAL, checks the arguments needed to use the function correctly.
        '''
        if arg == "recent":
            URL = f"https://api.jikan.moe/v4/watch/episodes"
            URL2 = "https://myanimelist.net/watch/episode"
            setTitle = "Latest 25 released anime episodes on MyAnimeList"
            setImage = "http://static.zerochan.net/Tsukinose.Vignette.April.full.2657880.gif"
        elif arg == "popular":
            URL = f"https://api.jikan.moe/v4/watch/episodes/popular"
            URL2 = "https://myanimelist.net/watch/episode/popular"
            setTitle = "Latest 25 released popular anime episodes on MyAnimeList"
            setImage = "http://i.imgur.com/2KCjOZB.gif"
        elif arg is None:
            await ctx.send("I can only retrieve .watch <recent or popular>")
            return None
        else:
            await ctx.send("I can only retrieve .watch <recent or popular>")
            return None

        # Sents get request pulling the data
        async with request("GET", URL, headers={}) as response:
            if response.status == 200:
                databox = await response.json()
                data = databox["data"]

            # creates a list, loops through the data, adds it to the list
            # then splits it correctly, the "*" is used because there are anime
            # that uses the ","
            listdata = []
            for length in range(0,len(data)):
                listdata.append(data[length]['entry']['title']) # title
                listdata.append(data[length]['episodes'][0]['url']) # url to episode
                listdata.append(data[length]['episodes'][0]['title']) # episode
                listdata.append(data[length]['episodes'][0]['premium']) # premium true/false
            string = '*'.join([str(item) for item in listdata])
            x = string.split("*")

            # loops through the list while replacing True and False to Paid & Free
            for i, word in enumerate(x):
                if word == 'True':
                    x[i] = 'Paid'
                elif word == 'False':
                    x[i] = 'Free'

            # sents the full embed
            embed=discord.Embed(title=setTitle, url=URL2, description="\n" + "1. " + x[0] + " released " + x[2] + " and is " + x[3] + " to watch." + "\n" +
                                "2. " + x[4] + " released " + x[6] + " and is " + x[7] + " to watch." + "\n" + "3. " + x[8] + " released " + x[10] + " and is " + x[11] + " to watch." + "\n" +
                                "4. " + x[12] + " released " + x[14] + " and is " + x[15] + " to watch." + "\n" + "5. " + x[16] + " released " + x[18] + " and is " + x[19] + " to watch." + "\n" +
                                "6. " + x[20] + " released " + x[22] + " and is " + x[23] + " to watch." + "\n" + "7. " + x[24] + " released " + x[26] + " and is " + x[27] + " to watch." + "\n" +
                                "8. " + x[28] + " released " + x[30] + " and is " + x[31] + " to watch." + "\n" + "9. " + x[32] + " released " + x[34] + " and is " + x[35] + " to watch." + "\n" +
                                "10. " + x[36] + " released " + x[38] + " and is " + x[39] + " to watch." + "\n" + "11. " + x[40] + " released " + x[42] + " and is " + x[43] + " to watch." + "\n" +
                                "12. " + x[44] + " released " + x[46] + " and is " + x[47] + " to watch." + "\n" + "13. " + x[48] + " released " + x[50] + " and is " + x[51] + " to watch." + "\n" +
                                "14. " + x[52] + " released " + x[54] + " and is " + x[55] + " to watch." + "\n" + "15. " + x[56] + " released " + x[58] + " and is " + x[59] + " to watch." + "\n" +
                                "16. " + x[60] + " released " + x[62] + " and is " + x[63] + " to watch." + "\n" + "17. " + x[64] + " released " + x[66] + " and is " + x[67] + " to watch." + "\n" +
                                "18. " + x[68] + " released " + x[70] + " and is " + x[71] + " to watch." + "\n" + "19. " + x[72] + " released " + x[74] + " and is " + x[75] + " to watch." + "\n" +
                                "20. " + x[76] + " released " + x[78] + " and is " + x[79] + " to watch." + "\n" + "21. " + x[80] + " released " + x[82] + " and is " + x[83] + " to watch." + "\n" +
                                "22. " + x[84] + " released " + x[86] + " and is " + x[87] + " to watch." + "\n" + "23. " + x[88] + " released " + x[90] + " and is " + x[91] + " to watch." + "\n" +
                                "24. " + x[92] + " released " + x[94] + " and is " + x[95] + " to watch." + "\n" + "25. " + x[96] + " released " + x[98] + " and is " + x[99] + " to watch." + "\n" + "\n" + "**Note:** Country regulations still apply, so it might be still __paid__ for you and __free__ for others.", color=0xf37a12)
            embed.set_image(url=setImage)
            embed.set_footer(text="Requested by: {}".format(ctx.author.display_name), icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
            embed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=embed)

# adding cog to bot setup
def setup(bot):
    bot.add_cog(Watch(bot))
