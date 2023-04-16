import math
import discord
from discord.ext import commands

    @commands.hybrid_command()
    async def wind_correction(self, ctx, tas: float, wind_speed: float, wind_direction: float, course: float):
        wind_angle = wind_direction - course
        wca = math.asin(wind_speed * math.sin(math.radians(wind_angle)) / tas)
        gs = tas * math.cos(wca) + wind_speed * math.cos(math.radians(wind_angle))
        wca = math.degrees(wca)

        embed = discord.Embed(title="Wind Correction", color=discord.Color.blue())
        embed.add_field(name="Wind Correction Angle", value=f"{wca:.2f}°")
        embed.add_field(name="Ground Speed", value=f"{gs:.2f} knots")
        await ctx.send(embed=embed)

    @commands.hybrid_command()
    async def true_airspeed(self, ctx, ias: float, altitude: float, temperature: float):
        # Assuming temperature in Celsius, altitude in feet
        tas = ias * math.sqrt((273 + temperature) / (273 + (15 - 2 * altitude / 1000)))

        embed = discord.Embed(title="True Airspeed", color=discord.Color.blue())
        embed.add_field(name="True Airspeed", value=f"{tas:.2f} knots")
        await ctx.send(embed=embed)

    @commands.hybrid_command()
    async def density_altitude(self, ctx, pressure_altitude: float, temperature: float):
        # Assuming temperature in Celsius
        density_altitude = pressure_altitude + (120 * (temperature - 15))

        embed = discord.Embed(title="Density Altitude", color=discord.Color.blue())
        embed.add_field(name="Density Altitude", value=f"{density_altitude:.2f} ft")
        await ctx.send(embed=embed)

    @commands.hybrid_command()
    async def pressure_altitude(self, ctx, altimeter_setting: float, altitude: float):
        pressure_altitude = (29.92 - altimeter_setting) * 1000 + altitude

        embed = discord.Embed(title="Pressure Altitude", color=discord.Color.blue())
        embed.add_field(name="Pressure Altitude", value=f"{pressure_altitude:.2f} ft")
        await ctx.send(embed=embed)

    @commands.hybrid_command()
    async def wind_components(self, ctx, wind_speed: float, wind_direction: float, runway_heading: float):
        wind_angle = wind_direction - runway_heading
        headwind = wind_speed * math.cos(math.radians(wind_angle))
        crosswind = wind_speed * math.sin(math.radians(wind_angle))

        embed = discord.Embed(title="Wind Components", color=discord.Color.blue())
        embed.add_field(name="Headwind", value=f"{headwind:.2f} knots")
        embed.add_field(name="Crosswind", value=f"{crosswind:.2f} knots")
        await ctx.send(embed=embed)

    @commands.hybrid_command()
    async def time_distance(self, ctx, speed: float = None, time: float = None, distance: float = None):
        if speed is not None and time is not None:
            distance = speed * time
            await ctx.send(f"Distance: {distance:.2f} nm")
        elif speed is not None and distance is not None:
            time = distance / speed
            await ctx.send(f"Time: {time:.2f} hours")
        elif time is not None and distance is not None:
            speed = distance / time
            await ctx.send(f"Speed: {speed:.2f} knots")

    @commands.hybrid_command()
    async def climb_descent_rate(self, ctx, distance: float, altitude_change: float, angle: float):
        rate = (altitude_change / distance) * math.tan(math.radians(angle)) * 60

        await ctx.send(f"Climb/Descent rate: {rate:.2f} ft/min")
    
    @commands.hybrid_command()
    async def fuel_consumption(self, ctx, flight_time: float, fuel_quantity: float):
        fuel_rate = fuel_quantity / flight_time
        fuel_required = flight_time * fuel_rate

        await ctx.send(f"Fuel consumption rate: {fuel_rate:.2f} per hour, Fuel required: {fuel_required:.2f}")

    @commands.hybrid_command()
    async def endurance(self, ctx, fuel_quantity: float, fuel_rate: float):
        endurance = fuel_quantity / fuel_rate

        await ctx.send(f"Endurance: {endurance:.2f} hours")

async def setup(bot):
    await bot.add_cog(E6B(bot))
    