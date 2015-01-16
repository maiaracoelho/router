#!/usr/local/bin/python
#caracteriza um cenario de picos negativos de bw

import time
import os
import sys
import datetime

arq = open("entrada_arquivos.txt","r")
linhas = arq.readlines()
arquivo1, arquivo2 = linhas[0].split()
arquivo_tshark = str(arquivo1)
arquivo_logbw = str(arquivo2)
print str(arquivo_logbw)

os.system(" nohup tshark -a duration:9000 -i eth0 -f 'port 80' -w %s.pcap &"%(arquivo_tshark))

settings  = "#time    #bw \n" 

print "Starting simulation at 3000kbps."
os.system("ipfw pipe 2 config bw 3000kbit/s")
settings  += str(datetime.datetime.now()) + "    3000000 \n" 
time.sleep(95)
print "95 seconds elapsed, reducing speed to 1200kbps."
os.system("ipfw pipe 2 config bw 1200kbit/s")
settings  += str(datetime.datetime.now()) + "    1200000 \n" 
time.sleep(5)

print "100 seconds elapsed, increasing speed to 3000kbps."
os.system("ipfw pipe 2 config bw 3000bit/s")
settings  += str(datetime.datetime.now()) + "    3000000 \n" 
time.sleep(95)
print "195 seconds elapsed, reducing speed to 1200kbps."
os.system("ipfw pipe 2 config bw 1200kbit/s")
settings  += str(datetime.datetime.now()) + "    1200000 \n" 
time.sleep(10)

print "205 seconds elapsed, increasing  speed to 3000kbps."
os.system("ipfw pipe 2 config bw 3000kbit/s")
settings  += str(datetime.datetime.now()) + "    3000000 \n" 
time.sleep(95)
print "300 seconds elapsed, reducing speed to 1200kbps."
os.system("ipfw pipe 2 config bw 1200kbit/s")
settings  += str(datetime.datetime.now()) + "    1200000 \n" 

time.sleep(15)

print "315 seconds elapsed, increasing speed to 3000kMbps."
os.system("ipfw pipe 2 config bw 3000kbit/s")
settings  += str(datetime.datetime.now()) + "    3000000 \n" 
time.sleep(95)
print "410 seconds elapsed, reducing  speed to 1200kbps."
os.system("ipfw pipe 2 config bw 1200kbit/s")
settings  += str(datetime.datetime.now()) + "    1200000 \n" 
time.sleep(20)

print "430 seconds elapsed, increasing speed to 3000kbps."
os.system("ipfw pipe 2 config bw 3000kbit/s")
settings  += str(datetime.datetime.now()) + "    3000000 \n" 
time.sleep(95)
print "525 seconds elapsed, reducing speed to 1200kbps."
os.system("ipfw pipe 2 config bw 1200kbit/s")
settings  += str(datetime.datetime.now()) + "    1200000 \n" 
time.sleep(25)

print "550 seconds elapsed, increasing speed to 3000kbps."
os.system("ipfw pipe 2 config bw 3000kbit/s")
settings  += str(datetime.datetime.now()) + "    3000000 \n" 
time.sleep(95)
print "645 seconds elapsed, reducing speed to 1200kbps."
os.system("ipfw pipe 2 config bw 1200kbit/s")
settings  += str(datetime.datetime.now()) + "    1200000 \n" 

time.sleep(30)

print "675 seconds elapsed, increasing speed to 3000kbps."
os.system("ipfw pipe 2 config bw 3000kbit/s")
settings  += str(datetime.datetime.now()) + "    3000000 \n" 
time.sleep(95)
print "770 seconds elapsed, reducing speed to 1200kbps."
os.system("ipfw pipe 2 config bw 1200kbit/s")
settings  += str(datetime.datetime.now()) + "    1200000 \n" 
time.sleep(35)

print "805 seconds elapsed, increasing speed to 3000kbps."
os.system("ipfw pipe 2 config bw 3000kbit/s")
settings  += str(datetime.datetime.now()) + "    3000000 \n" 
time.sleep(95)

print "900 seconds elapsed...finishing."

log_arq = open(arquivo_logbw, 'w')
log_arq.write(settings)
log_arq.close()

