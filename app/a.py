import requests
import urllib

api_url = "http://www.mapquestapi.com/directions/v2/route?"
key = "0vAkKXXRQQyexUzm06F9tHsA9CuOBWFU"

while True:
    origin = input("Ingrese zona: ")
    if origin == 'q':
        break
    destination = input("Ingrese nombre del local: ")
    if destination == 'q':
        break

    url = api_url + urllib.parse.urlencode({"key":key,"from":origin,"to":destination})

    json_data = requests.get(url).json()

    status_code = json_data["info"]["statuscode"]

    if status_code == 0:
        trip_duration = json_data["route"]["formattedTime"]
        print("===============================================")
        print(f"informacion del viaje desde {origin.capitalize()} hasta {destination.capitalize()}")
        print(f"Duracion del viaje: {trip_duration()}")
