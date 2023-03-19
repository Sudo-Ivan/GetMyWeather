import math
import discord
from discord.ext import commands

class Converter(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(name="wind_at_altitude")
    async def wind_at_altitude(self, ctx, altitude: float, wind_speed: float, wind_direction: float):
        wind_speed, wind_direction = wind_at_altitude(altitude, wind_speed, wind_direction)
        await ctx.send(f"Wind Speed: {wind_speed}, Wind Direction: {wind_direction}")

    # ... Define the rest of the commands similarly, for each of the functions ...

# Add this at the end of the converter.py file
async def setup(bot):
    await bot.add_cog(Converter(bot))

