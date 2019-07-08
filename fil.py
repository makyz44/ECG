import matplotlib.pyplot as plt 
from math import sin, pi 
import sys 
from scipy.signal import butter, lfilter
from scipy import signal

def butter_lowpass(cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

def butter_lowpass_filter(data, cutoff, fs, order=5):
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = lfilter(b, a, data)
    return y

def butter_highpass(cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = signal.butter(order, normal_cutoff, btype='high', analog=False)
    return b, a

def butter_highpass_filter(data, cutoff, fs, order=5):
    b, a = butter_highpass(cutoff, fs, order=order)
    y = signal.filtfilt(b, a, data)
    return y

#def filter1(x):
#    y = [0]*21600
#    for n in range(4, len(x)):
#        y[n] = 0.0101*x[n] - 0.0202*x[n-2] + 0.0101*x[n-4] + 2.4354*y[n-1] - 3.1869*y[n-2] + 2.0889*y[n-3] - 0.7368*y[n-4]
#    return y

#def filter2(x):
#    y = [0]*21600
#    for n in range(8, len(x)):
#        y[n] = y[n-1] + 0.125*x[n] - 0.125*x[n-8] 
#    return y

#frequency = 500

#input = [0]*21600
#output = [0]*21600

#for i in range(21600):
#    input[i] = sin(2 * pi * frequency * i / 21600) + sin(2 * pi * 70 * i / 21600)

#output = filter(input)

#output_section = output[0:480]  
#input_section = input[0:480] 

#plt.figure(1)                
#plt.subplot(211)   
#plt.ylabel('magnitude')
#plt.xlabel('samples') 
#plt.title('unfiltered signal')      
#plt.plot(input_section)
#plt.subplot(212)             
#plt.ylabel('magnitude')
#plt.xlabel('samples') 
#plt.title('filtered signal')
#plt.plot(output_section)
#plt.show()