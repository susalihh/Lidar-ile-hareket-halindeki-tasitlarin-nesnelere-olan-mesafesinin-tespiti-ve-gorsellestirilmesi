#! /usr/bin/env python
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import os
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):    
    dosya = open("/home/test/catkin_ws/src/p/test.txt","r")
    hiz = dosya.readline()    
    hiz = ''.join(hiz.split())
    uyari = dosya.readline()
    uyari2 = dosya.readline()
    uyari2 = ' '.join(uyari2.split())
    uyari3 = dosya.readline()
    uyari3 = ' '.join(uyari3.split())
    f = open("/home/test/catkin_ws/src/laser_values/src/test.txt" ,"r")
    xtwo = (f.readlines())
    arr_2 = np.array(xtwo)
    ln = len(arr_2)
    array = []
    for i in range(0,ln):
        array.append(arr_2[i])
    ax1.clear()
    os.system('python dene.py')
    plt.plot(range(0,ln),array)
    plt.xlabel("Hiz: "+str(hiz)+"km/s "+str(uyari)+" "+str(uyari2)+" "+str(uyari3))
    
ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()