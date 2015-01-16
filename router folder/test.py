#!/usr/local/bin/python

import time
import os
import datetime

arq = open("entrada_arquivos.txt","r")
linhas = arq.readlines()
arquivo1, arquivo2 = linhas[0].split()
arquivo_tshark = str(arquivo1)
arquivo_logbw = str(arquivo2)
print str(arquivo_logbw)

os.system(" nohup tshark -a duration:9000 -i eth0 -f 'port 80' -w %s.pcap &"%(arquivo_tshark))


settings  = "#time    #bw \n" 

print "Starting simulation at 2.5Mbps."
os.system("ipfw pipe 2 config bw 2560kbit/s")
settings  += str(datetime.datetime.now()) + "    2560000 \n" 
time.sleep(7)
print "7 seconds elapsed, reducing speed to 6Mbps."
os.system("ipfw pipe 2 config bw 6mbit/s")
settings  += str(datetime.datetime.now()) + "    6000000 \n" 
time.sleep(3)
print "10 seconds elapsed, reducing speed to 3Mbps."
os.system("ipfw pipe 2 config bw 3mbit/s")
settings  += str(datetime.datetime.now()) + "    3000000 \n" 
time.sleep(12)
print "22 seconds elapsed, increasing speed to 3.5Mbps."
os.system("ipfw pipe 2 config bw 3600kbit/s")
settings  += str(datetime.datetime.now()) + "    3600000 \n" 

time.sleep(8)
print "30 seconds elapsed"

log_arq = open(arquivo_logbw, 'w')
log_arq.write(settings)
log_arq.close()

