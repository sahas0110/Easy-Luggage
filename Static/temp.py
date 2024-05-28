"""import cv2
# Load images
image1 = cv2.imread("a1.jpg")
image2 = cv2.imread("a2.jpg")
hist_img1 = cv2.calcHist([image1], [0, 1, 2], None, [256, 256, 256], [0, 256, 0, 256, 0, 256])
hist_img1[255, 255, 255] = 0 #ignore all white pixels
cv2.normalize(hist_img1, hist_img1, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)
hist_img2 = cv2.calcHist([image2], [0, 1, 2], None, [256, 256, 256], [0, 256, 0, 256, 0, 256])
hist_img2[255, 255, 255] = 0  #ignore all white pixels
cv2.normalize(hist_img2, hist_img2, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)
# Find the metric value
metric_val = cv2.compareHist(hist_img1, hist_img2, cv2.HISTCMP_CORREL)
print(f"Similarity Score: ", round(metric_val, 2))"""

"""import requests

origin = "8.681495,49.41461"  # Replace with your origin coordinates
destination = "8.687872,49.420318"  # Replace with your destination coordinates
api_key = "5b3ce3597851110001cf6248d779a3e1429e445ab8f63bcb65bcfafc"

url = f"https://api.openrouteservice.org/v2/directions/driving-car?api_key={api_key}&start={origin}&end={destination}"
response = requests.get(url)
data = response.json()

travel_time_seconds = data['features'][0]['properties']['segments'][0]['duration']
travel_time_minutes = travel_time_seconds / 60

print(f"Travel time: {travel_time_minutes} minutes") """

import requests

destination = "13.0846200, 80.2483500"  # Replace with your origin coordinates
origin = "10.379663 , 78.820847"  # Replace with your destination coordinates
api_key = "5b3ce3597851110001cf6248d779a3e1429e445ab8f63bcb65bcfafc"

url = f"https://api.openrouteservice.org/v2/directions/driving-car?api_key={api_key}&start={origin}&end={destination}"
response = requests.get(url)
data = response.json()
print(data)
distance_meters = data['features'][0]['properties']['segments'][0]['distance']
distance_kilometers = distance_meters / 1000

print(f"Distance: {distance_kilometers} kilometers")