import numpy as np
import csv as csv
import pandas as pd

#readdata = csv.reader(open('fichero_salida_b.csv', 'r'))
#data = []
#for row in readdata:
    #data.append(row)
#Header = data[0]
#data.pop(0)
#print data

df = pd.read_csv("fichero_salida_b.csv", delimiter=';')
print df
print df.mean()
