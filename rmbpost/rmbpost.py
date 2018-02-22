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
    async def rmbpost(self, id):
        """Displays Specified RMB Post Text"""

        #Your code will go here
        url = "https://www.nationstates.net/page=rmb/postid=" + id #build the web adress
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            online = soupObject.find(class_='rmbrow odd post-' + id).find(class_="rmbmsg2-container-main").get_text()
            nation = soupObject.find(class_='nname').get_text()
            await self.bot.say("From: " + nation + "\nText: " + online)
        except:
            online = soupObject.find(class_='rmbrow even post-' + id).find(class_="rmbmsg2-container-main").get_text()
            nation = soupObject.find(class_='nname').get_text()
            await self.bot.say("From: " + nation + "\nText: " + online)

def setup(bot):
    bot.add_cog(nsextras(bot))