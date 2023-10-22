#Remember to use the decimal datatype for precision
import Bow as bow

import tkinter as tk
from tkinter import filedialog

import os
from functools import partial
from decimal import *

def classify(kTxt, spam, ham, messages, msgsPath):
  missingDirectory = 0

  #check if any of the input directories are missing
  if(spam.dictSize == 0):
    missingDirectory += missingDirectory + 1
    print("No spam folder selected")
  if(ham.dictSize == 0):
    missingDirectory += missingDirectory + 1
    print("No ham folder selected")
  if(len(classifyFiles) == 0):
    missingDirectory += missingDirectory + 1
    print("No classify directory selected")
  
  if(missingDirectory > 0):
    return

  k = int(kTxt.get(1.0, "end-1c"))
  pSpam = (spam.totalWords + k) / (spam.totalWords + ham.totalWords) + 2 * k
  pHam = (ham.totalWords + k) / (spam.totalWords + ham.totalWords) + 2 * k

  for filename in messages:
    path = msgsPath.get() + "/" + filename
    file = open(path, encoding='ISO-8859-1')
    messageBow = bow.Bow(path)

  return

def makeBag(dir, bag):
  path = filedialog.askdirectory(initialdir= "data/")
  dir.set(path)
  files = os.listdir(dir.get())#gets a list of all the filenames in path

  #for every file update the bag of words
  for file in range(0,len(files)):
    pathToFile = path + "/" + files[file]
    bag.updateDict(pathToFile)
  
  # print(path)
  # print("Dictionary size: ", bag.dictSize)
  # print("Total number of words: ", bag.totalWords)

  return

def getFiles(dir, files):
  path = filedialog.askdirectory(initialdir= "data/")
  dir.set(path)

  #for every message filename in path append to files
  for message in os.listdir(dir.get()):
     files.append(message)

  return



#Start of app
root = tk.Tk()
root.geometry("600x500")
root.title('Spam Ham')

spamDir = tk.StringVar()
spamBow = bow.Bow(None)
fileSelectSpam = tk.Button(root, 
                           text="Select Spam Dir", 
                           command=partial(makeBag, spamDir, spamBow))
fileSelectSpam.grid(row = 0, column = 0)

hamDir = tk.StringVar()
hamBow = bow.Bow(None)
fileSelectHam = tk.Button(root, 
                           text="Select Ham Dir", 
                           command=partial(makeBag, hamDir, hamBow))
fileSelectHam.grid(row = 0, column = 1)

classifyDir = tk.StringVar()
classifyFiles = []
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
                           command=partial(classify, kValInputBox, spamBow, hamBow, classifyFiles, classifyDir))
classifyButton.grid(row = 0, column = 5)

root.mainloop()