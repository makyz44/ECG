import os
import fil
import numpy as np
import matplotlib.pyplot as plt
import math
import time

#kvadriran=[]
#posleizvoda=[]
#rr=[]
#signal=[]
#apsolutni=[]
#skalirani=[]
#accalg=[]
#nizindexa2=[]
#nizindexa3=[]
#ns=[]
#opt=[]
ukupno=0

def tacnost(rezultat, dataset):
    b=0
    for i in range(len(dataset)):
        for j in range(len(rezultat)):
            if dataset[i]==rezultat[j] or dataset[i]==rezultat[j]-1 or dataset[i]==rezultat[j]+1:
                b=b+1
    acc=(b*100/len(dataset))
    return acc

def get_sec(time_str):
    m, s = time_str.split(':')
    return int(m) * 60 + float(s)

for k in range(1, 49):
    kvadriran=[]
    posleizvoda=[]
    rr=[]
    signal=[]
    apsolutni=[]
    skalirani=[]
    nizindexa2=[]
    nizindexa3=[]
    naj=[]
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

    filtriran_signal=fil.butter_highpass_filter(signal, 0.5, 360)

    kvadriran = list(np.array(filtriran_signal)**2)

    for i in range(len(filtriran_signal)-1):
        posleizvoda.append(filtriran_signal[i+1]-filtriran_signal[i])

    for i in range(len(posleizvoda)):
        apsolutni.append(abs(posleizvoda[i]))

    mx=-1

    for i in range(len(apsolutni)):
        if apsolutni[i]>mx:
            mx=apsolutni[i]

    for i in range(len(apsolutni)):
        skalirani.append(apsolutni[i]*(1/mx))
    
    for u in range(-30, 31):
        opt=[]
        accalg=[]
        ns=[]
        th=0.1
        while(th<1):
            nizindexa=[]
            for i in range(1, len(skalirani)-1):
                if skalirani[i]>th and skalirani[i]>skalirani[i-1] and skalirani[i]>skalirani[i+1]:
                    nizindexa.append(i+u)
            nizindexa=[round(x) for x in nizindexa]
            if tacnost(nizindexa, rr) <= 100:
                accalg.append(tacnost(nizindexa, rr))
                ns.append(len(nizindexa))
            th=th+0.01

        mn=50000
        for i in range(len(ns)):
            opt.append(accalg[i]/abs((len(rr)/(ns[i]+0.01))-1))

        mxi=0
        inx=0
        for i in range(len(opt)):
            if opt[i]>mxi:
                mxi=opt[i]
                inx=i
        naj.append(accalg[inx])
    mxnaj=0
    for i in range(len(naj)):
        if naj[i]>mxnaj:
            mxnaj=naj[i]
    print(k)
    print(mxnaj)
    ukupno=ukupno+mxnaj

print("Ukupno")
print(ukupno/48)



