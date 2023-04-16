import math
import discord
from discord.ext import commands

class DRT(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(description="calculate the distance flown.")
    async def distance(self, ctx, rate: float, time: float, unit_system: str = "aviation"):
        distance = rate * time
        if unit_system.lower() == "metric":
            distance *= 1.852  # Convert nautical miles to kilometers
            unit = "kilometers"
        else:
            unit = "nautical miles"

        await ctx.send(f"Distance traveled: {distance:.2f} {unit}.")

    @commands.hybrid_command(description="calculate the time to reach destination.")
    async def time(self, ctx, distance: float, rate: float, unit_system: str = "aviation"):
        if unit_system.lower() == "metric":
            distance /= 1.852  # Convert kilometers to nautical miles

        time = distance / rate
        await ctx.send(f"Time to travel the distance: {time:.2f} hours.")

    @commands.hybrid_command(description="calculate the rate using knots.")
    async def rate(self, ctx, distance: float, time: float, unit_system: str = "aviation"):
        if unit_system.lower() == "metric":
            distance /= 1.852  # Convert kilometers to nautical miles

        rate = distance / time
        if unit_system.lower() == "metric":
            rate *= 1.852  # Convert knots to kilometers per hour
            unit = "km/h"
        else:
            unit = "knots"

        await ctx.send(f"Rate of travel: {rate:.2f} {unit}.")

async def setup(bot):
    await bot.add_cog(DRT(bot))
