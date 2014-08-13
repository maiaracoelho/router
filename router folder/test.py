#!/usr/local/bin/python

import time
import os

print "Starting simulation at 2.5Mbps."
os.system("ipfw pipe 2 config bw 2560kbit/s")
os.system("ipfw pipe 3 config bw 2560kbit/s")
time.sleep(7)
print "7 seconds elapsed, reducing speed to 6Mbps."
os.system("ipfw pipe 2 config bw 6mbit/s")
os.system("ipfw pipe 3 config bw 6mbit/s")
time.sleep(3)
print "10 seconds elapsed, reducing speed to 3Mbps."
os.system("ipfw pipe 2 config bw 3mbit/s")
os.system("ipfw pipe 3 config bw 3mbit/s")
time.sleep(12)
print "22 seconds elapsed, increasing speed to 3.5Mbps."
os.system("ipfw pipe 2 config bw 3600kbit/s")
os.system("ipfw pipe 3 config bw 3600kbit/s")
time.sleep(8)
print "30 seconds elapsed"

