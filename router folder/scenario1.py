#!/usr/local/bin/python
#Este cenario caracteriza um cenario decrescente de variacoes longas 
# O arquivo somente deve ser executado em sudo e depois de setupdummy ter sido executado
# O arquivo deveser executado via shell da seguinte forma: 
import time
import os
import sys
import datetime

arquivo = sys.argv[1]
print str(arquivo)
os.system(" nohup tshark -a duration:9000 -i eth0 -f 'port 80' -w %s.pcap &"%(str(arquivo)))

settings  = "#time    #bw \n" 

print "Starting simulation at 3000kbps."
os.system("ipfw pipe 2 config bw 3000kbit/s")
settings  += str(datetime.datetime.now()) + "    3000000 \n" 
time.sleep(90)
print "90 seconds elapsed, reducing speed to 2550kbps."
os.system("ipfw pipe 2 config bw 2550kbit/s")
settings  += str(datetime.datetime.now()) + "    2550000 \n" 

time.sleep(90)
print "180 seconds elapsed, reducing speed to 2100kbps."
os.system("ipfw pipe 2 config bw 2100kbit/s")
settings  += str(datetime.datetime.now()) + "    2100000 " 
time.sleep(90)
print "270 seconds elapsed, reducing speed to 1650kbps."
os.system("ipfw pipe 2 config bw 1650kbit/s")
settings  += str(datetime.datetime.now()) + "    1650000 \n" 
time.sleep(90)
print "360 seconds elapsed, reducing speed to 1200kbps."
os.system("ipfw pipe 2 config bw 1200kbit/s")
settings  += str(datetime.datetime.now()) + "    1200000 \n"
time.sleep(90)

print "450 seconds elapsed."
time.sleep(90)

print "540 seconds elapsed, increasing speed to 1650kbps."
os.system("ipfw pipe 2 config bw 1650kbit/s")
settings  += str(datetime.datetime.now()) + "    1650000 \n" 
time.sleep(90)
print "630 seconds elapsed, increasing speed to 2100kbps."
os.system("ipfw pipe 2 config bw 2100kbit/s")
settings  += str(datetime.datetime.now()) + "    2100000 \n" 
time.sleep(90)
print "720 seconds elapsed, increasing speed to 2550kbps."
os.system("ipfw pipe 2 config bw 2550kbit/s")
settings  += str(datetime.datetime.now()) + "    2550000 \n" 
time.sleep(60)
print "810 seconds elapsed, increasing speed to 3000kbps."
os.system("ipfw pipe 2 config bw 3000kbit/s")
settings  += str(datetime.datetime.now()) + "    3000000 \n" 
time.sleep(90)
print "900 seconds elapsed...finishing."

log_arq = codecs.open("logs_bw/teste1_algoritmos/ROMEROMEANRULE/log?_algoritmoROMEROMEANRULE_cenario1_fps?_gran?.txt", 'w', 'utf_8')
log_arq.write(settings)
log_arq.close()
