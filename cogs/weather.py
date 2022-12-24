from discord.ext import commands
from discord.ext.commands import Context

import discord
import requests
import os
import dotenv
import json

from datetime import datetime


# Here we name the cog and create a new class for the cog.
class Weather(commands.Cog, name="weather"):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(
    name="forecast",
    description="Gets weather forecast from openweather",
    )
    async def forecast(self, ctx, city: str, country: str, day: int, type: str = "detailed", unit: str = "imperial"):

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
        requestParameters = {'lat': latitude, 'lon': longditude, 'exclude': 'current', 'units': unit, 'appid': apiKey}  
        requestUrl = requests.get('https://api.openweathermap.org/data/2.5/onecall', params = requestParameters)

        # Get json data for weather request.
        jsonOutput = requestUrl.content.decode()

        # Find useful info (with argument 3 to define day).
        weatherDescription = json.loads(jsonOutput)['daily'][int(day)]['weather'][0]['description']
        dayTemp = json.loads(jsonOutput)['daily'][int(day)]['temp']['day']#||||||||||||||||||||||||
        nightTemp = json.loads(jsonOutput)['daily'][int(day)]['temp']['night']#||||||||||||||||||||
        weatherIcon = json.loads(jsonOutput)['daily'][int(day)]['weather'][0]['icon']#|||||||||||||
        minTemp = json.loads(jsonOutput)['daily'][int(day)]['temp']['min']#||||||||||||||||||||||||
        maxTemp = json.loads(jsonOutput)['daily'][int(day)]['temp']['max']#||||||||||||||||||||||||
        PoP = json.loads(jsonOutput)['daily'][int(day)]['pop']#||||||||||||||||||||||||||||||||||||
        uvi =  json.loads(jsonOutput)['daily'][int(day)]['uvi']#|||||||||||||||||||||||||||||||||||
        pressure =  json.loads(jsonOutput)['daily'][int(day)]['pressure']#|||||||||||||||||||||||||
        dewPoint = json.loads(jsonOutput)['daily'][int(day)]['dew_point']#|||||||||||||||||||||||||
        windSpeed = json.loads(jsonOutput)['daily'][int(day)]['wind_speed']#|||||||||||||||||||||||
        windDirection = json.loads(jsonOutput)['daily'][int(day)]['wind_deg']#|||||||||||||||||||||
        timestampForSunrise = json.loads(jsonOutput)['daily'][int(day)]['sunrise']#||||||||||||||||
        timestampForSunset = json.loads(jsonOutput)['daily'][int(day)]['sunset']#||||||||||||||||||
        sunrise = datetime.fromtimestamp(timestampForSunrise)#||||||||||||||||||||||||||||||||||||||
        sunset = datetime.fromtimestamp(timestampForSunset)#||||||||||||||||||||||||||||||||||||||||


        # Determines how detailed the response should be with argument 4, and responds accordingly.
        # This one has embeds, instead of plain text

        if type == 'Basic' or type == 'basic':
            
            embed = discord.Embed(
            title = ' ',
            
            color = discord.Color.from_rgb(236, 110, 76))

            embed.set_author(name = 'Requested by ' + ctx.author.display_name)
            
            embed.set_thumbnail(url = 'http://openweathermap.org/img/wn/' + weatherIcon + '@2x.png' )
            
            embed.add_field(name = 'Weather Report for ' + capitalisedCity, value = 'There will be **' + str(weatherDescription) + '** \nwith an average temperature of\n**' + str(dayTemp) + '°** celsius.')

            embed.set_footer(text = 'Powered by OpenWeatherMap')

            await ctx.send(embed = embed)

        elif type == 'Detailed' or type == 'detailed':

            embed = discord.Embed(
            title = ' ',
            
            color = discord.Color.from_rgb(236, 110, 76))

            embed.set_author(name = 'Requested by ' + ctx.author.display_name)
            
            embed.set_thumbnail(url = 'http://openweathermap.org/img/wn/' + weatherIcon + '@2x.png' )
            
            embed.add_field(name = 'Weather Report for ' + capitalisedCity, value = 'There will be **' + str(weatherDescription) + '** \nwith an average temperature of **' + str(dayTemp) + '°** celsius in the day,\nand **' + str(nightTemp) + '°** in the night.\nthe minimum temperature being **' + str(minTemp) + '°** \nand the maximum temperature being **' + str(maxTemp) + '°**.\nThe probability of precipitation is **' + str(PoP) + '**.\nThe sun will set at **' + str(sunrise) + '** \nand rise at **' + str(sunset) + '**.')

            embed.set_footer(text = 'Powered by OpenWeatherMap')

            await ctx.send(embed = embed)

        elif type == 'Very_Detailed' or type == 'Very_detailed' or type == 'very_detailed':

            embed = discord.Embed(
            title = ' ',

            color = discord.Color.from_rgb(236, 110, 76))

            embed.set_author(name = 'Requested by ' + ctx.author.display_name)
            
            embed.set_thumbnail(url = 'http://openweathermap.org/img/wn/' + weatherIcon + '@2x.png' )
            
            embed.add_field(name = 'Weather Report for ' + capitalisedCity, value = 'There will be **' + str(weatherDescription) + '** \nwith an average temperature of\n**' + str(dayTemp) + '°** celsius in the day,\nand **' + str(nightTemp) + '°** in the night.\nthe minimum temperature being **' + str(minTemp) + '°** \nand the maximum temperature being **' + str(maxTemp) + '°**.\nThe probability of precipitation is **' + str(PoP) + '**.\nThe sun will rise at **' + str(sunrise) + '** \nand set at **' + str(sunset) + '**.\nThere is a uvi of **' + str(uvi) + '**,\na dew point of **' + str(dewPoint) + '°**\nand pressure of **' + str(pressure) + '** atm.\nThe wind speed is **' + str(windSpeed) + '** m/s,\nand the wind direction is **' + str(windDirection) + '°**.')

            embed.set_footer(text = 'Powered by OpenWeatherMap')

            await ctx.send(embed = embed)

        # Prints the commands that someone has done to the terminal window, with the time. eg.    12:30  -  Username#1111 ran the command '~forecast test test 1 basic'.
        print(now.strftime('%H:%M') + '  -  ' + str(ctx.message.author) + ' ran the commmand \'' + str(ctx.message.content) + '\'')
        print("weather command successfully executed")

async def setup(bot):
    await bot.add_cog(Weather(bot))