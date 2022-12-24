from discord.ext import commands
from discord.ext.commands import Context

import discord
import requests
import os
import dotenv
import json
import pytz

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
        geocodingParmeters = {'q': capitalisedCity + ',' + upperCaseCountry, 'appid': apiKey}
        geocodingUrl = requests.get('http://api.openweathermap.org/geo/1.0/direct', params = geocodingParmeters)

        geocodingOutput = geocodingUrl.content.decode()

        latitude = json.loads(geocodingOutput)[0]['lat']
        longditude = json.loads(geocodingOutput)[0]['lon']

        # Make api request for the weather request.
        requestParameters = {'lat': latitude, 'lon': longditude, 'exclude': 'alerts', 'units': unit, 'appid': apiKey}  
        requestUrl = requests.get('https://api.openweathermap.org/data/2.5/onecall', params = requestParameters)

        # Get json data for weather request.
        jsonOutput = requestUrl.content.decode()

        currentTemperature = json.loads(jsonOutput)['current']['temp']
        feelsLikeTemperature = json.loads(jsonOutput)['current']['feels_like']
        weatherDescription = json.loads(jsonOutput)['current']['weather'][0]['description']
        weatherIcon = json.loads(jsonOutput)['current']['weather'][0]['icon']
        pressure = json.loads(jsonOutput)['current']['pressure']
        humidity = json.loads(jsonOutput)['current']['humidity']
        windSpeed = json.loads(jsonOutput)['current']['wind_speed']
        windDirection = json.loads(jsonOutput)['current']['wind_deg']
        cloudCoverage = json.loads(jsonOutput)['current']['clouds']
        visibility = json.loads(jsonOutput)['current']['visibility']
        sunriseTimestamp = json.loads(jsonOutput)['current']['sunrise']
        sunsetTimestamp = json.loads(jsonOutput)['current']['sunset']
        sunrise = datetime.fromtimestamp(sunriseTimestamp)
        sunset = datetime.fromtimestamp(sunsetTimestamp)
        localtime = json.loads(jsonOutput)['timezone_offset']

        def get_wind_direction(degrees):
            # Convert degrees to a value between 0 and 360
            degrees = (degrees + 360) % 360
            # Determine the wind direction based on the degree value
            if degrees >= 337.5 or degrees < 22.5:
                return " N "
            elif degrees >= 22.5 and degrees < 67.5:
                return " NE "
            elif degrees >= 67.5 and degrees < 112.5:
                return " E "
            elif degrees >= 112.5 and degrees < 157.5:
                return " SE "
            elif degrees >= 157.5 and degrees < 202.5:
                return " S "
            elif degrees >= 202.5 and degrees < 247.5:
                return " SW "
            elif degrees >= 247.5 and degrees < 292.5:
                return " W "
            elif degrees >= 292.5 and degrees < 337.5:
                return " NW "

        #define wind direction and units
        wind_direction = get_wind_direction(windDirection)
        units_str = ' F' if unit == 'imperial' else ' C'

        # Convert the timezone value to a timezone object
        timezone = pytz.FixedOffset(localtime / 3600)

        # Convert the current UTC time to the local time in the city
        now = datetime.utcnow()
        local_time = timezone.localize(now)

        # Format the local time as a string
        local_time_str = local_time.strftime('%H:%M:%S')
        # Determines how detailed the response should be with argument 4, and responds accordingly.
        # This one has embeds, instead of plain text

        if type == 'Basic' or type == 'basic':
            
            embed = discord.Embed(
            title = ' ',
            
            color = discord.Color.from_rgb(236, 110, 76))

            embed.set_author(name = 'Requested by ' + ctx.author.display_name)
            
            embed.set_thumbnail(url = 'https://openweathermap.org/img/wn/' + weatherIcon + '@2x.png' )
            
            embed.add_field(name = 'Weather Report for ' + capitalisedCity + ', ' + upperCaseCountry + ' Time- ' + local_time_str, value = 'There will be **' + str(weatherDescription) + '** \nwith a current temperature of **' + str(currentTemperature) + '°' + units_str + '**.\nThe sun will set at **' + str(sunrise) + '** \nand rise at **' + str(sunset) + '**,\na Humidity of **' + str(humidity)+'% ' + '**\nand pressure of **' + str(pressure) + '** atm.\nThe wind speed is **' + str(windSpeed) + ' MPH ' + '**,\nand the wind direction is **' + str(windDirection) + wind_direction +'**.')

            embed.set_footer(text = 'Powered by OpenWeather API')

            await ctx.send(embed = embed)

        elif type == 'Detailed' or type == 'detailed':

            embed = discord.Embed(
            title = ' ',
            
            color = discord.Color.from_rgb(236, 110, 76))

            embed.set_author(name = 'Requested by ' + ctx.author.display_name)
            
            embed.set_thumbnail(url = 'https://openweathermap.org/img/wn/' + weatherIcon + '@2x.png' )
            
            embed.add_field(name = 'Weather Report for ' + capitalisedCity + ', ' + upperCaseCountry + ' Time- ' + local_time_str, value = 'There will be **' + str(weatherDescription) + '** \nwith a current temperature of **' + str(currentTemperature) + '°' + units_str + '**.\nThe sun will set at **' + str(sunrise) + '** \nand rise at **' + str(sunset) + '**,\na Humidity of **' + str(humidity)+'% ' + '**\nand pressure of **' + str(pressure) + '** atm.\nThe wind speed is **' + str(windSpeed) + ' MPH ' +'**,\nand the wind direction is **' + str(windDirection) + wind_direction +'**.')

            embed.set_footer(text = 'Powered by OpenWeather API')

            await ctx.send(embed = embed)

        elif type == 'Very_Detailed' or type == 'Very_detailed' or type == 'very_detailed':

            embed = discord.Embed(
            title = ' ',

            color = discord.Color.from_rgb(236, 110, 76))

            embed.set_author(name = 'Requested by ' + ctx.author.display_name)
            
            embed.set_thumbnail(url = 'https://openweathermap.org/img/wn/' + weatherIcon + '@2x.png' )
            
            embed.add_field(name = 'Weather Report for ' + capitalisedCity + ', ' + upperCaseCountry + ' Time- ' + local_time_str, value = 'There will be **' + str(weatherDescription) + '** \nwith a current temperature of **' + str(currentTemperature) + '°' + units_str + '**.\nThe sun will set at **' + str(sunrise) + '** \nand rise at **' + str(sunset) + '**,\na Humidity of **' + str(humidity)+'% ' + '**\nand pressure of **' + str(pressure) + '** atm.\nThe wind speed is **' + str(windSpeed) + ' MPH ' + '**,\nand the wind direction is **' + str(windDirection) + wind_direction +'**.')

            embed.set_footer(text = 'OpenWeather API')

            await ctx.send(embed = embed)

        # Prints the commands that someone has done to the terminal window, with the time. eg.    12:30  -  Username#1111 ran the command '~forecast test test 1 basic'.
        print(now.strftime('%H:%M') + '  -  ' + str(ctx.message.author) + ' ran the commmand \'' + str(ctx.message.content) + '\'')
        print("weather command successfully executed")

async def setup(bot):
    await bot.add_cog(Weather(bot))