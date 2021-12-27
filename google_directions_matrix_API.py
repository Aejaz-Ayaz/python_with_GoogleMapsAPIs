import googlemaps

gmaps = googlemaps.Client(key='"**you need to have a valid API key with billing enabled**"')

my_dict = gmaps.distance_matrix('Delhi','Mumbai')['rows'][0]['elements'][0]

print(my_dict)


# this outputs a dictionary, with  distance between delhi and mumbai and also the duration it takes for the travel
# **you need to have a valid API key with billing enabled**
