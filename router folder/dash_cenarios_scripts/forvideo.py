#!/usr/local/bin/python

import time
import os

print "Starting simulation at 5Mbps."
os.system("ipfw pipe 2 config bw 5mbit/s")
os.system("ipfw pipe 3 config bw 5mbit/s")
time.sleep(5)
print "5 sec elapsed, reducing speed to 4.5Mbps."
os.system("ipfw pipe 2 config bw 4608kbit/s")
os.system("ipfw pipe 3 config bw 4608kbit/s")
time.sleep(10)
print "15 sec elapsed, increasing speed to 4Mbps."
os.system("ipfw pipe 2 config bw 4mbit/s")
os.system("ipfw pipe 3 config bw 4mbit/s")
time.sleep(5)
print "20 sec elapsed, reducing speed to 3.5Mbps."
os.system("ipfw pipe 2 config bw 3584kbit/s")
os.system("ipfw pipe 3 config bw 3584kbit/s")
time.sleep(15)
print "35 sec elapsed, increasing speed to 3Mbps."
os.system("ipfw pipe 2 config bw 3mbit/s")
os.system("ipfw pipe 3 config bw 3mbit/s")
time.sleep(15)
print "50 sec elapsed, increasing speed to 2.5Mbps."
os.system("ipfw pipe 2 config bw 2560kbit/s")
os.system("ipfw pipe 3 config bw 2560kbit/s")
time.sleep(5)
print "55 sec elapsed, reducing speed to 4.5Mbps."
os.system("ipfw pipe 2 config bw 4608kbit/s")
os.system("ipfw pipe 3 config bw 4608kbit/s")
time.sleep(15)
print "75 sec elapsed, increasing speed to 3Mbps."
os.system("ipfw pipe 2 config bw 3mbit/s")
os.system("ipfw pipe 3 config bw 3mbit/s")
time.sleep(5)
print "80 sec elapsed, increasing speed to 4Mbps."
os.system("ipfw pipe 2 config bw 4mbit/s")
os.system("ipfw pipe 3 config bw 4mbit/s")
time.sleep(10)
print "90 sec elapsed, increasing speed to 3Mbps."
os.system("ipfw pipe 2 config bw 3mbit/s")
os.system("ipfw pipe 3 config bw 3mbit/s")
time.sleep(5)
print "95 sec elapsed, increasing speed to 4Mbps."
os.system("ipfw pipe 2 config bw 4mbit/s")
os.system("ipfw pipe 3 config bw 4mbit/s")
time.sleep(10)
print "105 sec elapsed, increasing speed to 3Mbps."
os.system("ipfw pipe 2 config bw 3mbit/s")
os.system("ipfw pipe 3 config bw 3mbit/s")
time.sleep(5)
print "110 sec elapsed, increasing speed to 4Mbps."
os.system("ipfw pipe 2 config bw 4mbit/s")
os.system("ipfw pipe 3 config bw 4mbit/s")
