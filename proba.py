import os
import EKG
import fil
import numpy as np
import matplotlib.pyplot as plt
import math
import time
import treci

print("Testiranje...")

listaindexa=[2, 5, 7, 9, 17, 19, 23, 24, 27, 29, 30, 32, 40, 41, 43, 47]

for i in range(len(listaindexa)):
    niztacnosti=[]
    naj=0
    freq=0.1
    while(freq<5):
        freq=freq+0.3
        niztacnosti.append(treci.trecialg(freq, listaindexa[i]))
    for j in range(len(niztacnosti)):
        if niztacnosti[j]>naj:
            naj=niztacnosti[j]
    print(listaindexa[i])
    print(naj)