#!/usr/local/bin/python
#caracteriza um cenario crescente de variacoes longas 

import time
import os
import sys

arquivo = sys.argv[1]
print str(arquivo)
os.system(" nohup tshark -a duration:900 -i eth0 -f 'port 80' -w %s.pcap &"%(str(arquivo)))

print "Starting simulation at 1200kbps."
os.system("ipfw pipe 2 config bw 1200kbit/s")
os.system("ipfw pipe 3 config bw 1200kbit/s")
time.sleep(90)
print "90 seconds elapsed, reducing speed to 1650kbps."
os.system("ipfw pipe 2 config bw 1650kbit/s")
os.system("ipfw pipe 3 config bw 1650kbit/s")
time.sleep(90)
print "180 seconds elapsed, reducing speed to 2100kbps."
os.system("ipfw pipe 2 config bw 2100kbit/s")
os.system("ipfw pipe 3 config bw 2100kbit/s")
time.sleep(90)
print "270 seconds elapsed, reducing speed to 2550kbps."
os.system("ipfw pipe 2 config bw 2550kbit/s")
os.system("ipfw pipe 3 config bw 2550kbit/s")
time.sleep(90)
print "360 seconds elapsed, reducing speed to 3000kbps."
os.system("ipfw pipe 2 config bw 3000kbit/s")
os.system("ipfw pipe 3 config bw 3000kbit/s")
time.sleep(90)

print "450 seconds elapsed."
time.sleep(90)

print "540 seconds elapsed, increasing speed to 2550kbps."
os.system("ipfw pipe 2 config bw 1650kbit/s")
os.system("ipfw pipe 3 config bw 1650kbit/s")
time.sleep(90)
print "630 seconds elapsed, increasing speed to 2100kbps."
os.system("ipfw pipe 2 config bw 2550kbit/s")
os.system("ipfw pipe 3 config bw 2550kbit/s")
time.sleep(90)
print "720 seconds elapsed, increasing speed to 1650kbps."
os.system("ipfw pipe 2 config bw 1650kbit/s")
os.system("ipfw pipe 3 config bw 1650kbit/s")
time.sleep(60)
print "810 seconds elapsed, increasing speed to 1200kbps."
os.system("ipfw pipe 2 config bw 1200kbit/s")
os.system("ipfw pipe 3 config bw 1200kbit/s")
time.sleep(90)
print "900 seconds elapsed...finishing."

