#!/usr/local/bin/python

import time
import os
import sys

arquivo = sys.argv[1]
print str(arquivo)
os.system(" nohup tshark -a duration:900 -i eth0 -f 'port 80' -w %s.pcap &"%(str(arquivo)))

print "Starting simulation at 3000kbps."
os.system("ipfw pipe 2 config bw 3000kbit/s")
os.system("ipfw pipe 3 config bw 3000kbit/s")
time.sleep(95)
print "95 seconds elapsed, increasing speed to 1200kbps."
os.system("ipfw pipe 2 config bw 1200kbit/s")
os.system("ipfw pipe 3 config bw 1200kbit/s")
time.sleep(5)

print "100 seconds elapsed, reducing speed to 3000kbps."
os.system("ipfw pipe 2 config bw 3000bit/s")
os.system("ipfw pipe 3 config bw 3000bit/s")
time.sleep(95)
print "195 seconds elapsed, increasing speed to 1200kbps."
os.system("ipfw pipe 2 config bw 1200kbit/s")
os.system("ipfw pipe 3 config bw 1200kbit/s")
time.sleep(10)

print "205 seconds elapsed, reducing speed to 3000kbps."
os.system("ipfw pipe 2 config bw 3000kbit/s")
os.system("ipfw pipe 3 config bw 3000kbit/s")
time.sleep(95)
print "300 seconds elapsed, increasing speed to 1200kbps."
os.system("ipfw pipe 2 config bw 1200kbit/s")
os.system("ipfw pipe 3 config bw 1200kbit/s")
time.sleep(15)

print "315 seconds elapsed, reducing speed to 3000kMbps."
os.system("ipfw pipe 2 config bw 3000kbit/s")
os.system("ipfw pipe 3 config bw 3000kbit/s")
time.sleep(95)
print "410 seconds elapsed, increasing speed to 1200kbps."
os.system("ipfw pipe 2 config bw 1200kbit/s")
os.system("ipfw pipe 3 config bw 1200kbit/s")
time.sleep(20)

print "430 seconds elapsed, reducing speed to 3000kbps."
os.system("ipfw pipe 2 config bw 3000kbit/s")
os.system("ipfw pipe 3 config bw 3000kbit/s")
time.sleep(95)
print "525 seconds elapsed, increasing speed to 1200kbps."
os.system("ipfw pipe 2 config bw 1200kbit/s")
os.system("ipfw pipe 3 config bw 1200kbit/s")
time.sleep(25)

print "550 seconds elapsed, reducing speed to 3000kbps."
os.system("ipfw pipe 2 config bw 3000kbit/s")
os.system("ipfw pipe 3 config bw 3000kbit/s")
time.sleep(95)
print "645 seconds elapsed, increasing speed to 1200kbps."
os.system("ipfw pipe 2 config bw 1200kbit/s")
os.system("ipfw pipe 3 config bw 1200kbit/s")
time.sleep(30)

print "675 seconds elapsed, reducing speed to 3000kbps."
os.system("ipfw pipe 2 config bw 3000kbit/s")
os.system("ipfw pipe 3 config bw 3000kbit/s")
time.sleep(95)
print "770 seconds elapsed, increasing speed to 1200kbps."
os.system("ipfw pipe 2 config bw 1200kbit/s")
os.system("ipfw pipe 3 config bw 1200kbit/s")
time.sleep(35)

print "805 seconds elapsed, reducing speed to 3000kbps."
os.system("ipfw pipe 2 config bw 3000kbit/s")
os.system("ipfw pipe 3 config bw 3000kbit/s")
time.sleep(95)

print "900 seconds elapsed. Please wait for movie to end before finishing."

