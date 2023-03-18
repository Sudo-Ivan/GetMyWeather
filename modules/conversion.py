#fahrenheit to celsius
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

#fahrenheit to kelvin
def fahrenheit_to_kelvin(fahrenheit):
    kelvin = (fahrenheit + 459.67) * 5/9
    return kelvin

#celsius to fahrenheit
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

#celsius to kelvin
def celsius_to_kelvin(celsius):
    kelvin = celsius + 273.15
    return kelvin

#kelvin to fahrenheit
def kelvin_to_fahrenheit(kelvin):
    fahrenheit = (kelvin * 9/5) - 459.67
    return fahrenheit

#kelvin to celsius
def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273.15
    return celsius

#meters per second to miles per hour
def mps_to_mph(mps):
    mph = mps * 2.23694
    return mph

#miles per hour to meters per second
def mph_to_mps(mph):
    mps = mph / 2.23694
    return mps

#meters per second to kilometers per hour
def mps_to_kph(mps):
    kph = mps * 3.6
    return kph

#kilometers per hour to miles per hour
def kph_to_mph(kph):
    mph = kph / 1.60934
    return mph

#miles per hour to kilometers per hour
def mph_to_kph(mph):
    kph = mph * 1.60934
    return kph

#hpa to inHg
def hpa_to_inhg(hpa):
    inhg = hpa * 0.029529983071445
    return inhg

#inHg to hpa
def inhg_to_hpa(inhg):
    hpa = inhg / 0.029529983071445
    return hpa

#hpa to mmHg
def hpa_to_mmhg(hpa):
    mmhg = hpa * 0.750061561303
    return mmhg

#mmHg to hpa
def mmhg_to_hpa(mmhg):
    hpa = mmhg / 0.750061561303
    return hpa

#hpa to atm
def hpa_to_atm(hpa):
    atm = hpa * 0.00098692326671601
    return atm

#atm to hpa
def atm_to_hpa(atm):
    hpa = atm / 0.00098692326671601
    return hpa

#visibility in meters to miles
def meters_to_miles(meters):
    miles = meters / 1609.34
    return miles

#visibility in miles to meters
def miles_to_meters(miles):
    meters = miles * 1609.34
    return meters

#visibility in miles to kilometers
def miles_to_kilometers(miles):
    kilometers = miles * 1.60934
    return kilometers

#visibility in kilometers to miles
def kilometers_to_miles(kilometers):
    miles = kilometers / 1.60934
    return miles
