import os
import EKG
import fil
import numpy as np
import matplotlib.pyplot as plt
import math

odseceni_negativni=[]
apsolutni=[]

print("Testiranje...")

filtriran_signal=fil.butter_highpass_filter(EKG.signal, 0.5, 360)

for i in range(len(filtriran_signal)):
    if filtriran_signal[i]>=0:
        odseceni_negativni.append(filtriran_signal[i])
    else:
        odseceni_negativni.append(0)

def running_mean(signal):
    output=[]
    for i in range(30, len(signal)-30):
        sum=0
        for j in range (i-30, i+30):
            sum=sum+signal[j]
        output.append(sum)
    return output

def apsolutni_signal(signal):
    apsolutno=[]
    for i in range(len(signal)):
        if signal[i]>=0:
            apsolutno.append(signal[i])
        else:
            apsolutno.append(-1*signal[i])
    return apsolutno

running_signal=running_mean(apsolutni_signal(filtriran_signal))

def odluka(signal):
    niz_odluke=[]
    for i in range(100, len(signal)-100):
        max=-1
        for j in range(i-100,i+100):
            if signal[j]>max:
                max=signal[j]
        if signal[i]==max:
           niz_odluke.append(1)
        else:
            niz_odluke.append(0)
    return niz_odluke

prozor_za_odlucivanje=odluka(running_signal)

nizind=[]
mx=[]
for p in range(0,300):
    for i in range(len(prozor_za_odlucivanje)):
        if prozor_za_odlucivanje[i]==1:
            nizind.append(i+p)
    test=EKG.rr
    b=0
    for i in range(len(test)):
        for j in range(len(nizind)):
            if test[i]==nizind[j] or test[i]==nizind[j]+1 or test[i]==nizind[j]-1:
                b=b+1
    mx.append(b*100/len(test))

ref=0
for i in range(len(mx)):
    if mx[i]>ref and mx[i]<=100:
        ref=mx[i]

print(ref)
print(mx)

print("Testiranje zavrseno.")

plt.plot(EKG.signal)
plt.plot(prozor_za_odlucivanje)
plt.show()

#plt.figure(1)                
#plt.subplot(211)        
#plt.plot(EKG.signal)
#plt.subplot(212)             
#plt.plot(filtriran_signal)
#plt.figure(2)
#plt.plot(przor_za_odlucivanje)
#plt.show()