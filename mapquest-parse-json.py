import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?" 
second_api = "http://www.mapquestapi.com/directions/v2/alternateroutes?"
key = "tZp0Nwi0EgdqNNv9DU7Nbfe6Y79HtMTE"

while True:
    orig = input("Starting Location: ")
    if orig == "quit" or orig == "q":
        break
    dest = input("Destination: ")
    if dest == "quit" or dest == "q":
        break
    url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest, "routeType":"fastest"})
    url_2 = second_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
    json_data = requests.get(url).json()
    json_data_2 = requests.get(url_2).json()
    json_status = json_data["info"]["statuscode"]
    if json_status == 0:
        print("=============================================")
        print("Road Characteristics: ")
        print("Ferry: " + str((json_data_2["route"]["hasFerry"])))
        print("Highway: " + str((json_data_2["route"]["hasHighway"])))
        print("Toll Road: " + str((json_data_2["route"]["hasTollRoad"])))
        print("Unpaved Roads: " + str((json_data_2["route"]["hasUnpaved"])))
        print("Seasonal Closure: " + str((json_data_2["route"]["hasSeasonalClosure"])))
        print("Country Crossing: " + str((json_data_2["route"]["hasCountryCross"])))
        print("=============================================")
        print("Directions from " + (orig) + " to " + (dest))
        print("Trip Duration: " + (json_data["route"]["formattedTime"]))
        print("kilometer: " + str("{:.2f}".format((json_data["route"]["distance"])*(1.61))))
        #print("Fuel Consumption: " + str("{:.2f}".format((json_data_2["route"]["fuelUsed"]*(3.78)))))
        print("=============================================")
        print("Directions: ")
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))
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
        print("For Staus Code: " + str(json_status) + "; Refer to:")
        print("https://developer.mapquest.com/documentation/directions-api/status-codes")
        print("************************************************************************\n")