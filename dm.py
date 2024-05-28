import geocoder

def get_current_location():
    # Get current location based on IP address
    location = geocoder.ip('me')

    # Print the location details
    print("Current Location:")
    print("City:", location.city)
    
    print("Country:", location.country)
    print("Latitude:", location.latlng[0])
    print("Longitude:", location.latlng[1])

if __name__ == "__main__":
    get_current_location()
