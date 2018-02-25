import discord
from discord.ext import commands
try: # check if BeautifulSoup4 is installed
    from bs4 import BeautifulSoup
    soupAvailable = True
except:
    soupAvailable = False
import aiohttp

class nsextras:
    """NS Extras"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def tpd(self, region):
        """A region's top pinned dispatch."""

        #Your code will go here
        url = "https://www.nationstates.net/region=" + region #build the web adress
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            dispatchname = soupObject.find(class_='dispatchlist').find('li').find('h3').find('a').get_text()
            dispatchauthor = soupObject.find(class_='dispatchlist').find('li').find(class_='dispatchauthorline').find('a').find('span').get_text()
			await self.bot.say(dispatchname + " by " + dispatchauthor)
        except:
            await self.bot.say("This region has no pinned dispatches.")

def setup(bot):
    bot.add_cog(nsextras(bot))