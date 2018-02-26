import discord
from discord.ext import commands

class nsextras:
    """NS Extras"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    @checks.admin_or_permissions(manage_server=True)
    async def say(self, ctx, channel, *, text):
        """Displays what is said after say"""
        server = ctx.message.server

        #Your code will go here
        c = discord.utils.get(server.channels, name=channel)
        await self.bot.send_message(c, text)

def setup(bot):
    bot.add_cog(nsextras(bot))