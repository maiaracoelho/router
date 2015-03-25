#!/usr/local/bin/python
#caracteriza um cenario com uma variacao crescente

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

print "Start simulation at 3000kbps."
os.system("ipfw pipe 2 config bw 3000kbit/s")
log_arq.write(str(datetime.datetime.now()) + " 3000000 \n") 
time.sleep(900)

log_arq.write(str(datetime.datetime.now()) + " 3000000 \n") 
log_arq.close()

print "900 seconds elapsed...finishing."

