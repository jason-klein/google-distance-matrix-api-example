import urllib.request
import json

file = open('key.txt', 'r')
key = file.read().strip()

origin = '2500+E+Kearney+Springfield+MO+65898'
destination = '405+N+Jefferson+Ave+Springfield+MO+65806'

url = ('https://maps.googleapis.com/maps/api/distancematrix/json'
       + '?language=en-US&units=imperial'
       + '&origins={}'
       + '&destinations={}'
       + '&key={}'
       ).format(origin, destination, key)

response = urllib.request.urlopen(url)
response_json = json.loads(response.read())
distance_meters = response_json['rows'][0]['elements'][0]['duration']['value']
distance_minutes = response_json['rows'][0]['elements'][0]['duration']['value'] / 60

print("Origin: %s\nDestination: %s\nDistance (Meters): %s\nDistance (Seconds): %s"
      % (origin, destination, distance_meters, round(distance_minutes,2)))

"""
SAMPLE OUTPUT (refer to example-request.json for raw API response)

$ python example-request.py
Origin: 2500+E+Kearney+Springfield+MO+65898
Destination: 405+N+Jefferson+Ave+Springfield+MO+65806
Distance (Meters): 748
Distance (Seconds): 12.47

"""
