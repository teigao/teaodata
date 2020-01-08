#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
This module is used to handle GPS, location, distance. etc. 
-- distance_location: distance between two location name
"""

from teaodata.gps_tool import _function as gp

def distance_location(location_name1, location_name2):
    """
    This function will return the distance between two locations. It receives two parameter, the two location name.
    """
    return gp.get_distance(gp.get_location(location_name1), gp.get_location(location_name2))
    
    

if __name__ == '__main__':
    print('Welcome to use "teaodata" library, please use it with the import command!')
