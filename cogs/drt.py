import math
import discord
from discord.ext import commands

class DRT(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command()
    async def distance(self, ctx, rate: float, time: float):
        distance = rate * time
        await ctx.send(f"Distance traveled: {distance:.2f} nautical miles.")

    @commands.hybrid_command()
    async def time(self, ctx, distance: float, rate: float):
        time = distance / rate
        await ctx.send(f"Time to travel the distance: {time:.2f} hours.")

    @commands.hybrid_command()
    async def rate(self, ctx, distance: float, time: float):
        rate = distance / time
        await ctx.send(f"Rate of travel: {rate:.2f} knots.")

async def setup(bot):
    await bot.add_cog(DRT(bot))
