#!/usr/local/bin/python

import time
import os

print "Starting simulation at 4Mbps."
os.system("ipfw pipe 2 config bw 4mbit/s")
os.system("ipfw pipe 3 config bw 4mbit/s")
time.sleep(30)
print "0.5 minutes elapsed, reducing speed to 2.5Mbps."
os.system("ipfw pipe 2 config bw 2560kbit/s")
os.system("ipfw pipe 3 config bw 2560kbit/s")
time.sleep(60)
print "1.5 minutes elapsed, reducing speed to 4.5Mbps."
os.system("ipfw pipe 2 config bw 4608kbit/s")
os.system("ipfw pipe 3 config bw 4608kbit/s")
time.sleep(210)
print "5 minutes elapsed, reducing speed to 2.5Mbps."
os.system("ipfw pipe 2 config bw 2560kbit/s")
os.system("ipfw pipe 3 config bw 2560kbit/s")
time.sleep(80)
print "6:20 minutes elapsed, increasing speed to 4.5Mbps."
os.system("ipfw pipe 2 config bw 4608kbit/s")
os.system("ipfw pipe 3 config bw 4608kbit/s")
time.sleep(120)
print "8:20 minutes elapsed, reducing speed to 2.5Mbps."
os.system("ipfw pipe 2 config bw 2560kbit/s")
os.system("ipfw pipe 3 config bw 2560kbit/s")
time.sleep(100)
print "10 minutes elapsed. Please wait for movie to end before finishing."

