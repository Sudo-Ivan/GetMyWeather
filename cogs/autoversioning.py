import discord
from discord.ext import commands

class AutoVersioning(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.version = "1.0.0"

    @commands.Cog.listener()
    async def on_ready(self):
        print("AutoVersioning is ready.")

    @commands.hybrid_command()
    async def version(self, ctx):
        await ctx.send(f"Current version is {self.version}")

    @commands.hybrid_command()
    async def update(self, ctx):
        self.version = "1.0.1"
        await ctx.send(f"Updated version to {self.version}")

def setup(bot):
    bot.add_cog(AutoVersioning(bot))
