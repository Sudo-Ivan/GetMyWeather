import math


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