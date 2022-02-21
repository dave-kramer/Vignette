import discord

from discord.ext import commands


class Commands(commands.Cog):
    
    def __init__(self, client):
        self.client = client
    
    @commands.command(name='commands')
    async def commands(self, ctx, arg=None):
        if arg is None:
            embed = discord.Embed(title=f"Commands", color=0x87CEEB)

            embed.add_field(name=".anime ```name``` or use .manga .character .person .producer .magazine", value="Returns information about your anime, manga and so on.\n`Example: .anime shingeki`", inline=False)
            embed.add_field(name=".user ```name```", value="Returns user information with buttons for about, clubs, favorites, friends, history, recommendations, reviews, statistics or userupdates.\n`Example: .user davekramer", inline=False)
            embed.add_field(name=".random <anime, manga, characters, people, users>", value="Returns a random anime, manga, character, people or user from MyAnimeList.\n`Example: .random manga`", inline=False)
            embed.add_field(name=".top <anime, manga, characters, people, reviews>", value="Returns the current top 25 from MyAnimeList.\n`Example: .top characters`", inline=False)
            embed.add_field(name=".season <summer, fall, winter, spring, later> <year>", value="Returns the anime to release for that season and year.\n`Example: .anime fall 2022`", inline=False)
            embed.add_field(name=".notify ```name```", value="Add an anime and receive a notification when it airs.\n`Example: .notify Death Note`", inline=False)
            embed.add_field(name=".delete ```name```", value="Remove an airing anime.\n`Example: .remove Death Note`", inline=False)
            embed.add_field(name=".airlist ```name```", value="Returns the notification list for your airing or upcoming anime.\n`Example: .airlist`", inline=False)
            embed.add_field(name=".trace <url>", value="Uses trace.moe API to find the correct anime to your image.\n`Example: .trace url.com/blabla.png`", inline=False)
            embed.add_field(name=".waifu <argument>", value="Uses waifu.pics API to return a waifu or maid, use .command waifu for more info\n`Example: .waifu cry`", inline=False)
            embed.add_field(name=".quote", value="Uses animechan API to return an anime quote.\n`Example: .quote`", inline=False)
            embed.add_field(name=".watch <recent, popular>", value="Returns recent or popular top 25 to watch.\n`Example: .watch recent`", inline=False)
            embed.add_field(name=".recommendation <anime, manga>", value="Returns random recommendation from MyAnimeList.\n`Example: .recommendation anime`", inline=False)
            embed.add_field(name=".schedule <today, monday, tuesday, wednesday, thursday, friday, saturday, sunday>", value="Returns schedule of a certain day.\n`Example: .schedule today`", inline=False)
            embed.add_field(name=".trailer <recent, popular>", value="Returns recent or popular trailers BEING WORKED ON.\n`Example: .trailer recent`", inline=False)
            embed.add_field(name=".trivia <easy, medium, hard> <1-5>", value="Uses opentdb for true or false anime trivia.\n`Example: .trivia medium 5`", inline=False)
            embed.add_field(name=".guess <anime, char>", value="Guess the Anime & Character game\n`Example: .guess char`", inline=False)
            embed.add_field(name=".leaderboards", value="Leaderboard for Guess the Character.\n`Example: .leaderboards`", inline=False)
            embed.add_field(name=".info", value="More information about Vignette\n`Example: .info`", inline=False)
            embed.add_field(name=".commands", value="Returns this commands list.\n`Example: .commands`", inline=False)
            embed.add_field(name=".commands waifu", value="Returns commands list with more info on the waifu command.\n`Example: .commands waifu`", inline=False)

            await ctx.author.send(embed=embed)

        elif arg == "waifu":
            embed = discord.Embed(title=f".waifu <argument>", color=0x87CEEB)
            embed.add_field(name="Arguments", value="`neko, shinobu, megumin, bully, cuddle, cry, hug, awoo, kiss, lick, pat, smug, bonk, yeet, blush, smile, wave, highfive, handhold, nom, bite, glomp, slap, kill, kick, happy, wink, poke, dance, cringe`", inline=False)
            embed.add_field(name="Example", value="`.waifu cuddle`", inline=False)
            await ctx.author.send(embed=embed)
        
        else:
            await ctx.send('Woopsie! use .commands or .commands waifu')


# adding cog to bot setup
def setup(bot):
    bot.add_cog(Commands(bot))