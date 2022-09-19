import requests
import urllib

api_url = "https://www.mapquestapi.com/directions/v2/route?"                           #api de maps
key = "ydiyiK71UHQPS1DgXNdohvQfNcIPoHja"
api_mrc = "https://assets.mapquestapi.com/icon/v2/marker@2x.png"                      #imagen de marcador
while True:
    origin = input("Ingrese zona: ")
    if origin == 'q':
        break
    destination = input("Ingrese ubicacion del local: ")
    if destination == 'q':
        break

    url = api_url + urllib.parse.urlencode({"key":key,"from":origin,"to":destination})

    json_data = requests.get(url).json()

    status_code = json_data["info"]["statuscode"]

    if status_code == 0:
        trip_duration = json_data["route"]["formattedTime"]
        distance = json_data["route"]["distance"]
        print("===============================================")
        print(f"Informacion del viaje desde {origin.capitalize()} hasta {destination.capitalize()}.")
        print(f"Duracion del viaje: {trip_duration}.")
        print("Distancia:" + str("{:.2f}".format(distance) + "Km"))
            # print("================================================")
            # print("indicaciones del viaje")

            # for each in json_data["route"]["legs"][0]["maneuvers"]:
            #     print(each["narrative"])
                