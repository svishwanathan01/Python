from django.contrib.gis.geos import Point
from geopy.distance import distance as geopy_distance
from itertools import tee, izip
from geopy.geocoders import Nominatim
import math, csv

def pairwise(iterable):
    a, b= tee(iterable)
    next(b, None)
    return izip(a,b)

def distance(e):
    return e['Distance']

def appendSortCSV(tempList):
    destList = []
    geolocator = Nominatim(user_agent="Hello")
    origin = geolocator.geocode("Stony Brook University")
    p1 = Point(origin.latitude, origin.longitude)
    for pos in range(len(tempList)):
        dest = geolocator.geocode(tempList[pos])
        p2 = Point(dest.latitude, dest.longitude)
        points = (p1, p2)
        destList.append({'Address': tempList[pos], 'Distance': float(
            round(sum(geopy_distance(a,b).meters for (a,b) in pairwise(points))*0.000621371, 4))})
    destList.sort(key=distance)
    for pos in range(len(destList)):
        print destList[pos]


def searchDjango():
    with open('redfin_2020-09-04-13-52-21 updated9.csv', mode='r') as csv_file:
        csv_f = csv.DictReader(csv_file)
        tempList = []
        for row in csv_f:
            tempList.append(row['ADDRESS'] + ", " + row['CITY'] + ", " + row['STATE OR PROVINCE'] + ", " + row['ZIP OR POSTAL CODE'])
    return appendSortCSV(tempList)



searchDjango()