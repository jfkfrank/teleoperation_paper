#!/usr/bin/env python
## Para limpiar los ficheros desde la shell
## cat Log_decryption.txt | cut -d " " -f 5 > Log_decryption_clean.txt

#from matplotlib.pyplot import *
import matplotlib.pyplot as plt
import numpy as np

from scipy.stats.kde import gaussian_kde
from scipy.interpolate import UnivariateSpline
#from scipy import stats
import scipy.stats as ss


#with open("Log_mas_limpio.txt", "r") as ins:
    #array = []
    #for line in ins:
        #array.append(line.rstrip())
        
data_cifrado = np.genfromtxt("Log_encryption_clean.txt",delimiter="\n")
data_descifrado = np.genfromtxt("Log_decryption_clean.txt",delimiter="\n")

##################################################################################### 
# create new figure
fig = plt.figure()
fig.suptitle('Data Analysis: Laser Encrypt/Decrypt (DES3)', fontsize=16, fontweight='bold')
##################################################################################### 


####################### ######################### 
# Box-Plot
####################### ######################### 


#####Caso Cifrado
ax = fig.add_subplot(221)
ax.set_title('Box-Plot')
ax.set_xlabel('Encryption')
ax.set_ylabel('Time (seconds)')
ax.set_ylim([0,0.015])
ax.boxplot(data_cifrado)

#####Caso Descifrado
ax = fig.add_subplot(222)
ax.set_title('Box-Plot')
ax.set_xlabel('Decryption')
ax.set_ylabel('Time (seconds)')
ax.set_ylim([0,0.015])
ax.boxplot(data_descifrado)

ax = fig.add_subplot(235)
ax.boxplot(data_cifrado,data_descifrado)
####################### ######################### 
# Histogramas
####################### ######################### 

#Histograma data_cifrado
ax = fig.add_subplot(223)
ax.set_title('Histogram')
ax.set_xlabel('Time (seconds)')
ax.set_ylabel('Units')

kde = gaussian_kde( data_cifrado )
# these are the values over wich your kernel will be evaluated
dist_space = np.linspace( min(data_cifrado), max(data_cifrado), 200 )
ax.plot(dist_space, kde(dist_space))


#Histograma data_descifrado
ax = fig.add_subplot(224)
ax.set_title('Histogram')
ax.set_xlabel('Time (seconds)')
ax.set_ylabel('Units')


kde = gaussian_kde( data_descifrado )
# these are the values over wich your kernel will be evaluated
dist_space = np.linspace( min(data_descifrado), max(data_descifrado), 200 )
ax.plot(dist_space, kde(dist_space))


####################### ######################### 
# Estadistica basica descriptiva
####################### ######################### 
print "======================================"
print "Cifrado"
print "======================================"

desc = ss.describe(data_cifrado)

names = ["length", "min", "max", "mean", "stdev"]
desc = [desc[0], desc[1][0],desc[1][1], desc[2],desc[3]]

for i in range(5):
    print "Cifrado %s: %f" % (names[i], desc[i])

####Para calcular el valor moda
print "El valor moda de la fase de cifrado fue:"
print ss.mode(data_cifrado)

print "======================================"
print "Descifrado"
print "======================================"
desc = ss.describe(data_descifrado)

names = ["length", "min", "max", "mean", "stdev"]
desc = [desc[0], desc[1][0],desc[1][1], desc[2],desc[3]]

for i in range(5):
    print "Descifrado %s: %f" % (names[i], desc[i])

print "El valor moda de la fase de descifrado fue:"
print ss.mode(data_descifrado)



####################### ######################### 
# Mostrar Por pantalla
####################### ######################### 
plt.show()
#print array

## some simple data
#x = [1,2,3,4]
#y = [5,4,3,2]
## create new figure
#figure()
## divide subplots into 2 x 3 grid
## and select #1
#subplot(231)
#plot(x, y)
## select #2
#subplot(232)
#bar(x, y)
## horizontal bar-charts
#subplot(233)
#barh(x, y)
## create stacked bar charts
#subplot(234)
#bar(x, y)
## we need more data for stacked bar charts
#y1 = [7,8,5,3]
#bar(x, y1, bottom=y, color = 'r')
## box plot
#subplot(235)
#boxplot(data)

## scatter plot
#subplot(236)
#scatter(x,y)
#show()

