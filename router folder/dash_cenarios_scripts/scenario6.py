#!/usr/local/bin/python
#caracteriza um cenario com uma variacao decrescente

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
log_arq.write("#time    #bw \n" ) 

print "Start simulation at 4000kbit."
os.system("ipfw pipe 2 config bw 4000kbit/s")
log_arq.write(str(datetime.datetime.now()) + " 4000000 \n") 
time.sleep(450)

print "450 seconds elapsed, reducing speed to 1600kbit."
os.system("ipfw pipe 2 config bw 1600kbit/s")
log_arq.write(str(datetime.datetime.now()) + " 1600000 \n") 
time.sleep(450)
log_arq.write(str(datetime.datetime.now()) + " 1600000 \n") 
log_arq.close()

print "900 seconds elapsed...finishing."

