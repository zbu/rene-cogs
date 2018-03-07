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
    async def rmbpost(self, ctx, id):
        """Displays Specified RMB Post Text"""

        #Your code will go here
        url = "https://www.nationstates.net/page=rmb/postid=" + id #build the web adress
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            online = soupObject.find(class_='rmbmsg2-container').get_text()
            nation = soupObject.find(class_='nname').get_text()
            datetime = soupObject.find('time').get_text()
            flagpic = soupObject.find(class_='rmbdate').find('img').attrs['src']
            description = online
            footer_text = "Last active " + datetime
            embed.title = "RMB Post"
            embed.set_author(name=nation, url="https://nationstates.net/" + nation)
            embed.set_thumbnail(url="https://nationstates.net" + flagpic)
            embed.set_footer(text=footer_text)
            embed = discord.Embed(colour=0xCEFF00, description=description)
            await self.bot.say(embed=embed)
        except:
            await self.bot.say("This RMB Post does not exist.")
def setup(bot):
    bot.add_cog(nsextras(bot))