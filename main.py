import gpsd

gpsd.connect(host="0.0.0.0", port=2947)

print(gpsd.GpsResponse.lat)
print(gpsd.GpsResponse.long)
























































































































































