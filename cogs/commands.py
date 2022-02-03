import discord

from discord.ext import commands


class Commands(commands.Cog):
    
    def __init__(self, client):
        self.client = client
    
    @commands.command(name='commands')
    async def commands(self, ctx):
        
        embed = discord.Embed(title=f"Commands", color=0x87CEEB)

        embed.add_field(name=".anime ```name``` or use .manga .character .person .producer .magazine", value="Returns information about your anime, manga and so on.\nExample: .anime shingeki", inline=False)
        embed.add_field(name=".user ```name``` <about, clubs, favorites, friends, history, recommendations, reviews, statistics, userupdates>", value="Returns user information, check on the user statistics, update or their about page.\nExample: .user davekramer or .user davekramer history", inline=False)
        embed.add_field(name=".random <anime, manga, characters, people, users>", value="Returns a random anime, manga, character, people or user from MyAnimeList.\nExample: .random manga", inline=False)
        embed.add_field(name=".top <anime, manga, characters, people, reviews>", value="Returns the current top from MyAnimeList.\nExample: .top characters", inline=False)
        embed.add_field(name=".season <summer, fall, winter, spring, later> <year>", value="Returns the anime to release for that season and year.\nExample: .anime fall 2022", inline=False)
        embed.add_field(name=".watch <recent, popular>", value="Returns recent or popular top 25 to watch BEING WORKED ON.\nExample: .watch recent", inline=False)
        embed.add_field(name=".recommendations <anime, manga>", value="Returns user recommendations on certain anime or manga BEING WORKED ON.\nExample: .recommendations anime", inline=False)
        embed.add_field(name=".schedule <today, monday, tuesday, wednesday, thursday, friday, saturday, sunday>", value="Returns schedule of a certain day BEING WORKED ON.\nExample: .schedule today", inline=False)
        embed.add_field(name=".trailer <recent, popular>", value="Returns recent or popular trailers BEING WORKED ON.\nExample: .trailer recent", inline=False)
        embed.add_field(name=".commands", value="Returns this commands list.\nExample: .commands", inline=False)

        await ctx.author.send(embed=embed)


# adding cog to bot setup
def setup(bot):
    bot.add_cog(Commands(bot))