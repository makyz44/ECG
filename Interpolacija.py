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

ukupno=0
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
    mx=0
    mxi=0
    for i in range(len(izvodgreske)):
        if abs(izvodgreske[i])>mx:
            mx=izvodgreske[i]
            mxi=i+22

    maximumi=[]
    for i in range(1, len(filtriran_signal2)-1):
        if filtriran_signal2[i]>filtriran_signal2[i+1] and filtriran_signal2[i]>filtriran_signal2[i-1]:
            maximumi.append(filtriran_signal2[i])
    sortirani=sorted(maximumi)

    mojevrednostimax=[]
    for i in range(0, mxi+1):
        mojevrednostimax.append(sortirani[len(sortirani)-i-1])
    minimalnimax=min(mojevrednostimax)
    trsh=minimalnimax

    mojiindexi=[]
    for i in range(1, len(filtriran_signal2)-1):
        if filtriran_signal2[i]>trsh*0.5 and filtriran_signal2[i]>filtriran_signal2[i+1] and filtriran_signal2[i]>filtriran_signal2[i-1]:
            mojiindexi.append(i)

    #print(mojiindexi)
    #print(rr)
    konind=[]
    for i in range(len(mojiindexi)):
        mxv1=-5
        mxv2=-5
        mxv3=-5
        mxvi1=0
        mxvi2=0
        mxvi3=0
        if mojiindexi[i]>75 and mojiindexi[i]<21525:
            for j in range(mojiindexi[i]-75, mojiindexi[i]+75):
                if filtriran_signal2[j]>filtriran_signal2[j-1] and filtriran_signal2[j]>filtriran_signal2[j+1] and filtriran_signal2[j]>mxv1:
                    mxv1=filtriran_signal2[j]
                    mxvi1=j
            for j in range(mojiindexi[i]-75, mojiindexi[i]+75):
                if filtriran_signal2[j]>filtriran_signal2[j-1] and filtriran_signal2[j]>filtriran_signal2[j+1] and filtriran_signal2[j]>mxv2 and filtriran_signal2[j]<mxv1:
                    mxv2=filtriran_signal2[j]
                    mxvi2=j
            for j in range(mojiindexi[i]-75, mojiindexi[i]+75):
                if filtriran_signal2[j]>filtriran_signal2[j-1] and filtriran_signal2[j]>filtriran_signal2[j+1] and filtriran_signal2[j]>mxv3 and filtriran_signal2[j]<mxv2:
                    mxv3=filtriran_signal2[j]
                    mxvi3=j
        f=[mxvi1, mxvi2, mxvi3]
        f=sorted(f)
        mxf=0
        for j in range(len(f)):
            if f[j]>mxf:
                mxf=f[j]
        konind.append(mxf)
    konind=list(dict.fromkeys(konind))
    b=0
    for i in range(len(rr)):
        for j in range(len(konind)):
            if rr[i]==konind[j] or rr[i]==konind[j]-1 or rr[i]==konind[j]+1:
                b=b+1
    print(k)
    print(b*100/len(rr))
    ukupno=ukupno+(b*100/len(rr))
print(ukupno/48)