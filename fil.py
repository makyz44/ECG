import matplotlib.pyplot as plt 
from math import sin, pi 
import sys 

def filter(x):
    y = [0]*21600
    for n in range(240, len(x)):
        #y[n] = 0.0101*x[n] - 0.0202*x[n-2] + 0.0101*x[n-4] + 2.4354*y[n-1] - 3.1869*y[n-2] + 2.0889*y[n-3] - 0.7368*y[n-4] 
        #y[n] = 0.0101*x[n] - 0.0202*x[n-2] + 0.0101*x[n-4] + 2.4354*y[n-1] - 3.1869*y[n-2] + 2.0889*y[n-3] - 0.7368*y[n-4]
        #y[n] = 2 * y[n-1] - y[n-2] + x[n] - 2 * x[n - 10] + x[n - 20]
        y[n]=y[n-120]-((y[n - 1] + x[n] - y[n - 240])/240)
    return y

#frequency = 500

#input = [0]*21600
#output = [0]*21600

#for i in range(21600):
#    input[i] = sin(2 * pi * frequency * i / 21600) + sin(2 * pi * 70 * i / 21600)

#output = filter(input)

##output_section = output[0:480]  
##input_section = input[0:480] 

#plt.figure(1)                
#plt.subplot(211)   
#plt.ylabel('Magnitude')
#plt.xlabel('Samples') 
#plt.title('Unfiltered Signal')      
#plt.plot(input_section)
#plt.subplot(212)             
#plt.ylabel('Magnitude')
#plt.xlabel('Samples') 
#plt.title('Filtered Signal')
#plt.plot(output_section)
#plt.show()