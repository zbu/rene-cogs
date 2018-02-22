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
    async def rmbpostadvanced(self, region, id, startpost):
        """Displays Specified RMB Post Text"""

        #Your code will go here
        url = "https://www.nationstates.net/page=display_region_rmb/region=" +region + "?start=" + startpost #build the web adress
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            online = soupObject.find(class_='rmbrow odd post-' + id).find(class_="rmbmsg2-container-main").get_text()
            await self.bot.say("RMB Post: " + online)
        except:
            online = soupObject.find(class_='rmbrow even post-' + id).find(class_="rmbmsg2-container-main").get_text()
            await self.bot.say("RMB Post: " + online)

def setup(bot):
    bot.add_cog(nsextras(bot))