import _tkinter
from Tkinter import *
import Tkinter
import sys
import os
import string
import random
from operator import itemgetter
import time

# format of friend_info < username, score >
my_friendlist = []

def poll():
  lab.after(200, poll)
  sel = L.curselection()
  lab.config(text=str(sel))
def generateUsername():
  charSet = 'abcdefghijklmnopqrstuvwxyz1234567890'
  minLength = 5
  maxLength = 10
  length = random.randint(minLength, maxLength)

  return ''.join(map(lambda unused : random.choice(charSet), range(length)))

def generateNamelist(size):
  result = []
  for i in range(size):
    result.append((generateUsername(),random.randint(0,100)))
  return result

def generatePin(size):
    result = []
    for i in range(size):
        result.append((generatePin()))
    return result
  
    ########### Code for Visualization ##########
while True:
  F1 = Tkinter.Frame()
  s = Tkinter.Scrollbar(F1)
  L = Tkinter.Listbox(F1)

  s.pack(side=Tkinter.RIGHT, fill=Tkinter.Y)
  L.pack(side=Tkinter.LEFT, fill=Tkinter.Y)

  s['command'] = L.yview
  L['yscrollcommand'] = s.set


  F1.pack(side=Tkinter.TOP)

  F2 = Tkinter.Frame()
  lab = Tkinter.Label(F2)



  print generateNamelist(random.randint(0,10))
  print "reading the new pins..."
  # Pin format < username, longitude, latitude, time_stamp >
  my_friendlist += generateNamelist(random.randint(0,10))
  print len(my_friendlist)
  my_friendlist = sorted(my_friendlist, key=itemgetter(1), reverse=True)
  for i in range(len(my_friendlist)): 
    L.insert(Tkinter.END, my_friendlist[i])
  
  print my_friendlist
  print "reading new geo_location information crossovers..."
  # Pin format < username, longitude, latitude, time_stamp >
    
  print "reading new common_interests:"
    
  print "This prints once a second."
    

  
  
  lab.pack()
  F2.pack(side=Tkinter.TOP)
  poll()
  Tkinter.mainloop()
##  time.sleep(1)  # Delay for 1 second  
################# Code for Visualization#############
  



