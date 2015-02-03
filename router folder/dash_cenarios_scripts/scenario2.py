#!/usr/local/bin/python
#caracteriza um cenario crescente de variacoes longas 

import time
import os
import sys
import datetime

arq = open("/home/vod/dash_cenarios_scripts/entrada_arquivos.txt","r")
linhas = arq.readlines()
arquivo1, arquivo2 = linhas[0].split()
arquivo_tshark = str(arquivo1)
arquivo_logbw = str(arquivo2)
print str(arquivo_logbw)

os.system(" nohup tshark -a duration:1000 -i eth0 -f 'port 80' -w %s.pcap &"%(arquivo_tshark))

log_arq = open(arquivo_logbw, 'w')

settings  = "#time    #bw \n" 
log_arq.write(settings)
print "Starting simulation at 4000kbps."
os.system("ipfw pipe 2 config bw 4000Kbit/s")
log_arq.write(str(datetime.datetime.now()) + " 4000000 \n") 
time.sleep(90)
print "90 seconds elapsed, reducing speed to 3400kbps."
os.system("ipfw pipe 2 config bw 3400Kbit/s")
log_arq.write(str(datetime.datetime.now()) + " 3400000 \n") 
time.sleep(90)
print "180 seconds elapsed, reducing speed to 2800kbps."
os.system("ipfw pipe 2 config bw 2800Kbit/s")
log_arq.write(str(datetime.datetime.now()) + " 2800000 \n") 
time.sleep(90)
print "270 seconds elapsed, reducing speed to 2200kbps."
os.system("ipfw pipe 2 config bw 2200Kbit/s")
log_arq.write(str(datetime.datetime.now()) + " 2200000 \n") 
time.sleep(90)
print "360 seconds elapsed, reducing speed to 1600kbps."
os.system("ipfw pipe 2 config bw 1600Kbit/s")
log_arq.write(str(datetime.datetime.now()) + " 1600000 \n") 
time.sleep(90)

print "450 seconds elapsed."
time.sleep(90)

print "540 seconds elapsed, increasing speed to 2200kbps."
os.system("ipfw pipe 2 config bw 2200Kbit/s")
log_arq.write(str(datetime.datetime.now()) + " 2200000 \n") 
time.sleep(90)
print "630 seconds elapsed, increasing speed to 2800kbps."
os.system("ipfw pipe 2 config bw 2800Kbit/s")
log_arq.write(str(datetime.datetime.now()) + " 2800000 \n") 
time.sleep(90)
print "720 seconds elapsed, increasing speed to 3400kbps ."
os.system("ipfw pipe 2 config bw 3400Kbit/s")
log_arq.write(str(datetime.datetime.now()) + " 3400000 \n") 
time.sleep(90)
print "810 seconds elapsed, increasing speed to 4000kbps."
os.system("ipfw pipe 2 config bw 4000Kbit/s")
log_arq.write(str(datetime.datetime.now()) + " 4000000 \n") 
log_arq.close()
time.sleep(90)
log_arq.write(str(datetime.datetime.now()) + " 4000000 \n") 
log_arq.close()
print "900 seconds elapsed...finishing."


