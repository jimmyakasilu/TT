import Tkinter as tk
from ttk import *
from Buttons import *
win = tk.Tk()
win.title("Alphabets")
#...................................................................#
jimmy = tk.LabelFrame(win,text = 'Alphabets')
jimmy.pack(padx = 10, pady = 10, expand=True, fill='both' )
jimmy.configure(background = 'white')
AlphaStr = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
AlphaLow = AlphaStr.lower()
c = 0
r = 0
num = 26
action=list(AlphaStr)
from ImageInButton import *
commands = {'A':A,'B':B,'C':C,'D':D,'E':E,'F':F,'G':G,'H':H,'I':I,'J':J,'K':K,
                    'L':L,'M':M,'N':N,'O':O,'P':P,'Q':Q,'R':R,'S':S,'T':T,'U':U,'V':V,
                     'W':W,'X':X,'Y':Y,'Z':Z}
for i in xrange(0,num):
    if AlphaStr[i] not in ['Y','Z']:
        action[i] = tk.Button(jimmy, image = Photo[i], command = commands[AlphaStr[i]], width = 120, height = 120)
        action[i].grid(column = c, row = r,padx =10, pady =10, sticky = 'NSEW')
        action[i].configure(background = 'white')
        win.bind(AlphaLow[i],commands[AlphaStr[i]])
        if c<8:
            c=c+1
        if c==8:
            c=0
            r=r+1
    else:
        action[i] = tk.Button(jimmy, image = Photo[i], command = commands[AlphaStr[i]], width = 120, height = 120)
        action[i].grid(column = c, row = r, columnspan = 4, padx =10, pady =10, sticky = 'NSEW')
        action[i].configure(background = 'white')
        win.bind(AlphaLow[i],commands[AlphaStr[i]])
        c=c+4
win.mainloop()
