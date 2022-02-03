from aiohttp import request
from discord.ext import commands
from discord.ext.commands import MissingRequiredArgument


class Quote(commands.Cog):

    def __init__(self, client):
        self.client = client
    description = "Returns a random anime quote."

    @commands.command(name='quote')
    async def quote(self, ctx):
        '''Returns a random anime quote from the animechan.vercel.app API
        '''
        URL = f"https://animechan.vercel.app/api/random"
        
        async with request("GET", URL, headers={}) as response:
            if response.status == 200:
                data = await response.json()
                await ctx.send(f"*{data['quote']}*\n**{data['character']}** from {data['anime']}")
            else:
                await ctx.send(f"Server is currently down, try again later.")

    @quote.error
    async def quote_error(self, ctx, error):
        if isinstance(error, (MissingRequiredArgument)):
            if ctx.guild:
                await ctx.send('Try a quote by typing: .quote')
            else:
                return


# adding cog to bot setup
def setup(bot):
	bot.add_cog(Quote(bot))