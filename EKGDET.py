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

    for i in range(1, len(filtriran_signal2)-1):
        if abs(filtriran_signal2[i-1])<abs(filtriran_signal2[i]) and abs(filtriran_signal2[i+1])<abs(filtriran_signal2[i]) and abs(filtriran_signal2[i])>=0.4*mx:
            binar.append(1)
        else:
            binar.append(0)

    nizindexa=[]
    for i in range(len(binar)):
        if binar[i]==1:
            nizindexa.append(i)

    listaindexa=[]
    for i in range(len(nizindexa)):
        w=75
        mxv1=-5
        mxv2=-5
        mxv3=-5
        mxvi1=0
        mxvi2=0
        mxvi3=0
        if nizindexa[i]>w and nizindexa[i]<len(filtriran_signal2)-w:
            for j in range(nizindexa[i]-w, nizindexa[i]+w):
                if filtriran_signal2[j]>filtriran_signal2[j-1] and filtriran_signal2[j]>filtriran_signal2[j+1] and filtriran_signal2[j]>mxv1:
                    mxv1=filtriran_signal2[j]
                    mxvi1=j
            for j in range(nizindexa[i]-w, nizindexa[i]+w):
                if filtriran_signal2[j]>filtriran_signal2[j-1] and filtriran_signal2[j]>filtriran_signal2[j+1] and filtriran_signal2[j]>mxv2 and filtriran_signal2[j]<mxv1:
                    mxv2=filtriran_signal2[j]
                    mxvi2=j
            for j in range(nizindexa[i]-w, nizindexa[i]+w):
                if filtriran_signal2[j]>filtriran_signal2[j-1] and filtriran_signal2[j]>filtriran_signal2[j+1] and filtriran_signal2[j]>mxv3 and filtriran_signal2[j]<mxv2:
                    mxv3=filtriran_signal2[j]
                    mxvi3=j
            f=[mxvi1, mxvi2, mxvi3]
            mxf=-1
            for j in range(len(f)):
                if f[j]>mxf:
                    mxv=f[j]
        listaindexa.append(mxvi1)
    listaindexa=list(dict.fromkeys(listaindexa))
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


