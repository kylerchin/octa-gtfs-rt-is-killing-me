from google.transit import gtfs_realtime_pb2
import requests

print("testing Long Beach")

feed = gtfs_realtime_pb2.FeedMessage()
response = requests.get('https://lbtgtfs.lbtransit.com/TMGTFSRealTimeWebService/Vehicle/VehiclePositions.pb')
feed.ParseFromString(response.content)
for entity in feed.entity:
  print(entity)


print("testing octa")

feed = gtfs_realtime_pb2.FeedMessage()
response = requests.get('https://api.goswift.ly/real-time/octa/gtfs-rt-vehicle-positions')
feed.ParseFromString(response.content)
for entity in feed.entity:
  print(entity)
