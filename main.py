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
    direwolfconf.write()
    lines = 27
    for line in lines:
        if (line == "")
        print >>direwolfconf, line
    direwolfconf.flush()
    direwolfconf.close()
    os.rename("direwolf.txt", "direwolf.conf")
    #aprs = subprocess.run(["sudo rtl_fm -f 144.39M - | direwolf -c direwolf.conf -r 24000 -D 1 -"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    
    for opt, arg in opts:
        if opt == '-d':
            print("DEBUG: ", uhub.stdout)
    
if __name__ == "__main__":
   main(sys.argv[1:])






















































































































































