#from matplotlib.pyplot import *
import matplotlib.pyplot as plt
import numpy as np

from scipy.stats.kde import gaussian_kde
from scipy.interpolate import UnivariateSpline
#from scipy import stats
import scipy.stats as ss
import csv
import sys
import getopt

DEBUG = False

def help():
	print 'test.py -i <inputfile> -o <outputfile>'
	sys.exit(2)


def main(argv):
	total = len(sys.argv)
	if total == 1:
		help()	
		
	inputfile = ''
	outputfile = ''
	try:
	  opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
	except getopt.GetoptError:
		help()
			  
	for opt, arg in opts:
	  if opt == '-h':
		 print 'test.py -i <inputfile> -o <outputfile>'
		 sys.exit()
	  elif opt in ("-i", "--ifile"):
		 inputfile = arg
	  elif opt in ("-o", "--ofile"):
		 outputfile = arg
		 
		 
	print 'Input file is "', inputfile
	print 'Output file is "', outputfile
   
   
	with open(inputfile) as f:
		headers1 = f.next()
		headers2 = f.next()
		v_reader = csv.reader(f, delimiter=";")
		tmp = [i for i in v_reader]
		#print([i for i in reader])  
		
	csvReader = csv.reader(open('fichero_salida_b1.csv'), delimiter=';')
	headers1 = csvReader.next()
	headers2 = csvReader.next()
	values = [map(float, row) for row in csvReader]

        if DEBUG:
          print headers1
          print headers2
          print ("Los elementos de la cabecera son %d")%len(headers2)
          print len([x[0] for x in tmp])
          print len(values)
          print len(tmp)
          print type(values)
          print type(tmp)
	 
	 
	for index,item in enumerate(headers2):
	  try:
		
		print item 
		element = [float(x[index]) for x in tmp]
		desc = ss.describe(element)
		names = ["length", "min", "max", "mean", "stdev"]
		desc = [desc[0], desc[1][0],desc[1][1], desc[2],desc[3]]

		for i in range(5):
		  print "Cifrado %s: %f" % (names[i], desc[i])
		  
		print "El valor moda del elemento %s: %s" %  (item,ss.mode(element),)

	  except:
		print "Unexpected error:", sys.exc_info()
		

if __name__ == "__main__":
   main(sys.argv[1:])

