#!/usr/local/bin/python
#caracteriza um cenario com uma variacao crescente

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

print "Start simulation at 1200kbps."
os.system("ipfw pipe 2 config bw 1200kbit/s")
settings  += str(datetime.datetime.now()) + "    1200000 \n" 
time.sleep(450)

print "450 seconds elapsed, increasing speed to 3000kbps."
os.system("ipfw pipe 2 config bw 3000kbit/s")
settings  += str(datetime.datetime.now()) + "    3000000 \n" 
time.sleep(450)

print "900 seconds elapsed...finishing."

log_arq = open(arquivo_logbw, 'w')
log_arq.write(settings)
log_arq.close()
