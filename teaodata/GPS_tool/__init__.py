#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
This module is used to handle GPS, location, distance. etc. We need to provide a key of amap.com
-- distance_location: distance between two location name
-- location_coordinate: get the coordinate of a location
"""

from teaodata.gps_tool import _function as gp


def distance_location(location1="", location2="", key="1564ed3301b85f24f7a7c2c2295edf5e"):
    """
    This function will return the distance between two locations. It receives three parameter, the two location name, the key of amap.com
    -- location: receive ['location_name','city_name']
    """
    if location1 == "" or location2 == "":
        return "error: please provide two location"
    elif len(location1) > 2 or len(location2) > 2:
        return "error: please use ['location_name','city_name'] for location"
    else:
        if len(location1) > 1:
            location_name1 = location1[0]
            location_city1 = location1[1]
        else:
            location_name1 = location1[0]
            location_city1 = ""
        if len(location2) > 1:
            location_name2 = location2[0]
            location_city2 = location2[1]
        else:
            location_name2 = location2[0]
            location_city2 = ""
        location_coordinate1 = gp.get_location(
            location_name1, location_city1, key)
        location_coordinate2 = gp.get_location(
            location_name2, location_city2, key)
        if type(location_coordinate1) == list and type(location_coordinate2) == list:
            return gp.get_distance(location_coordinate1, location_coordinate2)
        else:
            return "error: can't match"


def location_coordinate(location="", key="1564ed3301b85f24f7a7c2c2295edf5e"):
    """
    This function will return the coordinate of the location, it receives two parameter, location list and key of amap.com.
    -- location: receive ['location_name','city_name']
    """
    if location == "":
        return "error: please provide the location"
    elif len(location) > 2:
        return "error: please use ['location_name','city_name'] for location"
    else:
        if len(location) > 1:
            location_name = location[0]
            location_city = location[1]
        else:
            location_name = location[0]
            location_city = ""
        return gp.get_location(location_name, location_city)


if __name__ == '__main__':
    print('Welcome to use "teaodata" library, please use it with the import command!')
