import gpsd, subprocess, sys, getopt
from subprocess import PIPE

def main(argv):
    opts, args = getopt.getopt(argv,"d")

    gpsd.connect(host="0.0.0.0", port=2947)
    gpsd.GpsResponse.mode = 3

    gps = gpsd.get_current()

    uhub = subprocess.run(["/home/pi/gpsscript/uhubctl -a 0 -p 10"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    if uhub.stderr != '':
        print("Encoutered fatal error @ uhubctl: ", uhub.stderr)
        sys.exit(-1)
    else:
        print("I function correctly")
    for opt, arg in opts:
        if opt == '-d':
            print("DEBUG: ", uhub.stdout)
    
if __name__ == "__main__":
   main(sys.argv[1:])






















































































































































