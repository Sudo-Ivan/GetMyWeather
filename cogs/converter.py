import math
import discord
from discord.ext import commands

class Converter(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def convert_units(self, altitude, indicated_airspeed, wind_speed, unit):
        if unit == 'imperial':
            altitude *= 0.3048  # Convert feet to meters
            indicated_airspeed *= 0.514444  # Convert knots to m/s
            wind_speed *= 0.514444  # Convert knots to m/s
        return altitude, indicated_airspeed, wind_speed

    @commands.hybrid_command()
    async def wind_at_altitude(self, ctx, altitude: float, wind_speed: float, wind_direction: float, unit: str = 'metric'):
        altitude, indicated_airspeed, wind_speed = self.convert_units(altitude, 0, wind_speed, unit)
        wind_speed, wind_direction = wind_at_altitude(altitude, wind_speed, wind_direction)
        await ctx.send(f"Wind speed at {altitude} m is {wind_speed:.2f} m/s and wind direction is {wind_direction:.2f} degrees.")

    @commands.hybrid_command()
    async def true_airspeed(self, ctx, altitude: float, indicated_airspeed: float, wind_speed: float, wind_direction: float, unit: str = 'metric'):
        altitude, indicated_airspeed, wind_speed = self.convert_units(altitude, indicated_airspeed, wind_speed, unit)
        tas = true_airspeed(altitude, indicated_airspeed, wind_speed, wind_direction)
        await ctx.send(f"True airspeed at {altitude} m is {tas:.2f} m/s.")

    @commands.hybrid_command()
    async def ground_speed(self, ctx, altitude: float, indicated_airspeed: float, wind_speed: float, wind_direction: float, unit: str = 'metric'):
        altitude, indicated_airspeed, wind_speed = self.convert_units(altitude, indicated_airspeed, wind_speed, unit)
        gs = ground_speed(altitude, indicated_airspeed, wind_speed, wind_direction)
        await ctx.send(f"Ground speed at {altitude} m is {gs:.2f} m/s.")

    @commands.hybrid_command()
    async def wind_component(self, ctx, altitude: float, indicated_airspeed: float, wind_speed: float, wind_direction: float, unit: str = 'metric'):
        altitude, indicated_airspeed, wind_speed = self.convert_units(altitude, indicated_airspeed, wind_speed, unit)
        wc = wind_component(altitude, indicated_airspeed, wind_speed, wind_direction)
        await ctx.send(f"Wind component at {altitude} m is {wc:.2f} m/s.")

    @commands.hybrid_command()
    async def drift_angle(self, ctx, altitude: float, indicated_airspeed: float, wind_speed: float, wind_direction: float, unit: str = 'metric'):
        altitude, indicated_airspeed, wind_speed = self.convert_units(altitude, indicated_airspeed, wind_speed, unit)
        da = drift_angle(altitude, indicated_airspeed, wind_speed, wind_direction)
        await ctx.send(f"Drift angle at {altitude} m is {da:.2f} degrees.")

    @commands.hybrid_command()
    async def drift_distance(self, ctx, altitude: float, indicated_airspeed: float, wind_speed: float, wind_direction: float, unit: str = 'metric'):
        altitude, indicated_airspeed, wind_speed = self.convert_units(altitude, indicated_airspeed, wind_speed, unit)
        dd = drift_distance(altitude, indicated_airspeed, wind_speed, wind_direction)
        await ctx.send(f"Drift distance at {altitude} m is {dd:.2f}.")

    @commands.hybrid_command()
    async def glide_ratio(self, ctx, altitude: float, indicated_airspeed: float, wind_speed: float, wind_direction: float, unit: str = 'metric'):
        altitude, indicated_airspeed, wind_speed = self.convert_units(altitude, indicated_airspeed, wind_speed, unit)
        gr = glide_ratio(altitude, indicated_airspeed, wind_speed, wind_direction)
        await ctx.send(f"Glide ratio at {altitude} m is {gr:.2f}.")

    @commands.hybrid_command()
    async def time_to_altitude(self, ctx, altitude: float, indicated_airspeed: float, wind_speed: float, wind_direction: float, unit: str = 'metric'):
        altitude, indicated_airspeed, wind_speed = self.convert_units(altitude, indicated_airspeed, wind_speed, unit)
        tta = time_to_altitude(altitude, indicated_airspeed, wind_speed, wind_direction)
        await ctx.send(f"Time to reach {altitude} m is {tta:.2f} seconds.")

async def setup(bot):
    await bot.add_cog(Converter(bot))
