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
    async def rpbudget(self, key, education, welfare, defense, healthcare, industry, lawandorder, infrastructure, administration, taxrate, *, nation):
        """Force RP Nation Budget Update Tool. This won't work unless you are logged into your NS nation. Access the key here: https://www.nationstates.net/page=verify_login?token=fieiJHRjf8r3JR"""

        #Your code will go here
        nation.replace(" ", "_")
        url = "https://slink.be/rp/discordnsverify.php?nation=" + nation + "&vkey=" + key + "&education=" + education + "&welfare=" + welfare + "&defense=" + defense + "&healthcare=" + healthcare + "&industry=" + industry + "&lawandorder=" + lawandorder + "&infrastructure=" + infrastructure + "&administration=" + administration + "&tax=" + taxrate #build the web adress
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            online = soupObject.get_text()
            await self.bot.say(online)
        except:
            await self.bot.say("ERROR.")

def setup(bot):
    bot.add_cog(nsextras(bot))