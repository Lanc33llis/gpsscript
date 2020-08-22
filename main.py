import gpsd, subprocess, sys, getopt, os, time, math
from subprocess import PIPE

def gpsCheck():
        gps = gpsd.get_current()
        lat = gps.lat
        lon = gps.lon
        alt = gps.alt
        if math.trunc(lat) == 0.0 or math.trunc(lon) == 0.0 or math.trunc(alt) == 0.0:
            time.sleep(.1)
            lat, lon, alt = gpsCheck()
        return lat, lon, alt

def updateDirewolfConf():
    lat, lon, alt = gpsCheck()
    lines = ["ACHANNELS 1 \n",
    "GPSD \n",
    "CHANNEL 0 \n",
    "MYCALL KI5KFW \n",
    "MODEM 1200 \n",
    "AGWPORT 8000 \n",
    "KISSPORT 8001 \n",
    "PBEACON delay=0:05  every=30 overlay=S symbol=\"digi\" lat=" + str(float(lat)) + " long=" + str(float(lon)) + " power=50 height=20 gain=4 comment=\"San Antonia TX\" via=WIDE1-1,WIDE2-1 \n",
    "DIGIPEAT 0 0 ^WIDE[3-7]-[1-7]$|^TEST$ ^WIDE[12]-[12]$ TRACE \n",
    "IGSERVER noam.aprs2.net \n", 
    "IGLOGIN KI5KFW 19383 \n",
    "TBEACON sendto=IG delay=0 DELAY=0:30 EVERY=1:00 VIA=WIDE1-1 SYMBOL=Balloon\n",
    "IGTXLIMIT 6 10 \n",
    "TTPOINT  B01  37^55.37N  81^7.86W\n",		
    "TTPOINT  B7495088  42.605237  -71.34456\n",
    "TTPOINT  B934  42.605237  -71.34456\n",		
    "TTPOINT B901  42.661279  -71.364452\n",
    "TTPOINT B902  42.660411  -71.364419\n",
    "TTPOINT B903  42.659046  -71.364452\n",
    "TTPOINT B904  42.657578  -71.364602\n",
    "TTVECTOR  B5bbbddd  37^55.37N  81^7.86W  0.01  mi\n",
    "TTGRID   Byyyxxx    37^50.00N  81^00.00W  37^59.99N  81^09.99W\n",
    "TTUTM  B6xxxyyy  19T  10  300000  4720000\n",
    "TTCORRAL   37^55.50N  81^7.00W  0^0.02N\n",
    "TTMACRO  xx1yy  B9xx*AB166*AA2B4C5B3B0A1yy\n",
    "TTMACRO  xx2yy  B9xx*AB170*AA3C4C7C3B0A2yy\n",
    "TTMACRO  xxyyy  B9xx*AB180*AA3A6C4A0Ayyy\n",
    "TTMACRO  z  Cz\n",
    "#ThisIsWorking!"]
    direwolfconf = open("direwolf.txt", "w")
    direwolfconf.writelines(lines)
    direwolfconf.close()
    os.rename("direwolf.txt", "direwolf.conf")

def main(argv):
    callsign = "KI5KFW"
    passcode = "19383"

    
     
    opts, args = getopt.getopt(argv,"d")

    gpsd.connect(host="0.0.0.0", port=2947)
    gpsd.GpsResponse.mode = 3

    #uhub = subprocess.run(["/home/pi/gpsscript/uhubctl -a 0 -p 10"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # if uhub.stderr == '':
    #     print("Encoutered fatal error @ uhubctl: ", uhub.stderr)
    #     sys.exit(-1)
    # else:

    # while True:
    #     lat, lon, alt = gpsCheck()
    #     print("Lat " + str(float(lat)) + " Lon " + str(float(lon)))
    #     dT = datetime.datetime.now(pytz.timezone("America/Chicago"))
    #     days = dT.day
    #     hours = dT.hour
    #     mins = dT.minute
    #     timestring = str(days) + str(hours) + str(mins)

    #     latd = str(int(lat))
    #     latm = str((lat - float(latd)) * 60)[0:2]
    #     lats = str((lat - float(latd) - (float(latm) / 60)) * 3600)
    #     lats = str(round(float(lats)))[0:2]
    #     lats = str(float(lats) * 100)[0:2]
    #     if float(lats) / 60 >= 1:
    #         latm = str((float(latm) + 1))
    #         lats = str(((float(lats) / 60) - 1) * 60)
    #     latstring = latd + latm + "." + str(float(lats) / 60 * 100)[0:2] + "N"

    #     lon = abs(lon)
    #     lond = str(int(lon))
    #     lond = lond.zfill(3)
    #     lonm = str((lon - float(lond)) * 60)[0:2]
    #     lons = str((lon - float(lond) - (float(lonm) / 60)) * 3600)
    #     lons = str(round(float(lons)))
    #     lons = str(float(lons) * 100)[0:2]
    #     lonstring = lond + lonm + "." + str(float(lons) / 60 * 100)[0:2] + "W"

    #     altstring = str((int(alt * 3.281)))
    #     altstring = altstring.zfill(6)

    updateDirewolfConf()
    # try:
    #     #aprs = subprocess.run(["sudo rtl_fm -f 144.39M - | direwolf -c direwolf.conf -r 24000 -D 1 -"], shell=True, timeout=60, start_new_session=True)
    # except subprocess.TimeoutExpired:
    #     print("reset")
    #     print(latd + " " + latm + " " + lats)
    #     print(lond + " " + lonm + " " + lons)
    #     final = "aprs -c " + callsign + " -o packet.wav \"@" + timestring + "/" +  latstring + "/" + lonstring + " /A=" + altstring + "\""
    #     frame = aprs.parse_frame(callsign + ">APRS:> @211425/2930.43N/09832.33W /A=000812")
    #     a = aprs
    #     print(final)
    #     subprocess.run([final], shell=True)
    #     time.sleep(10)
    #     subprocess.run(["aplay packet.wav"], shell=True)
    #     time.sleep(30)
    
    for opt, arg in opts:
        if opt == '-d':
            print("DEBUG: ")
    
if __name__ == "__main__":
   main(sys.argv[1:])






















































































































































