#!/usr/local/bin/python

import time
import os
import sys

arquivo = sys.argv[1]
print str(arquivo)
os.system(" nohup tshark -a duration:900 -i eth0 -f 'port 80' -w %s.pcap &"%(str(arquivo)))

print "Start simulation at 1200kbps."
os.system("ipfw pipe 2 config bw 1200kbit/s")
os.system("ipfw pipe 3 config bw 1200kbit/s")
time.sleep(450)

print "450 seconds elapsed, increasing speed to 3000kbps."
os.system("ipfw pipe 2 config bw 3000kbit/s")
os.system("ipfw pipe 3 config bw 3000kbit/s")
time.sleep(450)

print "900 seconds elapsed...finishing."

