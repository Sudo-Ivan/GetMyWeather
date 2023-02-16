import time
import discord
import requests
import os
import json

from discord.ext import commands
from discord.ext.commands import Context
from modules import windcalc
from datetime import datetime


# Here we name the cog and create a new class for the cog.
class Weather(commands.Cog, name="weather"):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(
    name="forecast",
    description="Gets weather forecast from openweather",
    )
    async def forecast(self, ctx, city: str, country: str, type: str = "detailed", unit: str = "imperial"):

        apiKey = os.getenv('OWM_API_KEY')

        now = datetime.now()

        # Quality of life - allows lowercase arguments, e.g. 'london gb' instead of 'London GB'.
        capitalisedCity = city.capitalize()
        upperCaseCountry = country.upper()

        # Make api requests to geocode arguments 1 and 2, so we can use the OneCall api. 
        geocodingParmeters = {'q': f"{capitalisedCity},{upperCaseCountry}", 'appid': apiKey}
        geocodingUrl = requests.get('http://api.openweathermap.org/geo/1.0/direct', params = geocodingParmeters)

        geocodingOutput = geocodingUrl.content.decode()

        latitude = json.loads(geocodingOutput)[0]['lat']
        longditude = json.loads(geocodingOutput)[0]['lon']

        # Make api request for the weather request.
        requestParameters = {'lat': latitude, 'lon': longditude, 'exclude': 'alerts', 'units': unit, 'appid': apiKey}  
        requestUrl = requests.get('https://api.openweathermap.org/data/2.5/onecall', params = requestParameters)

        # Get json data for weather request.
        jsonOutput = requestUrl.content.decode()

        data = json.loads(jsonOutput)['current']
        currentTemperature = data['temp']
        feelsLikeTemperature = data['feels_like']
        weatherDescription = data['weather'][0]['description']
        weatherIcon = data['weather'][0]['icon']
        pressure = data['pressure']
        humidity = data['humidity']
        windSpeed = data['wind_speed']
        windDirection = data['wind_deg']
        cloudCoverage = data['clouds']
        visibility = data['visibility']
        sunriseTimestamp = data['sunrise']
        sunsetTimestamp = data['sunset']

        sunrise = sunriseTimestamp
        sunset = sunsetTimestamp

        #DCalculate Wind Direction Using windcalc module and convert speed
        wind_direction = windcalc.find_wind_direction(windDirection)
        wind_speed_str = str(windSpeed) if unit == 'imperial' else str(windSpeed)

        # Define units for temperature and wind
        temp_units_str = ' F' if unit == 'imperial' else ' C'
        wind_units_str = ' mph' if unit == 'imperial' else ' m/s'

        # Format the local time as a string
        local_time_str = time.strftime('%H:%M:%S')

        # Determines how detailed the response and responds accordingly.
        # This one has embeds, instead of plain text
        if type == 'Basic' or type == 'basic':
            
            embed = discord.Embed(
            title = ' ',
            
            color = discord.Color.from_rgb(236, 110, 76))

            embed.set_author(name = 'Requested by ' + ctx.author.display_name)
            
            embed.set_thumbnail(url = 'https://openweathermap.org/img/wn/' + weatherIcon + '@2x.png' )
            
            embed.add_field(name = 'Weather Report for ' + capitalisedCity + ', ' + upperCaseCountry + ' Time- ' + local_time_str, value = 'There will be **' + str(weatherDescription) + '** \nwith a current temperature of **' + str(currentTemperature) + '°' + temp_units_str + '**.\nThe sun will set at **' + str(sunrise) + '** \nand rise at **' + str(sunset) + '**,\na Humidity of **' + str(humidity)+'% ' + '**\nand pressure of **' + str(pressure) + '**hPa.\nThe wind speed is **' + wind_speed_str + wind_units_str + '**,\nand the wind direction is **' + str(windDirection) + wind_direction +'**.')

            embed.set_footer(text = 'Powered by OpenWeather API')

            await ctx.send(embed = embed)

        elif type == 'Detailed' or type == 'detailed':

            embed = discord.Embed(
            title = ' ',
            
            color = discord.Color.from_rgb(236, 110, 76))

            embed.set_author(name = 'Requested by ' + ctx.author.display_name)
            
            embed.set_thumbnail(url = 'https://openweathermap.org/img/wn/' + weatherIcon + '@2x.png' )
            
            embed.add_field(name = 'Weather Report for ' + capitalisedCity + ', ' + upperCaseCountry + ' Time- ' + local_time_str, value = 'There will be **' + str(weatherDescription) + '** \nwith a current temperature of **' + str(currentTemperature) + '°' + temp_units_str + '**.\nThe sun will set at **' + str(sunrise) + '** \nand rise at **' + str(sunset) + '**,\na Humidity of **' + str(humidity)+'% ' + '**\nand pressure of **' + str(pressure) + '**hPa.\nThe wind speed is **' + wind_speed_str + wind_units_str +'**,\nand the wind direction is **' + str(windDirection) + wind_direction +'**.')

            embed.set_footer(text = 'Powered by OpenWeather API')

            await ctx.send(embed = embed)

        # Prints the commands that someone has done to the terminal window, with the time. eg.    12:30  -  Username#1111 ran the command '~forecast test test 1 basic'.
        print(now.strftime('%H:%M') + '  -  ' + str(ctx.message.author) + ' ran the commmand \'' + str(ctx.message.content) + '\'')
        print("weather command successfully executed")

async def setup(bot):
    await bot.add_cog(Weather(bot))