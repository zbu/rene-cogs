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
    async def tnos(self):
        """Today's featured region"""

        #Your code will go here
        url = "https://www.nationstates.net/page=world" #build the web adress
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            online = soupObject.find(href_='page=list_nations').get_text()
            await self.bot.say(online + " total nations")
        except:
            await self.bot.say("ERROR.")
        try:
            online2 = soupObject.find(href_='page=list_regions').get_text()
            await self.bot.say(online2 + " total regions")
        except:
            await self.bot.say("ERROR.")

def setup(bot):
    bot.add_cog(nsextras(bot))