#!/usr/local/bin/python

import time
import os

print "Starting simulation at 6Mbps."
os.system("ipfw pipe 2 config bw 6mbit/s")
os.system("ipfw pipe 3 config bw 6mbit/s")
time.sleep(15)
print "15 sec elapsed, reducing speed to 5.5Mbps."
os.system("ipfw pipe 2 config bw 5632kbit/s")
os.system("ipfw pipe 3 config bw 5632kbit/s")
time.sleep(15)
print "30 sec elapsed, reducing speed to 4.5Mbps."
os.system("ipfw pipe 2 config bw 4608kbit/s")
os.system("ipfw pipe 3 config bw 4608kbit/s")
time.sleep(15)
print "45 sec elapsed, reducing speed to 3.5Mbps."
os.system("ipfw pipe 2 config bw 3584kbit/s")
os.system("ipfw pipe 3 config bw 3584kbit/s")
time.sleep(15)
print "60 sec elapsed, reducing speed to 2.5Mbps."
os.system("ipfw pipe 2 config bw 2560kbit/s")
os.system("ipfw pipe 3 config bw 2560kbit/s")
time.sleep(15)
print "75 sec elapsed, increasing speed to 3Mbps."
os.system("ipfw pipe 2 config bw 3mbit/s")
os.system("ipfw pipe 3 config bw 3mbit/s")
time.sleep(15)
print "90 sec elapsed, increasing speed to 4Mbps."
os.system("ipfw pipe 2 config bw 4mbit/s")
os.system("ipfw pipe 3 config bw 4mbit/s")
time.sleep(15)
print "105 sec elapsed, increasing speed to 5Mbps."
os.system("ipfw pipe 2 config bw 5mbit/s")
os.system("ipfw pipe 3 config bw 5mbit/s")
time.sleep(15)
print "120 sec elapsed, increasing speed to 2.5Mbps."
os.system("ipfw pipe 2 config bw 2560kbit/s")
os.system("ipfw pipe 3 config bw 2560kbit/s")
time.sleep(15)
print "135 sec elapsed, increasing speed to 3Mbps."
os.system("ipfw pipe 2 config bw 3072kbit/s")
os.system("ipfw pipe 3 config bw 3072kbit/s")
time.sleep(15)
print "150 sec elapsed, increasing speed to 2.5Mbps."
os.system("ipfw pipe 2 config bw 2560kbit/s")
os.system("ipfw pipe 3 config bw 2560kbit/s")
time.sleep(15)
print "165 sec elapsed, increasing speed to 3.5Mbps."
os.system("ipfw pipe 2 config bw 3584kbit/s")
os.system("ipfw pipe 3 config bw 3584kbit/s")
time.sleep(15)
print "180 sec elapsed, increasing speed to 2.5Mbps."
os.system("ipfw pipe 2 config bw 2560kbit/s")
os.system("ipfw pipe 3 config bw 2560kbit/s")
time.sleep(15)
print "195 sec elapsed, increasing speed to 4Mbps."
os.system("ipfw pipe 2 config bw 4096kbit/s")
os.system("ipfw pipe 3 config bw 4096kbit/s")
time.sleep(30)
print "225 sec elapsed, increasing speed to 3.5Mbps."
os.system("ipfw pipe 2 config bw 3584kbit/s")
os.system("ipfw pipe 3 config bw 3584kbit/s")
time.sleep(15)
print "240 sec elapsed, increasing speed to 5Mbps."
os.system("ipfw pipe 2 config bw 5120kbit/s")
os.system("ipfw pipe 3 config bw 5120kbit/s")
time.sleep(15)
print "255 sec elapsed, increasing speed to 3.5Mbps."
os.system("ipfw pipe 2 config bw 3584kbit/s")
os.system("ipfw pipe 3 config bw 3584kbit/s")
time.sleep(15)
print "270 sec elapsed, increasing speed to 5.5Mbps."
os.system("ipfw pipe 2 config bw 5632kbit/s")
os.system("ipfw pipe 3 config bw 5632kbit/s")
time.sleep(15)
print "285 sec elapsed, increasing speed to 3.5Mbps."
os.system("ipfw pipe 2 config bw 3584kbit/s")
os.system("ipfw pipe 3 config bw 3584kbit/s")
time.sleep(15)
print "300 sec elapsed, increasing speed to 5Mbps."
os.system("ipfw pipe 2 config bw 5120kbit/s")
os.system("ipfw pipe 3 config bw 5120kbit/s")
time.sleep(15)
print "315 sec elapsed, increasing speed to 3.5Mbps."
os.system("ipfw pipe 2 config bw 3584kbit/s")
os.system("ipfw pipe 3 config bw 3584kbit/s")
time.sleep(15)
print "330 sec elapsed, increasing speed to 2.5Mbps."
os.system("ipfw pipe 2 config bw 2560kbit/s")
os.system("ipfw pipe 3 config bw 2560kbit/s")
time.sleep(15)
print "345 sec elapsed, increasing speed to 6Mbps."
os.system("ipfw pipe 2 config bw 6144kbit/s")
os.system("ipfw pipe 3 config bw 6144kbit/s")
time.sleep(1)
print "346 sec elapsed, increasing speed to 2.5Mbps."
os.system("ipfw pipe 2 config bw 2560kbit/s")
os.system("ipfw pipe 3 config bw 2560kbit/s")
time.sleep(10)
print "356 sec elapsed, increasing speed to 6Mbps."
os.system("ipfw pipe 2 config bw 6144kbit/s")
os.system("ipfw pipe 3 config bw 6144kbit/s")
time.sleep(1)
print "357 sec elapsed, increasing speed to 2.5Mbps."
os.system("ipfw pipe 2 config bw 2560kbit/s")
os.system("ipfw pipe 3 config bw 2560kbit/s")
time.sleep(10)
print "367 sec elapsed, increasing speed to 6Mbps."
os.system("ipfw pipe 2 config bw 6144kbit/s")
os.system("ipfw pipe 3 config bw 6144kbit/s")
time.sleep(3)
print "370 sec elapsed, increasing speed to 2.5Mbps."
os.system("ipfw pipe 2 config bw 2560kbit/s")
os.system("ipfw pipe 3 config bw 2560kbit/s")
time.sleep(10)
print "380 sec elapsed, increasing speed to 6Mbps."
os.system("ipfw pipe 2 config bw 6144kbit/s")
os.system("ipfw pipe 3 config bw 6144kbit/s")
time.sleep(10)
print "390 sec elapsed, increasing speed to 2.5Mbps."
os.system("ipfw pipe 2 config bw 2560kbit/s")
os.system("ipfw pipe 3 config bw 2560kbit/s")
time.sleep(1)
print "391 sec elapsed, increasing speed to 6Mbps."
os.system("ipfw pipe 2 config bw 6144kbit/s")
os.system("ipfw pipe 3 config bw 6144kbit/s")
time.sleep(10)
print "401 sec elapsed, increasing speed to 2.5Mbps."
os.system("ipfw pipe 2 config bw 2560kbit/s")
os.system("ipfw pipe 3 config bw 2560kbit/s")
time.sleep(2)
print "403 sec elapsed, increasing speed to 6Mbps."
os.system("ipfw pipe 2 config bw 6144kbit/s")
os.system("ipfw pipe 3 config bw 6144kbit/s")
time.sleep(10)
print "413 sec elapsed, increasing speed to 3.5Mbps."
os.system("ipfw pipe 2 config bw 3584kbit/s")
os.system("ipfw pipe 3 config bw 3584kbit/s")
time.sleep(18)
print "431 sec elapsed, increasing speed to 4Mbps."
os.system("ipfw pipe 2 config bw 4096kbit/s")
os.system("ipfw pipe 3 config bw 4096kbit/s")
time.sleep(1)
print "432 sec elapsed, increasing speed to 4.5Mbps."
os.system("ipfw pipe 2 config bw 4608kbit/s")
os.system("ipfw pipe 3 config bw 4608kbit/s")
time.sleep(1)
print "433 sec elapsed, increasing speed to 4Mbps."
os.system("ipfw pipe 2 config bw 4096kbit/s")
os.system("ipfw pipe 3 config bw 4096kbit/s")
time.sleep(1)
print "434 sec elapsed, increasing speed to 3.5Mbps."
os.system("ipfw pipe 2 config bw 3584kbit/s")
os.system("ipfw pipe 3 config bw 3584kbit/s")
time.sleep(1)
print "435 sec elapsed, increasing speed to 4Mbps."
os.system("ipfw pipe 2 config bw 4096kbit/s")
os.system("ipfw pipe 3 config bw 4096kbit/s")
time.sleep(1)
print "436 sec elapsed, increasing speed to 4.5Mbps."
os.system("ipfw pipe 2 config bw 4608kbit/s")
os.system("ipfw pipe 3 config bw 4608kbit/s")
time.sleep(1)
print "437 sec elapsed, increasing speed to 4Mbps."
os.system("ipfw pipe 2 config bw 4096kbit/s")
os.system("ipfw pipe 3 config bw 4096kbit/s")
time.sleep(1)
print "438 sec elapsed, increasing speed to 3.5Mbps."
os.system("ipfw pipe 2 config bw 3584kbit/s")
os.system("ipfw pipe 3 config bw 3584kbit/s")
time.sleep(1)
print "439 sec elapsed, increasing speed to 4Mbps."
os.system("ipfw pipe 2 config bw 4096kbit/s")
os.system("ipfw pipe 3 config bw 4096kbit/s")
time.sleep(1)
print "440 sec elapsed, increasing speed to 4.5Mbps."
os.system("ipfw pipe 2 config bw 4608kbit/s")
os.system("ipfw pipe 3 config bw 4608kbit/s")
time.sleep(1)
print "441 sec elapsed, increasing speed to 4Mbps."
os.system("ipfw pipe 2 config bw 4096kbit/s")
os.system("ipfw pipe 3 config bw 4096kbit/s")
time.sleep(1)
print "442 sec elapsed, increasing speed to 3.5Mbps."
os.system("ipfw pipe 2 config bw 3584kbit/s")
os.system("ipfw pipe 3 config bw 3584kbit/s")
time.sleep(1)
print "443 sec elapsed, increasing speed to 4Mbps."
os.system("ipfw pipe 2 config bw 4096kbit/s")
os.system("ipfw pipe 3 config bw 4096kbit/s")
time.sleep(1)
print "444 sec elapsed, increasing speed to 4.5Mbps."
os.system("ipfw pipe 2 config bw 4608kbit/s")
os.system("ipfw pipe 3 config bw 4608kbit/s")
time.sleep(1)
print "445 sec elapsed, increasing speed to 4Mbps."
os.system("ipfw pipe 2 config bw 4096kbit/s")
os.system("ipfw pipe 3 config bw 4096kbit/s")
time.sleep(1)
print "446 sec elapsed, increasing speed to 3.5Mbps."
os.system("ipfw pipe 2 config bw 3584kbit/s")
os.system("ipfw pipe 3 config bw 3584kbit/s")
time.sleep(1)
print "447 sec elapsed, increasing speed to 4Mbps."
os.system("ipfw pipe 2 config bw 4096kbit/s")
os.system("ipfw pipe 3 config bw 4096kbit/s")
time.sleep(1)
print "448 sec elapsed, increasing speed to 4.5Mbps."
os.system("ipfw pipe 2 config bw 4608kbit/s")
os.system("ipfw pipe 3 config bw 4608kbit/s")
time.sleep(1)
print "449 sec elapsed, increasing speed to 4Mbps."
os.system("ipfw pipe 2 config bw 4096kbit/s")
os.system("ipfw pipe 3 config bw 4096kbit/s")
time.sleep(1)
print "450 sec elapsed, increasing speed to 3.5Mbps."
os.system("ipfw pipe 2 config bw 3584kbit/s")
os.system("ipfw pipe 3 config bw 3584kbit/s")
time.sleep(1)
print "451 sec elapsed, increasing speed to 4Mbps."
os.system("ipfw pipe 2 config bw 4096kbit/s")
os.system("ipfw pipe 3 config bw 4096kbit/s")
time.sleep(1)
print "452 sec elapsed, increasing speed to 4.5Mbps."
os.system("ipfw pipe 2 config bw 4608kbit/s")
os.system("ipfw pipe 3 config bw 4608kbit/s")
time.sleep(1)
print "453 sec elapsed, increasing speed to 4Mbps."
os.system("ipfw pipe 2 config bw 4096kbit/s")
os.system("ipfw pipe 3 config bw 4096kbit/s")
time.sleep(1)
print "454 sec elapsed, increasing speed to 3.5Mbps."
os.system("ipfw pipe 2 config bw 3584kbit/s")
os.system("ipfw pipe 3 config bw 3584kbit/s")
time.sleep(1)
print "455 sec elapsed, increasing speed to 4Mbps."
os.system("ipfw pipe 2 config bw 4096kbit/s")
os.system("ipfw pipe 3 config bw 4096kbit/s")
time.sleep(1)
print "456 sec elapsed, increasing speed to 4.5Mbps."
os.system("ipfw pipe 2 config bw 4608kbit/s")
os.system("ipfw pipe 3 config bw 4608kbit/s")
time.sleep(1)
print "457 sec elapsed, increasing speed to 4Mbps."
os.system("ipfw pipe 2 config bw 4096kbit/s")
os.system("ipfw pipe 3 config bw 4096kbit/s")
time.sleep(1)
print "458 sec elapsed, increasing speed to 3.5Mbps."
os.system("ipfw pipe 2 config bw 3584kbit/s")
os.system("ipfw pipe 3 config bw 3584kbit/s")
time.sleep(1)
print "459 sec elapsed, increasing speed to 4Mbps."
os.system("ipfw pipe 2 config bw 4096kbit/s")
os.system("ipfw pipe 3 config bw 4096kbit/s")
time.sleep(31)
print "490 sec elapsed, increasing speed to 3.5Mbps."
os.system("ipfw pipe 2 config bw 3584kbit/s")
os.system("ipfw pipe 3 config bw 3584kbit/s")
time.sleep(15)
print "505 sec elapsed, increasing speed to 3Mbps."
os.system("ipfw pipe 2 config bw 3072kbit/s")
os.system("ipfw pipe 3 config bw 3072kbit/s")
time.sleep(1)
print "506 sec elapsed, increasing speed to 3.5Mbps."
os.system("ipfw pipe 2 config bw 3584kbit/s")
os.system("ipfw pipe 3 config bw 3584kbit/s")
time.sleep(1)
print "507 sec elapsed, increasing speed to 4Mbps."
os.system("ipfw pipe 2 config bw 4096kbit/s")
os.system("ipfw pipe 3 config bw 4096kbit/s")
time.sleep(1)
print "508 sec elapsed, increasing speed to 3.5Mbps."
os.system("ipfw pipe 2 config bw 3584kbit/s")
os.system("ipfw pipe 3 config bw 3584kbit/s")
time.sleep(1)
print "509 sec elapsed, increasing speed to 3Mbps."
os.system("ipfw pipe 2 config bw 3072kbit/s")
os.system("ipfw pipe 3 config bw 3072kbit/s")
time.sleep(1)
print "510 sec elapsed, increasing speed to 3.5Mbps."
os.system("ipfw pipe 2 config bw 3584kbit/s")
os.system("ipfw pipe 3 config bw 3584kbit/s")
time.sleep(1)
print "511 sec elapsed, increasing speed to 4Mbps."
os.system("ipfw pipe 2 config bw 4096kbit/s")
os.system("ipfw pipe 3 config bw 4096kbit/s")
time.sleep(1)
print "512 sec elapsed, increasing speed to 3.5Mbps."
os.system("ipfw pipe 2 config bw 3584kbit/s")
os.system("ipfw pipe 3 config bw 3584kbit/s")
time.sleep(1)
print "513 sec elapsed, increasing speed to 3Mbps."
os.system("ipfw pipe 2 config bw 3072kbit/s")
os.system("ipfw pipe 3 config bw 3072kbit/s")
time.sleep(1)
print "514 sec elapsed, increasing speed to 3.5Mbps."
os.system("ipfw pipe 2 config bw 3584kbit/s")
os.system("ipfw pipe 3 config bw 3584kbit/s")
time.sleep(1)
print "515 sec elapsed, increasing speed to 4Mbps."
os.system("ipfw pipe 2 config bw 4096kbit/s")
os.system("ipfw pipe 3 config bw 4096kbit/s")
time.sleep(1)
print "516 sec elapsed, increasing speed to 3.5Mbps."
os.system("ipfw pipe 2 config bw 3584kbit/s")
os.system("ipfw pipe 3 config bw 3584kbit/s")
time.sleep(1)
print "517 sec elapsed, increasing speed to 3Mbps."
os.system("ipfw pipe 2 config bw 3072kbit/s")
os.system("ipfw pipe 3 config bw 3072kbit/s")
time.sleep(1)
print "518 sec elapsed, increasing speed to 3.5Mbps."
os.system("ipfw pipe 2 config bw 3584kbit/s")
os.system("ipfw pipe 3 config bw 3584kbit/s")
time.sleep(1)
print "519 sec elapsed, increasing speed to 4Mbps."
os.system("ipfw pipe 2 config bw 4096kbit/s")
os.system("ipfw pipe 3 config bw 4096kbit/s")
time.sleep(1)
print "520 sec elapsed, increasing speed to 3.5Mbps."
os.system("ipfw pipe 2 config bw 3584kbit/s")
os.system("ipfw pipe 3 config bw 3584kbit/s")
time.sleep(1)
print "521 sec elapsed, increasing speed to 3Mbps."
os.system("ipfw pipe 2 config bw 3072kbit/s")
os.system("ipfw pipe 3 config bw 3072kbit/s")
time.sleep(1)
print "522 sec elapsed, increasing speed to 3.5Mbps."
os.system("ipfw pipe 2 config bw 3584kbit/s")
os.system("ipfw pipe 3 config bw 3584kbit/s")
time.sleep(1)
print "523 sec elapsed, increasing speed to 4Mbps."
os.system("ipfw pipe 2 config bw 4096kbit/s")
os.system("ipfw pipe 3 config bw 4096kbit/s")
time.sleep(1)
print "524 sec elapsed, increasing speed to 3.5Mbps."
os.system("ipfw pipe 2 config bw 3584kbit/s")
os.system("ipfw pipe 3 config bw 3584kbit/s")
time.sleep(1)
print "525 sec elapsed, increasing speed to 3Mbps."
os.system("ipfw pipe 2 config bw 3072kbit/s")
os.system("ipfw pipe 3 config bw 3072kbit/s")
time.sleep(1)
print "526 sec elapsed, increasing speed to 3.5Mbps."
os.system("ipfw pipe 2 config bw 3584kbit/s")
os.system("ipfw pipe 3 config bw 3584kbit/s")
time.sleep(1)
print "527 sec elapsed, increasing speed to 4Mbps."
os.system("ipfw pipe 2 config bw 4096kbit/s")
os.system("ipfw pipe 3 config bw 4096kbit/s")
time.sleep(1)
print "528 sec elapsed, increasing speed to 3.5Mbps."
os.system("ipfw pipe 2 config bw 3584kbit/s")
os.system("ipfw pipe 3 config bw 3584kbit/s")
time.sleep(1)
print "529 sec elapsed, increasing speed to 3Mbps."
os.system("ipfw pipe 2 config bw 3072kbit/s")
os.system("ipfw pipe 3 config bw 3072kbit/s")
time.sleep(1)
print "530 sec elapsed, increasing speed to 3.5Mbps."
os.system("ipfw pipe 2 config bw 3584kbit/s")
os.system("ipfw pipe 3 config bw 3584kbit/s")
time.sleep(1)
print "531 sec elapsed, increasing speed to 4Mbps."
os.system("ipfw pipe 2 config bw 4096kbit/s")
os.system("ipfw pipe 3 config bw 4096kbit/s")
time.sleep(1)
print "532 sec elapsed, increasing speed to 3.5Mbps."
os.system("ipfw pipe 2 config bw 3584kbit/s")
os.system("ipfw pipe 3 config bw 3584kbit/s")
time.sleep(1)
print "533 sec elapsed, increasing speed to 3Mbps."
os.system("ipfw pipe 2 config bw 3072kbit/s")
os.system("ipfw pipe 3 config bw 3072kbit/s")
time.sleep(1)
print "534 sec elapsed, increasing speed to 3.5Mbps."
os.system("ipfw pipe 2 config bw 3584kbit/s")
os.system("ipfw pipe 3 config bw 3584kbit/s")
time.sleep(1)
print "535 sec elapsed, increasing speed to 4.5Mbps."
os.system("ipfw pipe 2 config bw 4608kbit/s")
os.system("ipfw pipe 3 config bw 4608kbit/s")
time.sleep(15)
print "550 sec elapsed, increasing speed to 5.5Mbps."
os.system("ipfw pipe 2 config bw 5632kbit/s")
os.system("ipfw pipe 3 config bw 5632kbit/s")
time.sleep(50)

print "600 sec elapsed. Please wait for movie to end before finishing."

