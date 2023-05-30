
# wind direction calculation based on degrees
def find_wind_direction(degrees):
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


def conv_wind_spd(speed, unit):
    # Convert wind speed from m/s to mph
    if unit == 'imperial':
        return speed * 2.23694
    # Convert wind speed from m/s to km/h
    elif unit == 'metric':
        return speed * 3.6
    # Return the wind speed in m/s
    else:
        return speed
