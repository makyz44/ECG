import os
import fil
import numpy as np
import matplotlib.pyplot as plt
import math

def skaliranje(signal, th):
    skaliran=[]
    for i in range(len(signal)):
        skaliran.append(signal[i]/th)
    return skaliran

def abslist(list):
    list2=[]
    for i in range(len(list)):
        list2.append(abs(list[i]))
    return list2
        
def running_mean(l, N):
    sum = 0
    result = list( 0 for x in l)
 
    for i in range( 0, N ):
        sum = sum + l[i]
        result[i] = sum / (i+1)
 
    for i in range( N, len(l) ):
        sum = sum - l[i-N] + l[i]
        result[i] = sum / N
 
    return result

def get_sec(time_str):
    m, s = time_str.split(':')
    return int(m) * 60 + float(s)

def izvod(signal):                  #izvod
    sig=[]
    for i in range(len(signal)-1):
        sig.append(signal[i+1]-signal[i])
    return sig

def lokalnimax(signal):
    sig=[]
    for i in range(1, len(signal)-1):
        if signal[i+1]<signal[i] and signal[i-1]<signal[i]:
            sig.append(1)
        else:
            sig.append(0)
    return sig
        
def kvadrat(signal):                #kvadrat
    kv=[]
    for i in range(len(signal)):
        kv.append(signal[i]*signal[i])
    return kv

signal=[]
rr=[]
with open("C:\\Users\\Pc\\Desktop\\Peak\\p"+str(17)+".txt") as file:
    for line in file: 
        #line = line.strip() #or some other preprocessing
        rr.append(get_sec(line)) #storing everything in memory!

with open("C:\\Users\\Pc\\Desktop\\Sample\\s"+str(17)+".txt") as file:
    for line in file: 
        line = line.strip() #or some other preprocessing
        signal.append(float(line)) #storing everything in memory!

for i in range(len(rr)):
    rr[i]=rr[i]*360
rr = [round(x) for x in rr]

filtriran_signal=fil.butter_highpass_filter(signal, 1.1, 360)
filtriran_signal2=fil.butter_lowpass_filter(filtriran_signal, 150 ,360)

sigiz=izvod(filtriran_signal2)
kvadriran=kvadrat(sigiz)

rm=running_mean(filtriran_signal2, 400)
th=max(abslist(rm))

absskaliran=skaliranje(abslist(rm), th)

mxk=max(kvadriran)
thk=mxk*0.4

nizindexa=[]
for i in range(len(kvadriran)):
    if kvadriran[i]>thk and kvadriran[i]>kvadriran[i-1] and kvadriran[i]>kvadriran[i+1]:
        nizindexa.append(i-5)

nizindexa=list(dict.fromkeys(nizindexa))

print(nizindexa)
print(rr)

b=0
for i in range(len(rr)):
    for j in range(len(nizindexa)):
        if rr[i]==nizindexa[j] or rr[i]==nizindexa[j]+1 or rr[i]==nizindexa[j]-1:
            b=b+1
print(b*100/len(rr))





