#import os
#import EKG
#import fil
#import numpy as np
#import matplotlib.pyplot as plt
#import math
#import time

#ukupno=0
#print("Testiranje...")
#for k in range(1, 49):
#    odseceni_negativni=[]
#    apsolutni=[]
#    signal=[]
#    rr=[]

#    def get_sec(time_str):
#        m, s = time_str.split(':')
#        return int(m) * 60 + float(s)

#    with open("C:\\Users\\Pc\\Desktop\\Peak\\p"+str(k)+".txt") as file:
#        for line in file: 
#            #line = line.strip() #or some other preprocessing
#            rr.append(get_sec(line)) #storing everything in memory!

#    with open("C:\\Users\\Pc\\Desktop\\Sample\\s"+str(k)+".txt") as file:
#        for line in file: 
#            line = line.strip() #or some other preprocessing
#            signal.append(float(line)) #storing everything in memory!

#    for i in range(len(rr)):
#        rr[i]=rr[i]*360

#    rr = [round(x) for x in rr]

#    filtriran_signal=fil.butter_highpass_filter(signal, 0.5, 360)

#    for i in range(len(filtriran_signal)):
#        if filtriran_signal[i]>=0:
#            odseceni_negativni.append(filtriran_signal[i])
#        else:
#            odseceni_negativni.append(0)

#    def running_mean(signal):
#        output=[]
#        for i in range(30, len(signal)-30):
#            sum=0
#            for j in range (i-30, i+30):
#                sum=sum+signal[j]
#            output.append(sum)
#        return output

#    def apsolutni_signal(signal):
#        apsolutno=[]
#        for i in range(len(signal)):
#            if signal[i]>=0:
#                apsolutno.append(signal[i])
#            else:
#                apsolutno.append(-1*signal[i])
#        return apsolutno

#    running_signal=running_mean(apsolutni_signal(filtriran_signal))

#    def odluka(signal):
#        niz_odluke=[]
#        for i in range(100, len(signal)-100):
#            max=-1
#            for j in range(i-100,i+100):
#                if signal[j]>max:
#                    max=signal[j]
#            if signal[i]==max:
#                niz_odluke.append(1)
#            else:
#                niz_odluke.append(0)
#        return niz_odluke

#    prozor_za_odlucivanje=odluka(running_signal)

#    nizind=[]
#    mx=[]
#    for p in range(0,300):
#        for i in range(len(prozor_za_odlucivanje)):
#            if prozor_za_odlucivanje[i]==1:
#                nizind.append(i+p)
#        test=rr
#        b=0
#        for i in range(len(test)):
#            for j in range(len(nizind)):
#                if test[i]==nizind[j] or test[i]==nizind[j]+1 or test[i]==nizind[j]-1:
#                    b=b+1
#        mx.append(b*100/len(test))

#    ref=0
#    for i in range(len(mx)):
#        if mx[i]>ref and mx[i]<=100:
#            ref=mx[i]
#    print(k)
#    print("     ")
#    print(ref)
#    print("\n")
#    ukupno=ukupno+ref

#print(ukupno/48)


