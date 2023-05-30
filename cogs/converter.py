import math
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
        
    def wind_at_altitude(altitude, wind_speed, wind_direction):
    # Calculate the wind speed at the given altitude
    wind_speed = wind_speed * (1 - (2.25577 * 10 ** -5) * altitude) ** 5.25588
    # Calculate the wind direction at the given altitude
    wind_direction = wind_direction + (0.00066 * altitude)
    # Return the wind speed and direction at the given altitude
    return wind_speed, wind_direction

# calculate the true airspeed at a given altitude
def true_airspeed(altitude, indicated_airspeed, wind_speed, wind_direction):
    # Calculate the wind speed at the given altitude
    wind_speed = wind_speed * (1 - (2.25577 * 10 ** -5) * altitude) ** 5.25588
    # Calculate the wind direction at the given altitude
    wind_direction = wind_direction + (0.00066 * altitude)
    # Calculate the true airspeed at the given altitude
    true_airspeed = indicated_airspeed + wind_speed * math.cos(math.radians(wind_direction))
    # Return the true airspeed at the given altitude
    return true_airspeed

# calculate the ground speed at a given altitude
def ground_speed(altitude, indicated_airspeed, wind_speed, wind_direction):
    # Calculate the wind speed at the given altitude
    wind_speed = wind_speed * (1 - (2.25577 * 10 ** -5) * altitude) ** 5.25588
    # Calculate the wind direction at the given altitude
    wind_direction = wind_direction + (0.00066 * altitude)
    # Calculate the ground speed at the given altitude
    ground_speed = indicated_airspeed + wind_speed * math.sin(math.radians(wind_direction))
    # Return the ground speed at the given altitude
    return ground_speed

# calculate the wind component at a given altitude
def wind_component(altitude, indicated_airspeed, wind_speed, wind_direction):
    # Calculate the wind speed at the given altitude
    wind_speed = wind_speed * (1 - (2.25577 * 10 ** -5) * altitude) ** 5.25588
    # Calculate the wind direction at the given altitude
    wind_direction = wind_direction + (0.00066 * altitude)
    # Calculate the wind component at the given altitude
    wind_component = wind_speed * math.cos(math.radians(wind_direction))
    # Return the wind component at the given altitude
    return wind_component

#calculate drift angle
def drift_angle(altitude, indicated_airspeed, wind_speed, wind_direction):
    # Calculate the wind speed at the given altitude
    wind_speed = wind_speed * (1 - (2.25577 * 10 ** -5) * altitude) ** 5.25588
    # Calculate the wind direction at the given altitude
    wind_direction = wind_direction + (0.00066 * altitude)
    # Calculate the drift angle at the given altitude
    drift_angle = math.degrees(math.atan(wind_speed * math.sin(math.radians(wind_direction)) / (indicated_airspeed - wind_speed * math.cos(math.radians(wind_direction)))))
    # Return the drift angle at the given altitude
    return drift_angle

#calculate drift distance
def drift_distance(altitude, indicated_airspeed, wind_speed, wind_direction):
    # Calculate the wind speed at the given altitude
    wind_speed = wind_speed * (1 - (2.25577 * 10 ** -5) * altitude) ** 5.25588
    # Calculate the wind direction at the given altitude
    wind_direction = wind_direction + (0.00066 * altitude)
    # Calculate the drift distance at the given altitude
    drift_distance = (wind_speed * math.sin(math.radians(wind_direction))) / (indicated_airspeed - wind_speed * math.cos(math.radians(wind_direction)))
    # Return the drift distance at the given altitude
    return drift_distance

#calculate glide ratio
def glide_ratio(altitude, indicated_airspeed, wind_speed, wind_direction):
    # Calculate the wind speed at the given altitude
    wind_speed = wind_speed * (1 - (2.25577 * 10 ** -5) * altitude) ** 5.25588
    # Calculate the wind direction at the given altitude
    wind_direction = wind_direction + (0.00066 * altitude)
    # Calculate the glide ratio at the given altitude
    glide_ratio = (indicated_airspeed - wind_speed * math.cos(math.radians(wind_direction))) / (wind_speed * math.sin(math.radians(wind_direction)))
    # Return the glide ratio at the given altitude
    return glide_ratio

#calculate the time to reach a given altitude
def time_to_altitude(altitude, indicated_airspeed, wind_speed, wind_direction):
    # Calculate the wind speed at the given altitude
    wind_speed = wind_speed * (1 - (2.25577 * 10 ** -5) * altitude) ** 5.25588
    # Calculate the wind direction at the given altitude
    wind_direction = wind_direction + (0.00066 * altitude)
    # Calculate the time to reach the given altitude
    time_to_altitude = altitude / (indicated_airspeed - wind_speed * math.cos(math.radians(wind_direction)))
    # Return the time to reach the given altitude
    return time_to_altitude

#calculate the distance to reach a given altitude
def distance_to_altitude(altitude, indicated_airspeed, wind_speed, wind_direction):
    # Calculate the wind speed at the given altitude
    wind_speed = wind_speed * (1 - (2.25577 * 10 ** -5) * altitude) ** 5.25588
    # Calculate the wind direction at the given altitude
    wind_direction = wind_direction + (0.00066 * altitude)
    # Calculate the distance to reach the given altitude
    distance_to_altitude = (indicated_airspeed - wind_speed * math.cos(math.radians(wind_direction))) * altitude / (indicated_airspeed - wind_speed * math.cos(math.radians(wind_direction)))
    # Return the distance to reach the given altitude
    return distance_to_altitude

#calculate the time to reach a given distance
def time_to_distance(distance, indicated_airspeed, wind_speed, wind_direction):
    # Calculate the wind speed at the given altitude
    wind_speed = wind_speed * (1 - (2.25577 * 10 ** -5) * altitude) ** 5.25588
    # Calculate the wind direction at the given altitude
    wind_direction = wind_direction + (0.00066 * altitude)
    # Calculate the time to reach the given distance
    time_to_distance = distance / (indicated_airspeed - wind_speed * math.cos(math.radians(wind_direction)))
    # Return the time to reach the given distance
    return time_to_distance

async def setup(bot):
    await bot.add_cog(Converter(bot))
