import os
import fil
import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.interpolate import interp1d
from scipy import interpolate

def get_sec(time_str):
    m, s = time_str.split(':')
    return int(m) * 60 + float(s)

def greska(signal):
    min=100
    for i in range(len(signal)):
        if signal[i]<min:
            min=signal[i]
    suma=0
    for i in range(len(signal)):
        suma=suma+(abs(signal[i]-min))
    return suma
koef=[]
for k in range(1, 49):
    signal=[]
    rr=[]
    with open("C:\\Users\\Pc\\Desktop\\Peak\\p"+str(k)+".txt") as file:
        for line in file: 
            #line = line.strip() #or some other preprocessing
            rr.append(get_sec(line)) #storing everything in memory!

    with open("C:\\Users\\Pc\\Desktop\\Sample\\s"+str(k)+".txt") as file:
        for line in file: 
            line = line.strip() #or some other preprocessing
            signal.append(float(line)) #storing everything in memory!

    for i in range(len(rr)):
        rr[i]=rr[i]*360
    rr = [round(x) for x in rr]

    filtriran_signal=fil.butter_highpass_filter(signal, 1.1, 360)
    filtriran_signal2=fil.butter_lowpass_filter(filtriran_signal, 150 ,360)

    maximumi=[]
    for i in range(1, len(filtriran_signal2)-1):
        if filtriran_signal2[i]>filtriran_signal2[i+1] and filtriran_signal2[i]>filtriran_signal2[i-1]:
            maximumi.append(filtriran_signal2[i])

    sortirani=sorted(maximumi)

    #print(sortirani)


    greske=[]
    #n=70
    for n in range(30, 140):
        mojevrednostimax=[]
        for i in range(0, n+1):
            mojevrednostimax.append(sortirani[len(sortirani)-i-1])

        #print(mojevrednostimax)

        nizindexa=[]
        for i in range(len(mojevrednostimax)):
            for j in range(1, len(filtriran_signal2)-1):
                if filtriran_signal2[j]==mojevrednostimax[i] and filtriran_signal2[j-1]<filtriran_signal2[j] and filtriran_signal2[j+1]<filtriran_signal2[j]:
                    nizindexa.append(j)

        sortiraniindexi=sorted(nizindexa)

        #print(sortiraniindexi)

        vrednosti=[]
        for i in range(len(sortiraniindexi)):
            vrednosti.append(filtriran_signal2[sortiraniindexi[i]])

        #print(vrednosti)

        x=sortiraniindexi
        y=vrednosti

        d=2
        s = interpolate.InterpolatedUnivariateSpline(x, y)
        xx = np.linspace(min(x),max(x))
        yy = s(xx)

        greske.append(greska(yy))

        #plt.plot(yy)

        #plt.figure()
        #plt.plot(filtriran_signal2)
        #plt.plot(x, y, 'ro', xx, yy)
        #plt.axis([min(xx)-d, max(xx)+d, min(yy)-d, max(yy)+d])
        #plt.show()
    izvodgreske=[]
    for i in range(len(greske)-1):
        izvodgreske.append(greske[i+1]-greske[i])
#    plt.plot(greske)
#    plt.plot(izvodgreske)
    mx=0
    mxi=0
    for i in range(len(izvodgreske)):
        if abs(izvodgreske[i])>mx:
            mx=izvodgreske[i]
            mxi=i+20
    print(k)
    print(mxi/len(rr))
    koef.append(mxi/len(rr))
print(koef)
#plt.show()