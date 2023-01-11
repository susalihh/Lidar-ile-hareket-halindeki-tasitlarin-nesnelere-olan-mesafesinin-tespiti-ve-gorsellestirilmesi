#! /usr/bin/env python
import time

frm1 = []
dosya = open("/home/test/catkin_ws/src/laser_values/src/test.txt","r")
for satir in dosya:
    frm1.append(satir)

#for i in range(0,len(frm1)):
#    print ''.join(frm1[i].split())

time.sleep(1)
frm2 = []
dosya2 = open("/home/test/catkin_ws/src/laser_values/src/test.txt","r")
for satir in dosya2:
    frm2.append(satir)

frm = float(frm1[45]) - float(frm2[45])
hiz = (float(frm)*36)/10
if not hiz >= 1:
    hiz = 0
uyari = ""
uyari2 = ""
uyari3 = ""

if hiz<=10:
    if float(frm2[45])<2.1:
        uyari = "Lutfen yavaslayiniz!"
    elif float(frm2[45])<0.7:
        uyari = "!!Kritik mesafe!! Araci durdurun!"
elif hiz<=15 and hiz>10:
    if float(frm2[45])<3.1:
        uyari = "Lutfen yavaslayiniz!"
    elif float(frm2[45])<1.5:
        uyari = "!!Kritik mesafe!! Araci durdurun!"
elif hiz<=20 and hiz>15:
    if float(frm2[45])<4.2:
        uyari = "Lutfen yavaslayiniz!"
    elif float(frm2[45])<2.6:
        uyari = "!!Kritik mesafe!! Araci durdurun!"
elif hiz<=25 and hiz>20:
    if float(frm2[45])<5.2:
        uyari = "Lutfen yavaslayiniz!"
    elif float(frm2[45])<4.1:
        uyari = "!!Kritik mesafe!! Araci durdurun!"
else:
    uyari = "\n"

if float(frm2[0])<1:
    uyari2 = "\nSol tarafta bir nesne var."
else:
    uyari2 ="\n"

if float(frm2[88])<1:
    uyari3 = "\nSag tarafta bir nesne var."
else:
    uyari3 ="\n"

dosya3 = open("/home/test/catkin_ws/src/p/test.txt","w")
dosya3.write(str("{:.2f}".format(hiz)))
dosya3.write("\n"+uyari)
dosya3.write(uyari2)
dosya3.write(uyari3)