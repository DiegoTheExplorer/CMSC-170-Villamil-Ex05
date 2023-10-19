#Remember to use the decimal datatype for precision
import Bow as bow

import tkinter as tk
from tkinter import filedialog

import os
from functools import partial

def classify(k):
  inp = k.get(1.0, "end-1c")
  print(inp)

  return

def getFiles(dir, bag):
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
  

#Start of app
root = tk.Tk()
root.geometry("600x500")
root.title('Spam Ham')

spamDir = tk.StringVar()
spamBow = 0
fileSelectSpam = tk.Button(root, 
                           text="Select Spam Dir", 
                           command=partial(getFiles, spamDir, spamBow))
fileSelectSpam.grid(row = 0, column = 0)

hamDir = tk.StringVar()
hamBow = 0
fileSelectHam = tk.Button(root, 
                           text="Select Ham Dir", 
                           command=partial(getFiles, hamDir, hamBow))
fileSelectHam.grid(row = 0, column = 1)

classifyDir = tk.StringVar()
classifyBow = 0
fileSelectClassify = tk.Button(root, 
                           text="Select Classify Dir", 
                           command=partial(getFiles, classifyDir, hamBow))
fileSelectClassify.grid(row = 0, column = 2)

kLabel = tk.Label(root, text = "K: ")
kLabel.grid(row = 0, column = 3)

kVal = 0
kValInputBox = tk.Text(root, height = 1, width = 5)
kValInputBox.grid(row = 0, column = 4)

classifyButton = tk.Button(root, 
                           text="Select Ham Dir", 
                           command=partial(classify, kValInputBox))
classifyButton.grid(row = 0, column = 5)

root.mainloop()