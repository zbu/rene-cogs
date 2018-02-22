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
    async def twcr(self):
        """Today's World Census Report"""

        #Your code will go here
        url = "https://www.nationstates.net/page=world" #build the web adress
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            online = soupObject.find('h3').get_text()
            await self.bot.say(online + " is today's World Census Report")
        except:
            await self.bot.say("ERROR.")

def setup(bot):
    bot.add_cog(nsextras(bot))