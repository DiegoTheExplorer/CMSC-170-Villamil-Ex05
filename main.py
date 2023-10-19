#Remember to use the decimal datatype for precision
import Bow as bow

import tkinter as tk
from tkinter import filedialog

import os
from functools import partial
from decimal import *

def classify(kTxt, spam, ham, messages):
  k = int(kTxt.get(1.0, "end-1c"))
  pSpam = (spam.totalWords + k) / (spam.totalWords + ham.totalWords) + 2 * k
  pHam = (ham.totalWords + k) / (spam.totalWords + ham.totalWords) + 2 * k

  
  for message in messages:
    

  return

def makeBag(dir, bag):
  path = filedialog.askdirectory(initialdir= "data/")
  dir.set(path)
  files = os.listdir(dir.get())

  for file in range(0,len(files)):
    pathToFile = path + "/" + files[file]

    if(file == 0):
      bag = bow.Bow(pathToFile)
    else:
      bag.updateDict(pathToFile)
  
  print(path)
  print("Dictionary size: ", bag.dictSize)
  print("Total number of words: ", bag.totalWords)

  return

def getFiles(dir, files):
  path = filedialog.askdirectory(initialdir= "data/")
  dir.set(path)
  files = os.listdir(dir.get()) 
  print(files)

  return



#Start of app
root = tk.Tk()
root.geometry("600x500")
root.title('Spam Ham')

spamDir = tk.StringVar()
spamBow = 0
fileSelectSpam = tk.Button(root, 
                           text="Select Spam Dir", 
                           command=partial(makeBag, spamDir, spamBow))
fileSelectSpam.grid(row = 0, column = 0)

hamDir = tk.StringVar()
hamBow = 0
fileSelectHam = tk.Button(root, 
                           text="Select Ham Dir", 
                           command=partial(makeBag, hamDir, hamBow))
fileSelectHam.grid(row = 0, column = 1)

classifyDir = tk.StringVar()
classifyFiles = 0
fileSelectClassify = tk.Button(root, 
                           text="Select Classify Dir", 
                           command=partial(getFiles, classifyDir, classifyFiles))
fileSelectClassify.grid(row = 0, column = 2)

kLabel = tk.Label(root, text = "K: ")
kLabel.grid(row = 0, column = 3)

kVal = 0
kValInputBox = tk.Text(root, height = 1, width = 5)
kValInputBox.grid(row = 0, column = 4)

classifyButton = tk.Button(root, 
                           text="Classify", 
                           command=partial(classify, kValInputBox, spamBow, hamBow, classifyFiles))
classifyButton.grid(row = 0, column = 5)

root.mainloop()