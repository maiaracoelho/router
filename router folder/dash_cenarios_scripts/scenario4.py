#!/usr/local/bin/python
#caracteriza um cenario de picos negativos de bw

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
os.system("ipfw pipe 2 config bw 4000kbit/s")
log_arq.write(str(datetime.datetime.now()) + " 4000000 \n")   
time.sleep(95)
print "95 seconds elapsed, reducing speed to 1600kbps."
os.system("ipfw pipe 2 config bw 1600kbit/s")
log_arq.write(str(datetime.datetime.now()) + " 1600000 \n") 
time.sleep(5)

print "100 seconds elapsed, increasing speed to 4000kbps."
os.system("ipfw pipe 2 config bw 4000kbit/s")
log_arq.write(str(datetime.datetime.now()) + " 4000000 \n")  
time.sleep(95)
print "195 seconds elapsed, reducing speed to 1600kbps."
os.system("ipfw pipe 2 config bw 1600kbit/s")
log_arq.write(str(datetime.datetime.now()) + " 1600000 \n") 
time.sleep(10)

print "205 seconds elapsed, increasing  speed to 4000kbps."
os.system("ipfw pipe 2 config bw 4000kbit/s")
log_arq.write(str(datetime.datetime.now()) + " 4000000 \n")  
time.sleep(95)
print "300 seconds elapsed, reducing speed to 1600kbps."
os.system("ipfw pipe 2 config bw 1600kbit/s")
log_arq.write(str(datetime.datetime.now()) + " 1600000 \n")
time.sleep(15)

print "315 seconds elapsed, increasing speed to 4000kMbps."
os.system("ipfw pipe 2 config bw 4000kbit/s")
log_arq.write(str(datetime.datetime.now()) + " 4000000 \n") 
time.sleep(95)
print "410 seconds elapsed, reducing  speed to 1600kbps."
os.system("ipfw pipe 2 config bw 1600kbit/s")
log_arq.write(str(datetime.datetime.now()) + " 1600000 \n")
time.sleep(20)

print "430 seconds elapsed, increasing speed to 4000kbps."
os.system("ipfw pipe 2 config bw 4000kbit/s")
log_arq.write(str(datetime.datetime.now()) + " 4000000 \n") 
time.sleep(95)
print "525 seconds elapsed, reducing speed to 1600kbps."
os.system("ipfw pipe 2 config bw 1600kbit/s")
log_arq.write(str(datetime.datetime.now()) + " 1600000 \n") 
time.sleep(25)

print "550 seconds elapsed, increasing speed to 4000kbps."
os.system("ipfw pipe 2 config bw 4000kbit/s")
log_arq.write(str(datetime.datetime.now()) + " 4000000 \n")  
time.sleep(95)
print "645 seconds elapsed, reducing speed to 1600kbps."
os.system("ipfw pipe 2 config bw 1600kbit/s")
log_arq.write(str(datetime.datetime.now()) + " 1600000 \n")
time.sleep(30)

print "675 seconds elapsed, increasing speed to 4000kbps."
os.system("ipfw pipe 2 config bw 4000kbit/s")
log_arq.write(str(datetime.datetime.now()) + " 4000000 \n")  
time.sleep(95)
print "770 seconds elapsed, reducing speed to 1600kbps."
os.system("ipfw pipe 2 config bw 1600kbit/s")
log_arq.write(str(datetime.datetime.now()) + " 1600000 \n")
time.sleep(35)

print "805 seconds elapsed, increasing speed to 4000kbps."
os.system("ipfw pipe 2 config bw 4000kbit/s")
log_arq.write(str(datetime.datetime.now()) + " 4000000 \n")  
time.sleep(95)
log_arq.write(str(datetime.datetime.now()) + " 4000000 \n") 
log_arq.close()
print "900 seconds elapsed...finishing."

