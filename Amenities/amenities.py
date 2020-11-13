import requests, json

#Insert Key here
api_key = ''
urlPlaces = "https://maps.googleapis.com/maps/api/place/textsearch/json?"
urlDistance = "https://maps.googleapis.com/maps/api/distancematrix/json?"

def amenities():
    #Insert address between both empty quotes
    distancematrix(amenitiesHelper(" "), " ")

def amenitiesHelper(property):
    amenityList = ["Restaurants in", "Malls in", "Costco in", "Target in", "Walmart in", "Bars in"]
    tempamenities = []

    for i in range(len(amenityList)):
        r = requests.get(urlPlaces + 'query=' + amenityList[i] + property + '&key=' + api_key)
        x = r.json()
        y = x['results']

        if amenityList[i] == "Costco in" or amenityList[i] == "Target in":
            tempamenities.append({'Amenity': y[i]['name'], 'Address': y[i]['formatted_address']})
        elif amenityList[i] == "Walmart in":
            for i in range(1):
                tempamenities.append({'Amenity': y[i]['name'], 'Address': y[i]['formatted_address']})
        else:
            for i in range(3):
                tempamenities.append({'Amenity': y[i]['name'], 'Address': y[i]['formatted_address']})

    return tempamenities

def distancematrix(amenlist, prop):
    finalAmenities = []
    for i in range(len(amenlist)):
        r = requests.get(urlDistance + 'origins=' + prop +
                      '&destinations=' + amenlist[i]['Address'] +
                      '&key=' + api_key)
        x = r.json()
        y = x['rows']
    finalAmenities.append({'Amenity': amenlist[i]['Amenity'], 'Address': amenlist[i]['Address'], 'Distance': y[0]})

    for i in range(len(finalAmenities)):
        print(finalAmenities[i])



amenities()

