import requests

endpoint = "https://maps.googleapis.com/maps/api/directions/json?"

api_key = "**you need to have a valid API key with billing enabled**"

origin = input("Where are you?: ").replace(' ', '+')

destination = input("Where do you want to go?: ").replace(' ', '+')

nav_request = endpoint + f"origin={origin}&destination={destination}&key={api_key}"

response = requests.get(nav_request)

print(response.json())



# this outputs a json, with all the details, co-ordinates, duration, distance etc from the origin to destination entered
# **you need to have a valid API key with billing enabled**
