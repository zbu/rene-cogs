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
    async def rpnation(self, *, sort):
        """Force RP Ranking Info"""

        #Your code will go here
        url = "https://iloo.cc/rp/discordranksapi.php?sort=" + sort #build the web adress
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            online = soupObject.get_text()
            await self.bot.say(online)
        except:
            await self.bot.say("ERROR.")

def setup(bot):
    bot.add_cog(nsextras(bot))