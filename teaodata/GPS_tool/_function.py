import math
import requests
earth_radious = 6378.137


def _angle_to_rad(angle):
    rad = angle * 3.14159265358979 / 180
    return rad

def get_location(location_name):
    request = requests.get('https://restapi.amap.com/v3/geocode/geo?key=1564ed3301b85f24f7a7c2c2295edf5e&address=' + location_name).json()
    location_string = request.get('geocodes')[0].get('location').split(',')
    location = [float(location_string[0]),float(location_string[1])]
    return location

def get_distance(location1, location2):
    """
    This function will calculate the distance between two location.
    """
    rad_lng1 = _angle_to_rad(location1[0])
    rad_lat1 = _angle_to_rad(location1[1])
    rad_lng2 = _angle_to_rad(location2[0])
    rad_lat2 = _angle_to_rad(location2[1])

    A = rad_lat1 - rad_lat2
    B = rad_lng1 - rad_lng2
    S = 2 * math.asin(math.sqrt(math.pow(math.sin(A/2), 2) +
                                math.cos(rad_lat1)*math.cos(rad_lat2)*math.pow(math.sin(B/2), 2)))
    S = S * earth_radious
    result = round(S*1000) / 1000
    return result


if __name__ == '__main__':
    print('Welcome to use "teaodata" library, please use it with the import command!')