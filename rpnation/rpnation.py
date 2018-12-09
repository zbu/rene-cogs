import discord
import re
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
    async def rpnation(self, nation):
        """Force RP Nation Data"""

        #Your code will go here
        url = "https://slink.be/rp/index.php?nation=" + nation + "&submit=null" #build the web adress
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            online = soupObject.get_text()
			s = re.sub('<br\s*?>', '\n', online)
            await self.bot.say(s)
        except:
            await self.bot.say("ERROR.")

def setup(bot):
    bot.add_cog(nsextras(bot))