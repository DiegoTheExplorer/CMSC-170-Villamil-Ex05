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
  pSpam = Decimal((spam.totalWords + k) / (spam.totalWords + ham.totalWords) + 2 * k)
  pHam = Decimal((ham.totalWords + k) / (spam.totalWords + ham.totalWords) + 2 * k)
  print("pSpam: ", pSpam)
  print("pHam: ", pHam)
  k = Decimal(k)
  pWordgSpam = []
  pWordgHam = []

  for filename in messages:
    #create a bag of words using words from path
    path = msgsPath.get() + "/" + filename
    file = open(path, encoding='ISO-8859-1')
    messageBow = bow.Bow(path)

    #get the number of new words
    newWords = 0
    for word in messageBow.dict:
      if(word not in spam.dict and word not in ham.dict):
        newWords = newWords + 1
    newWordsD = Decimal(newWords)

    for word in messageBow.dict:
      #calculate P(w|Spam) then append to pWordgSpam
      if(word in spam.dict):
        wordInSpam = Decimal(spam.dict[word])
      else:
        wordInSpam = Decimal(0)
      totalWordsSpam = Decimal(spam.totalWords)
      dictSizeSpam = Decimal(spam.dictSize)
      pWordgSpam.append((wordInSpam + k) /
                        (totalWordsSpam) + (k * (dictSizeSpam + newWordsD)))
      
      #calculate P(w|Ham) then append to pWordgHam
      if(word in ham.dict):
        wordInHam = Decimal(ham.dict[word])
      else:
        wordInHam = Decimal(0)
      totalWordsHam = Decimal(ham.totalWords)
      dictSizeHam = Decimal(ham.dictSize)
      pWordgHam.append((wordInHam + k) / 
                       (totalWordsHam) + (k * (dictSizeHam + newWordsD)))
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