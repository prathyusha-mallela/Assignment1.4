# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 17:58:43 2017

@author: Win 8.1
"""

#Assignment 1.4
def get_volume_of_sphere(diameter):
    volume_of_sphere= (4/3)*(3.14)*((diameter/2)**3)
    return volume_of_sphere
#main program for diameter 12cms
sphere_volume=get_volume_of_sphere(12)
print('volume of sphere ',sphere_volume);