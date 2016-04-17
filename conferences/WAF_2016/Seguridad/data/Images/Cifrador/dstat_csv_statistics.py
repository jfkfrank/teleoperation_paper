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


from Tkinter import Tk
from tkFileDialog import askopenfilename
from Tkinter import *
import ttk

DEBUG = False


class Checkbar(Frame):
   def __init__(self, parent=None, picks=[], side=LEFT, anchor=W):
      Frame.__init__(self, parent)
      self.vars = []
      for pick in picks:
         var = IntVar()
         chk = Checkbutton(self, text=pick, variable=var)
         chk.pack(side=side, anchor=anchor, expand=YES)
         self.vars.append(var)
         
   def state(self):
      return map((lambda var: var.get()), self.vars)
      
      

#class principal()
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
	  opts, args = getopt.getopt(argv,"hi:o:g",["ifile=","ofile="])
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
          elif opt in ("-g", "--gui"):
                Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
                inputfile = askopenfilename() # show an "Open" dialog box and return the path to the selected file
                print(inputfile)
                
                
		 
	print 'Input file is "', inputfile
	print 'Output file is "', outputfile
   
   
	with open(inputfile) as f:
		headers1 = f.next()
		headers2 = f.next()
		v_reader = csv.reader(f, delimiter=";")
		tmp = [i for i in v_reader]
		#print([i for i in reader])  
		
	csvReader = csv.reader(open(inputfile), delimiter=';')
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
	
	if DEBUG:
          root = Tk()
          lng = Checkbar(root, headers1)
          tgl = Checkbar(root, headers2)
          lng.pack(side=TOP,  fill=X)
          tgl.pack(side=LEFT)
          lng.config(relief=GROOVE, bd=2)

          def allstates(): 
              print(list(lng.state()), list(tgl.state()))
            
          Button(root, text='Quit', command=root.quit).pack(side=RIGHT)
          Button(root, text='Accept', command=allstates).pack(side=RIGHT)
        
          root.mainloop()
          
	for index,item in enumerate(headers2):
	  try:
		if headers1[index] != '':
                  print "*****************************************************"
                  print headers1[index]
                  print "*****************************************************"
                  
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

