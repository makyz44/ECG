import os
import matplotlib.pyplot as plt
import numpy as np
import plotly.plotly as py
from math import pi 
import scipy.signal as sig
import fil

signal=[]
signal2=[]
posleizvoda=[]
spoj=[]
pros=0
binar=[]
abssig=[]
nizindexa=[]
sigind=[]
rr=[]

def get_sec(time_str):
    m, s = time_str.split(':')
    return int(m) * 60 + float(s)

print(get_sec('3:43.028'))


with open("C:\\Users\\Pc\\Documents\\rr.txt") as file:
    for line in file: 
        #line = line.strip() #or some other preprocessing
        rr.append(get_sec(line)) #storing everything in memory!

with open("C:\\Users\\Pc\\Documents\\sample.txt") as file:
    for line in file: 
        line = line.strip() #or some other preprocessing
        signal.append(float(line)) #storing everything in memory!

####################################################
#signal2=fil.filter(signal)

for i in range(len(signal)-1):
    posleizvoda.append(signal[i+1]-signal[i])

for i in range(len(posleizvoda)):
    spoj.append(posleizvoda[i]/(signal[i]+0.0001))

for i in range(len(spoj)):
    binar.append(0)

for i in range(len(spoj)):
    abssig.append(abs(spoj[i]))

for i in range(1,len(abssig)-1):
    if abssig[i]>1 and abssig[i]>abssig[i+1] and abssig[i]>abssig[i-1]:
        binar[i]=1
    else:
        binar[i]=0

for i in range(len(binar)-100):
    if binar[i]==1:
        for j in range(i+1, i+100):
            if binar[j]==1:
                nizindexa.append((i+j)/2)

nizindexa = [round(x) for x in nizindexa]

#print(nizindexa)

for i in range(len(binar)):
    sigind.append(0)

for i in range(len(nizindexa)):
    sigind[nizindexa[i]+1]=2

for i in range(len(rr)):
    rr[i]=rr[i]*360

rr = [round(x) for x in rr]

b=0
for i in range(len(rr)):
    for j in range(len(nizindexa)):
        if rr[i]==nizindexa[j] or rr[i]==nizindexa[j]+1 or rr[i]==nizindexa[j]-1:
            b=b+1

#print(b/len(rr))


plt.plot(signal)
#plt.plot(sigind)
plt.show()