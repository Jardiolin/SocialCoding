import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
second_api = "http://www.mapquestapi.com/directions/v2/optimizedroute?"
key = "QmmjDPDDikEDvVILEupkDxlQMjxzaT4V"

while True:
    orig = input("Starting Location: ")
    if orig == "quit" or orig == "q":
        break
    dest = input("Destination: ")
    if dest == "quit" or dest == "q":
        break

    url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})
    url_2 = second_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
    print("URL: " + (url))
    print("URL: " + (url_2))
    json_data = requests.get(url).json()
    json_data_2 = requests.get(url_2).json()
    json_status = json_data["info"]["statuscode"]

    if json_status == 0:
        
        print("Trip Duration:   " + (json_data["route"]["formattedTime"]))
        print("Has toll road: " + str(json_data["route"]["hasTollRoad"]))
        print("Kilometers:           " + str("{:.2f}".format((json_data["route"]["distance"])*1.61)))
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print((each["narrative"]) + " (" +
        str("{:.2f}".format((each["distance"])*1.61) + " km)"))
        print("=============================================\n")
    elif json_status == 402:
        print("**********************************************")
        print("Status Code: " + str(json_status) + "; Invalid user inputs for one or both locations.")
        print("**********************************************\n")
    elif json_status == 611:
        print("**********************************************")
        print("Status Code: " + str(json_status) + "; Missing an entry for one or both locations.")
        print("**********************************************\n")
    else:
        print("************************************************************************")
        print("For Status Code: " + str(json_status) + "; Refer to:")
        print("https://developer.mapquest.com/documentation/directions-api/status-codes")
        print("************************************************************************\n")