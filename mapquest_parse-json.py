import urllib.parse
import requests

# Initialize API link
main_api = "https://www.mapquestapi.com/directions/v2/route?" 
# Initialize API key
key = "4WQ7ADdJyfBK0yi7yuJGT3a7qW8JIVp7"

while True:
    # Prompt user for starting location
    orig = input("Starting Location: ")
    # Enables the user to exit the program
    if orig == "quit" or orig == "q":
        break
    # Prompt user for their destination
    dest = input("Destination: ")
    if dest == "quit" or dest == "q":
        break
    aVoid = input("Roads you want to avoid: ")
    if aVoid == "quit" or aVoid == "q":
        break
    # Prompt user for their desired routing type
    rType = input("Route Type (fastest, shortest, pedestrian, bicycle): ")
    if rType == "quit" or rType == "q":
        break
    # Modify API URL to insert key, starting location, destination and route type
    url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest, "routeType":rType, "avoids": aVoid})
    # Request JSON data from the URL
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]
    # Proceed if JSON status is 0/success
    if json_status == 0:
        print("=============================================")
        print("| Road Characteristics: ")
        # Display if true or false
        print("| Ferry: " + str((json_data["route"]["hasFerry"])))
        print("| Highway: " + str((json_data["route"]["hasHighway"])))
        print("| Toll Road: " + str((json_data["route"]["hasTollRoad"])))
        print("| Unpaved Roads: " + str((json_data["route"]["hasUnpaved"])))
        print("=============================================")
        print("| Directions from " + (orig) + " to " + (dest))
        # Display the estimated trip duration
        print("| Trip Duration: " + (json_data["route"]["formattedTime"]))
        # Display the total distance covered in kilometers
        print("| kilometer: " + str("{:.2f}".format((json_data["route"]["distance"])*(1.61))))
        print("Estimated Time in Seconds: " + str((json_data_2["route"]["realTime"])))
        print("=============================================")
        print("| Directions: ")
        # Displays the step-by-step directions in order to go the desired destination
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print(("| "+each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))
        print("=============================================\n")
    # If unsuccessful display status code and it meaning
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

