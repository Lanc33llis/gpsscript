import gpsd, subprocess, sys, getopt, os
from subprocess import PIPE

def main(argv):
    opts, args = getopt.getopt(argv,"d")

    gpsd.connect(host="0.0.0.0", port=2947)
    gpsd.GpsResponse.mode = 3

    gps = gpsd.get_current()

    #uhub = subprocess.run(["/home/pi/gpsscript/uhubctl -a 0 -p 10"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # if uhub.stderr == '':
    #     print("Encoutered fatal error @ uhubctl: ", uhub.stderr)
    #     sys.exit(-1)
    # else:
    print("I function correctly")
    gps = gpsd.get_current()
    lat = gps.lat
    lon = gps.lon
    direwolfconf = open("direwolf.txt", "w")
    direwolfconf.write
    (
        "
        ACHANNELS 1
        CHANNEL 0
        MYCALL KI5KFW
        MODEM 1200
        AGWPORT 8000
        KISSPORT 8001
        PBEACON delay=1  every=30 overlay=S symbol="digi" lat=29.651190 long=-98.490837 power=50 height=20 gain=4 comment="San Antonia TX" via=WIDE1-1,WIDE2-1 
        DIGIPEAT 0 0 ^WIDE[3-7]-[1-7]$|^TEST$ ^WIDE[12]-[12]$ TRACE 
        IGSERVER noam.aprs2.net
        IGLOGIN KI5KFW 19383
        PBEACON sendto=IG delay=0:30 every=60:00 symbol="igate" overlay=R lat=", lat, " long=", lon," 
        IGTXLIMIT 6 10
        TTPOINT  B01  37^55.37N  81^7.86W  			
        TTPOINT  B7495088  42.605237  -71.34456		
        TTPOINT  B934  42.605237  -71.34456			
        TTPOINT B901  42.661279  -71.364452 
        TTPOINT B902  42.660411  -71.364419 
        TTPOINT B903  42.659046  -71.364452 
        TTPOINT B904  42.657578  -71.364602 v
        TTVECTOR  B5bbbddd  37^55.37N  81^7.86W  0.01  mi
        TTGRID   Byyyxxx    37^50.00N  81^00.00W  37^59.99N  81^09.99W   
        TTUTM  B6xxxyyy  19T  10  300000  4720000
        TTCORRAL   37^55.50N  81^7.00W  0^0.02N
        TTMACRO  xx1yy  B9xx*AB166*AA2B4C5B3B0A1yy
        TTMACRO  xx2yy  B9xx*AB170*AA3C4C7C3B0A2yy
        TTMACRO  xxyyy  B9xx*AB180*AA3A6C4A0Ayyy
        TTMACRO  z  Cz
        Check this!
        "
    )
    direwolfconf.flush()
    direwolfconf.close()
    os.rename("direwolf.txt", "direwolf.conf")
    #aprs = subprocess.run(["sudo rtl_fm -f 144.39M - | direwolf -c direwolf.conf -r 24000 -D 1 -"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    
    for opt, arg in opts:
        if opt == '-d':
            print("DEBUG: ", uhub.stdout)
    
if __name__ == "__main__":
   main(sys.argv[1:])






















































































































































