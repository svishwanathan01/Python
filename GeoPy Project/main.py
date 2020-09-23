from geopy.geocoders import Nominatim
import math, csv


def haversine(lat1, lon1, lat2, lon2):
    radius = 3959.87433 #miles

    dlat = math.radians(lat2-lat1)
    dlon = math.radians(lon2-lon1)
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = radius * c

    return round(d, 4)

def distance(e):
    return e['Distance']

def appendSort(tempList):
    destList = []
    geolocator = Nominatim(user_agent="Hello")
    origin = geolocator.geocode("Stony Brook University")
    for pos in range(len(tempList)):
        print tempList[pos]
        dest = geolocator.geocode(tempList[pos])
        destList.append({'Address': tempList[pos], 'Distance': float(
            haversine(origin.latitude, origin.longitude, dest.latitude, dest.longitude))})
    destList.sort(key=distance)
    for pos in range(len(destList)):
        print destList[pos]

def main():
    with open('redfin_2020-09-04-13-52-21 updated9.csv', mode='r') as csv_file:
        csv_f = csv.DictReader(csv_file)
        tempList = []
        for row in csv_f:
            tempList.append(row['ADDRESS'] + ", " + row['CITY'] + ", " + row['STATE OR PROVINCE'] + ", " + row['ZIP OR POSTAL CODE'])
    return appendSort(tempList)


    # while True:
    #     inp = raw_input("Please enter quit if you wish to quit, else enter any other character")
    #     if inp == "quit":
    #         destList.sort(key=distance)
    #         print destList
    #         break
    #     else:
    #         location2 = raw_input("Enter destination: ")
    #         dest = geolocator.geocode(location2)
    #         destList.append({'Address': location2, 'Distance': float(haversine(origin.latitude, origin.longitude, dest.latitude, dest.longitude))})
    #

main()