import discord
from discord.ext import commands
from .utils import checks

class nsextras:
    """NS Extras"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @checks.admin_or_permissions(manage_server=True)
    async def say(self, channel, *, text):
        """Displays what is said after say"""

        #Your code will go here
        c = discord.utils.get(server.channels, name=channel)
        await self.bot.send_message(c, text)

def setup(bot):
    bot.add_cog(nsextras(bot))