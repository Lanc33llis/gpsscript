import gpsd


gpsd.connect(host="0.0.0.0", port=2947)
gpsd.GpsResponse.mode = 3
gps = gpsd.GpsResponse()
gps.mode = 3

print(gpsd.device())
print(gpsd.get_current())
gpsd.GpsResponse.altitude(gps)
print(gps.altitude)
























































































































































