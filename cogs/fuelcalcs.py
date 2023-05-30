from discord.ext import commands


class FuelCalc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command()
    async def fuel(self, ctx, fuel_quantity: float, fuel_unit: str = "gallons"):
        if fuel_unit.lower() == "lbs":
            fuel_quantity /= 6.7  # Convert lbs to gallons
            fuel_unit = "gallons"

        await ctx.send(f"Fuel: {fuel_quantity:.2f} {fuel_unit}.")

    @commands.hybrid_command(dm_only=True)
    async def uav_bingo(self, ctx, ppc_descent_fuel: float, br: float, distance_to_airbase: float, ground_speed: float, night: bool = False, ifr: bool = False):
        if night or ifr:
            remaining_fuel_mins = 45
        else:
            remaining_fuel_mins = 30

        fuel_usage = br / 60  # Convert lbs per hour to lbs per minute
        remaining_fuel = fuel_usage * remaining_fuel_mins

        # Calculate time to airbase in minutes
        time_to_airbase = (distance_to_airbase / ground_speed) * 60
        fuel_for_distance = fuel_usage * time_to_airbase

        emergency_fuel = 35
        bingo_fuel = ppc_descent_fuel + remaining_fuel + \
            fuel_for_distance + emergency_fuel
        await ctx.send(f"UAV bingo fuel: {bingo_fuel:.2f} lbs.")


async def setup(bot):
    await bot.add_cog(FuelCalc(bot))
