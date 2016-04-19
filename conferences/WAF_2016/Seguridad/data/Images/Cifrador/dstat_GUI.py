from Tkinter import *
import csv

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


class Quitter(Frame):                         
    def __init__(self, parent=None):          
        Frame.__init__(self, parent)
        self.pack()
        widget = Button(self, text='Quit', command=self.quit)
        widget.pack(expand=YES, fill=BOTH, side=LEFT)
    def quit(self):
        ans = askokcancel('Verify exit', "Really quit?")
        if ans: Frame.quit(self)


if __name__ == '__main__':
    inputfile = "laser_dstat.csv"
    csvReader = csv.reader(open(inputfile), delimiter=';')
    headers1 = csvReader.next()
    headers2 = csvReader.next()
    values = [map(float, row) for row in csvReader]

    sub_headers1 = []
    sub_headers2 = []
    sub_headers3 = []
    sub_headers4 = []
    sub_headers5 = []
    sub_headers6 = []
    sub_headers7 = []
    sub_headers8 = []
    sub_headers9 = []
    sub_headers10 = []
    sub_headers11 = []
    sub_headers12 = []
    sub_headers13 = []
    
    print len(headers2)
    for index,item in enumerate(headers2):
      if(index < 2):
	sub_headers1.append(item)
      elif(index > 1 and index <4):
	sub_headers2.append(item)
      elif(index > 3 and index <4):
      elif(index > 29):
	sub_headers3.append(item)
      
    print sub_headers1
    print sub_headers2
    print sub_headers3
    root = Tk()
    lng1 = Checkbar(root, sub_headers1)
    lng2 = Checkbar(root, sub_headers2)
    lng3 = Checkbar(root, sub_headers3)
    tgl = Checkbar(root, ['All'])
    lng1.pack(side=TOP,  fill=X)
    lng2.pack(side=TOP,  fill=X)
    lng3.pack(side=TOP,  fill=X)
    tgl.pack(side=LEFT)
    lng3.config(relief=GROOVE, bd=2)

    def allstates(): print lng1.state(), lng2.state(),lng3.state(),tgl.state()
    Quitter(root).pack(side=RIGHT)
    Button(root, text='Peek', command=allstates).pack(side=RIGHT)
    root.mainloop()
