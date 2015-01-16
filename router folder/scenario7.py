#!/usr/local/bin/python
# Este cenario caracteriza as variacoes de banda curtas 

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

print "Starting simulation at 1200kbps."
os.system("ipfw pipe 2 config bw 1200kbit/s")
settings  += str(datetime.datetime.now()) + "    1200000 \n" 
time.sleep(45)
print "45 seconds elapsed, reducing speed to 2100kbps."
os.system("ipfw pipe 2 config bw 2100kbit/s")
settings  += str(datetime.datetime.now()) + "    2100000 \n" 
time.sleep(45)

print "90 seconds elapsed, increasing speed to 1200kbps."
os.system("ipfw pipe 2 config bw 1200kbit/s")
settings  += str(datetime.datetime.now()) + "    1200000 \n" 
time.sleep(45)
print "135 seconds elapsed, reducing speed to 2100kbps."
os.system("ipfw pipe 2 config bw 2100kbit/s")
settings  += str(datetime.datetime.now()) + "    2100000 \n" 
time.sleep(45)

print "180 seconds elapsed, increasing speed to 1200kbps."
os.system("ipfw pipe 2 config bw 1200kbit/s")
settings  += str(datetime.datetime.now()) + "    1200000 \n" 
time.sleep(45)
print "225 seconds elapsed, reducing speed to 2100kbps."
os.system("ipfw pipe 2 config bw 2100kbit/s")
settings  += str(datetime.datetime.now()) + "    2100000 \n" 
time.sleep(45)

print "270 seconds elapsed, increasing speed to 1200kbps."
os.system("ipfw pipe 2 config bw 1200kbit/s")
settings  += str(datetime.datetime.now()) + "    1200000 \n" 

time.sleep(45)
print "315 seconds elapsed, reducing speed to 2100kbps."
os.system("ipfw pipe 2 config bw 2100kbit/s")
settings  += str(datetime.datetime.now()) + "    1200000 \n" 

time.sleep(45)

print "360 seconds elapsed, increasing speed to 1200kbps."
os.system("ipfw pipe 2 config bw 1200kbit/s")
settings  += str(datetime.datetime.now()) + "    1200000 \n" 
time.sleep(45)
print "405 seconds elapsed, reducing speed to 2100kbps."
os.system("ipfw pipe 2 config bw 2100kbit/s")
settings  += str(datetime.datetime.now()) + "    2100000 \n" 
time.sleep(90)


print "450 seconds elapsed, increasing speed to 3000kbps."
os.system("ipfw pipe 2 config bw 3000kbit/s")
settings  += str(datetime.datetime.now()) + "    3000000 \n" 
time.sleep(45)
print "495 seconds elapsed, reducing speed to 2100kbps."
os.system("ipfw pipe 2 config bw 2100kbit/s")
settings  += str(datetime.datetime.now()) + "    2100000 \n" 
time.sleep(45)

print "540 seconds elapsed, increasing speed to 3000kbps."
os.system("ipfw pipe 2 config bw 3000kbit/s")
settings  += str(datetime.datetime.now()) + "    3000000 \n" 
time.sleep(45)
print "585 seconds elapsed, reducing speed to 2100kbps."
os.system("ipfw pipe 2 config bw 2100kbit/s")
settings  += str(datetime.datetime.now()) + "    2100000 \n" 
time.sleep(45)

print "630 seconds elapsed, increasing speed to 3000kbps."
os.system("ipfw pipe 2 config bw 3000kbit/s")
settings  += str(datetime.datetime.now()) + "    3000000 \n" 
time.sleep(45)
print "670 seconds elapsed, reducing speed to 2100kbps."
os.system("ipfw pipe 2 config bw 2100kbit/s")
settings  += str(datetime.datetime.now()) + "    2100000 \n" 
time.sleep(45)

print "720 seconds elapsed, increasing speed to 3000kbps."
os.system("ipfw pipe 2 config bw 3000kbit/s")
settings  += str(datetime.datetime.now()) + "    3000000 \n" 
time.sleep(45)
print "765 seconds elapsed, reducing speed to 2100kbps."
os.system("ipfw pipe 2 config bw 2100kbit/s")
settings  += str(datetime.datetime.now()) + "    2100000 \n" 
time.sleep(45)

print "810 seconds elapsed, increasing speed to 3000kbps."
os.system("ipfw pipe 2 config bw 3000kbit/s")
settings  += str(datetime.datetime.now()) + "    3000000 \n" 
time.sleep(45)

print "900 seconds elapsed...finishing."

log_arq = open(arquivo_logbw, 'w', 'utf_8')
log_arq.write(settings)
log_arq.close()


