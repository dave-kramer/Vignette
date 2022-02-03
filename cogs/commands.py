import discord

from discord.ext import commands


class Commands(commands.Cog):
    
    def __init__(self, client):
        self.client = client
    
    @commands.command(name='commands')
    async def commands(self, ctx, arg=None):
        if arg is None:
            embed = discord.Embed(title=f"Commands", color=0x87CEEB)

            embed.add_field(name=".anime ```name``` or use .manga .character .person .producer .magazine", value="Returns information about your anime, manga and so on.\n```Example: .anime shingeki```", inline=False)
            embed.add_field(name=".user ```name``` <about, clubs, favorites, friends, history, recommendations, reviews, statistics, userupdates>", value="Returns user information, check on the user statistics, update or their about page.\n```Example: .user davekramer or .user davekramer history```", inline=False)
            embed.add_field(name=".random <anime, manga, characters, people, users>", value="Returns a random anime, manga, character, people or user from MyAnimeList.\n```Example: .random manga```", inline=False)
            embed.add_field(name=".top <anime, manga, characters, people, reviews>", value="Returns the current top from MyAnimeList.\n```Example: .top characters```", inline=False)
            embed.add_field(name=".season <summer, fall, winter, spring, later> <year>", value="Returns the anime to release for that season and year.\n```Example: .anime fall 2022```", inline=False)
            embed.add_field(name=".trace <url>", value="Uses trace.moe API to find the correct anime to your image.\n```Example: .trace url.com/blabla.png```", inline=False)
            embed.add_field(name=".waifu <argument>", value="Uses waifu.pics API to return a waifu or maid, use .command waifu for more info\n```Example: .waifu cry```", inline=False)
            embed.add_field(name=".quote", value="Uses animechan API to return an anime quote.\n```Example: .quote```", inline=False)
            embed.add_field(name=".watch <recent, popular>", value="Returns recent or popular top 25 to watch BEING WORKED ON.\n```Example: .watch recent```", inline=False)
            embed.add_field(name=".recommendations <anime, manga>", value="Returns user recommendations on certain anime or manga BEING WORKED ON.\n```Example: .recommendations anime```", inline=False)
            embed.add_field(name=".schedule <today, monday, tuesday, wednesday, thursday, friday, saturday, sunday>", value="Returns schedule of a certain day BEING WORKED ON.\n```Example: .schedule today```", inline=False)
            embed.add_field(name=".trailer <recent, popular>", value="Returns recent or popular trailers BEING WORKED ON.\n```Example: .trailer recent```", inline=False)
            embed.add_field(name=".commands", value="Returns this commands list.\n```Example: .commands```", inline=False)

            await ctx.author.send(embed=embed)

        elif arg == "waifu":
            embed = discord.Embed(title=f".waifu <argument>", color=0x87CEEB)
            embed.add_field(name="Arguments", value="```neko, shinobu, megumin, bully, cuddle, cry, hug, awoo, kiss, lick, pat, smug, bonk, yeet, blush, smile, wave, highfive, handhold, nom, bite, glomp, slap, kill, kick, happy, wink, poke, dance, cringe```", inline=False)
            embed.add_field(name="Example", value="```.waifu cuddle```", inline=False)
            await ctx.author.send(embed=embed)
        
        else:
            await ctx.send('Woopsie! use .commands or .commands waifu')


# adding cog to bot setup
def setup(bot):
    bot.add_cog(Commands(bot))