import discord
from discord.ext import commands

class nsextras:
    """NS Extras"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def say(self, text):
        """Displays what is said after say"""

        #Your code will go here
        await self.bot.say(text)

def setup(bot):
    bot.add_cog(nsextras(bot))