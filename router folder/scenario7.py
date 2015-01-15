#!/usr/local/bin/python
#caracteriza um cenario com uma variacao decrescente

import time
import os
import sys

arquivo = sys.argv[1]
print str(arquivo)
os.system(" nohup tshark -a duration:900 -i eth0 -f 'port 80' -w %s.pcap &"%(str(arquivo)))

settings  = "#time    #bw \n" 

print "Start simulation at 3000kbit."
os.system("ipfw pipe 2 config bw 3000kbit/s")
settings  += str(datetime.datetime.now()) + "    3000000 \n" 
time.sleep(450)

print "450 seconds elapsed, reducing speed to 1200kbit."
os.system("ipfw pipe 2 config bw 1200kbit/s")
settings  += str(datetime.datetime.now()) + "    1200000 \n" 
time.sleep(450)

print "900 seconds elapsed...finishing."

log_arq = codecs.open("home/vod/capturas/teste_algoritmos1/ROMEROMEANRULE/log?_algoritmoROMEROMEANRULE_cenario7_fps?_gran?.txt", 'w', 'utf_8')
log_arq.write(settings)
log_arq.close()
