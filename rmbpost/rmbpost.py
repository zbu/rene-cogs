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
            text = soupObject.find(class_='rmbmsg2-container').get_text()
            nation = soupObject.find(class_='nname').get_text()
            datetime = soupObject.find(class_='rmbdate').find('a').find('time').get_text()
            region = soupObject.find(class_='widebox').find('h2').find('a').get_text()
            footer_text = "Posted " + datetime
            await self.bot.say(region + " RMB" + "\n" + "by " + nation + "\n" + "" + "\n" + text + "\n" + "" + "\n" + footer_text)
        except:
            await self.bot.say("This RMB Post does not exist.")

def setup(bot):
    bot.add_cog(nsextras(bot))