import time
import discord
import requests
import os
import json

from discord.ext import commands
from modules import windcalc
from datetime import datetime


class Weather(commands.Cog, name="weather"):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(
        name="forecast",
        description="Gets weather forecast from OpenWeather",
    )
    async def forecast(self, ctx, city: str, country: str, unit: str = "imperial"):

        apiKey = os.getenv('OWM_API_KEY')

        now = datetime.now()

        capitalisedCity = city.capitalize()
        upperCaseCountry = country.upper()

        geocodingParmeters = {'q': capitalisedCity +
                              ',' + upperCaseCountry, 'appid': apiKey}
        geocodingUrl = requests.get(
            'http://api.openweathermap.org/geo/1.0/direct', params=geocodingParmeters)

        geocodingOutput = json.loads(geocodingUrl.content.decode())
        latitude = geocodingOutput[0]['lat']
        longditude = geocodingOutput[0]['lon']

        requestParameters = {'lat': latitude, 'lon': longditude,
                             'exclude': 'alerts', 'units': unit, 'appid': apiKey}
        requestUrl = requests.get(
            'https://api.openweathermap.org/data/2.5/onecall', params=requestParameters)

        jsonOutput = json.loads(requestUrl.content.decode())
        current_data = jsonOutput['current']

        # Extract weather data from JSON
        currentTemperature = current_data['temp']
        weatherDescription = current_data['weather'][0]['description']
        weatherIcon = current_data['weather'][0]['icon']
        pressure = current_data['pressure']
        humidity = current_data['humidity']
        windSpeed = current_data['wind_speed']
        windDirection = current_data['wind_deg']
        sunrise = datetime.fromtimestamp(current_data['sunrise'])
        sunset = datetime.fromtimestamp(current_data['sunset'])

        wind_direction = windcalc.find_wind_direction(windDirection)
        wind_speed_str = str(windSpeed)

        temp_units_str = ' F' if unit == 'imperial' else ' C'
        wind_units_str = ' mph' if unit == 'imperial' else ' m/s'

        local_time_str = time.strftime('%H:%M:%S')

        embed = discord.Embed(
            title=' ',
            color=discord.Color.from_rgb(236, 110, 76)
        )

        embed.set_author(name='Requested by ' + ctx.author.display_name)
        embed.set_thumbnail(
            url='https://openweathermap.org/img/wn/' + weatherIcon + '@2x.png')

        embed.add_field(name='Weather Report for ' + capitalisedCity + ', ' + upperCaseCountry + ' Time- ' + local_time_str,
                        value='There will be **' + str(weatherDescription) + '** \nwith a current temperature of **' + str(currentTemperature) + '°' + temp_units_str + '**.\nThe sun will set at **' + str(sunset) + '** \nand rise at **' + str(sunrise) + '**,\na Humidity of **' + str(humidity) + '% ' + '**\nand pressure of **' + str(pressure) + '**hPa.\nThe wind speed is **' + wind_speed_str + wind_units_str + '**,\nand the wind direction is **' + str(windDirection) + wind_direction + '**.')

        embed.set_footer(text='Powered by OpenWeather API')

        await ctx.send(embed=embed)

        # Print the command usage information to the terminal windows
        print(now.strftime('%H:%M') + '  -  ' + str(ctx.message.author) +
              ' ran the commmand \'' + str(ctx.message.content) + '\'')
        print("weather command successfully executed")


async def setup(bot):
    await bot.add_cog(Weather(bot))
