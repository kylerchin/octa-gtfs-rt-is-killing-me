from google.transit import gtfs_realtime_pb2
import requests

feed = gtfs_realtime_pb2.FeedMessage()
response = requests.get('https://api.goswift.ly/real-time/octa/gtfs-rt-vehicle-positions')
feed.ParseFromString(response.content)
for entity in feed.entity:
  if entity.HasField('vehicle_position'):
    print(entity.vehicle_position)
