import discord
from discord.ext import commands

class nsextras:
    """NS Extras"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def map(self):
        """TNP Map Info"""

        #Your code will go here
        await self.bot.say('Eras (Forum RP) Map Claims Topic: http://forum.thenorthpacific.org/topic/9003207/findpost/10002391/' + "\n" + 'Strangereal (RMB RP) Map Factbook: https://www.nationstates.net/nation=puczovska/detail=factbook/id=847939' + "\n" + 'Strangereal (RMB RP) Climate Map Factbook: https://www.nationstates.net/nation=lungha/detail=factbook/id=977871')

def setup(bot):
    bot.add_cog(nsextras(bot))