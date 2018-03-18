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

    @commands.command(pass_context=True)
    async def rmbpost(self, id):
        """Displays Specified RMB Post Text"""

        #Your code will go here
        url = "https://www.nationstates.net/page=rmb/postid=" + id #build the web adress
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
		try:
            online = soupObject.find(class_='rmbmsg2-container').get_text()
            nation = soupObject.find(class_='nname').get_text()
            datetime = soupObject.find(class_='rmbdate').find('a').find('time').get_text()
            footer_text = "Posted " + datetime
            embed.set_author(name=nation, url="https://nationstates.net/" + nation)
            await self.bot.say("RMB Post by " + nation + "\n" + online + "\n" + footer_text)
def setup(bot):
    bot.add_cog(nsextras(bot))