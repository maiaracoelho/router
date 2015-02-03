#!/usr/local/bin/python

import time
import os

print "Starting simulation at 4Mbps."
os.system("ipfw pipe 2 config bw 5mbit/s")
os.system("ipfw pipe 3 config bw 5mbit/s")
time.sleep(500)
print "Dropping bandwidth to 2mbit/s."
os.system("ipfw pipe 2 config bw 3mbit/s")
os.system("ipfw pipe 3 config bw 3mbit/s")

