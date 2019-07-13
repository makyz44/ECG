import os
import fil
import numpy as np
import matplotlib.pyplot as plt
import math

ukupno=0
for k in range(1, 49):
    signal=[]
    rr=[]
    refmax=[]
    binar=[]
    nizind=[]
    def sumlist(list):                      #suma liste
        s=0
        for i in range(len(list)):
            s=s+list[i]
        return s

    def abslist(list):                      #apsolutna lista
        a=[]
        for i in range(len(list)):
            if list[i]>=0:
                a.append(list[i])
            else: 
                a.append(-1*list[i])
        return a

    def petmax(deo_signala):                #vrh
        mx1=0
        imx1=0
        for i in range(1, len(deo_signala)-1):
            if deo_signala[i]>mx1 and deo_signala[i]>deo_signala[i+1] and deo_signala[i]>deo_signala[i-1]:
                mx1=deo_signala[i]
                imx1=i
        mx2=0
        imx2=0
        for i in range(1, len(deo_signala)-1):
            if deo_signala[i]>mx2 and deo_signala[i]>deo_signala[i+1] and deo_signala[i]>deo_signala[i-1] and deo_signala[i]<mx1:
                mx2=deo_signala[i]
                imx2=i
        mx3=0
        imx3=0
        for i in range(1, len(deo_signala)-1):
            if deo_signala[i]>mx3 and deo_signala[i]>deo_signala[i+1] and deo_signala[i]>deo_signala[i-1] and deo_signala[i]<mx2:
                mx3=deo_signala[i]
                imx3=i
        mx4=0
        imx4=0
        for i in range(1, len(deo_signala)-1):
            if deo_signala[i]>mx4 and deo_signala[i]>deo_signala[i+1] and deo_signala[i]>deo_signala[i-1] and deo_signala[i]<mx3:
                mx4=deo_signala[i]
                imx4=i
        mx5=0
        imx5=0
        for i in range(1, len(deo_signala)-1):
            if deo_signala[i]>mx5 and deo_signala[i]>deo_signala[i+1] and deo_signala[i]>deo_signala[i-1] and deo_signala[i]<mx4:
                mx5=deo_signala[i]
                imx5=i
        n=[imx1, imx2, imx3, imx4, imx5]
        return n

    def izvod(signal):                  #izvod
        sig=[]
        for i in range(len(signal)-1):
            sig.append(signal[i+1]-signal[i])
        return sig
        
    def kvadrat(signal):                #kvadrat
        kv=[]
        for i in range(len(signal)):
            kv.append(signal[i]*signal[i])
        return kv

    def get_sec(time_str):
        m, s = time_str.split(':')
        return int(m) * 60 + float(s)


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

    inm=0;
    mx=0
    for i in range(len(filtriran_signal2)):
        if filtriran_signal2[i]>mx:
            mx=filtriran_signal2[i]
            inm=i

    refmax=[]
    for i in range(inm-100,inm+100):
        refmax.append(filtriran_signal2[i])


    for i in range(1, len(filtriran_signal2)-1):
        if abs(filtriran_signal2[i-1])<abs(filtriran_signal2[i]) and abs(filtriran_signal2[i+1])<abs(filtriran_signal2[i]) and abs(filtriran_signal2[i])>=0.4*mx:
            binar.append(1)
        else:
            binar.append(0)

    nizindexa=[]
    for i in range(len(binar)):
        if binar[i]==1:
            nizindexa.append(i)

    gres=[]
    for i in range(100,len(filtriran_signal2)-100):
        suma=0
        for j in range(0, 200):
            suma=suma+abs(filtriran_signal2[i+j-100]-refmax[j])
        gres.append(suma)

    listaindexa=[]
    for i in range(len(nizindexa)):
        if nizindexa[i]>50 and nizindexa[i]<21550:
            mx1=0
            mx1i=0
            for j in range(nizindexa[i]-48, nizindexa[i]+48):
                if abs(filtriran_signal2[j])>abs(filtriran_signal2[j-1]) and abs(filtriran_signal2[j])>abs(filtriran_signal2[j+1]) and abs(filtriran_signal2[j])>mx1:
                    mx1=filtriran_signal2[j]
                    mx1i=j
            mx2=0
            mx2i=0
            for j in range(nizindexa[i]-48, nizindexa[i]+48):
                if abs(filtriran_signal2[j])>abs(filtriran_signal2[j-1]) and abs(filtriran_signal2[j])>abs(filtriran_signal2[j+1]) and abs(filtriran_signal2[j])>mx2 and filtriran_signal2[j]<mx1:
                    mx2=filtriran_signal2[j]
                    mx2i=j
            mx3=0
            mx3i=0
            for j in range(nizindexa[i]-48, nizindexa[i]+48):
                if abs(filtriran_signal2[j])>abs(filtriran_signal2[j-1]) and abs(filtriran_signal2[j])>abs(filtriran_signal2[j+1]) and abs(filtriran_signal2[j])>mx3 and filtriran_signal2[j]<mx2:
                    mx3=filtriran_signal2[j]
                    mx3i=j
            mm=0
            mi=0
            if mx3>mx2:
                if mx3>mx1:
                    mm=mx3
                    mi=mx3i
                else:
                    mm=mx1
                    mi=mx1i
            else:
                if mx2>mx1:
                    mm=mx2
                    mi=mx2i
                else:
                    mm=mx1
                    mi=mx1i
            listaindexa.append(mi)

    b=0
    for i in range(len(rr)):
        for j in range(len(listaindexa)):
            if rr[i]==listaindexa[j] or rr[i]==listaindexa[j]-1 or rr[i]==listaindexa[j]+1:
                b=b+1
    ukupno=ukupno+(b*100/len(rr))
    print(k)
    print(b*100/len(rr))
print("Ukupno")
print(ukupno/48)


