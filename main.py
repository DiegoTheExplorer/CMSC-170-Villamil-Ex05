#Remember to use the decimal datatype for precision
import Bow as bow

import tkinter as tk
from tkinter import filedialog

import os
import numpy
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

  print("HAM")
  print("Dictionary Size: " + str(ham.dictSize))
  print("Total Number of Words: " + str(ham.totalWords))
  
  print("SPAM")
  print("Dictionary Size: " + str(spam.dictSize))
  print("Total Number of Words: " + str(spam.totalWords))

  fileOut = open("classify.out", "a", encoding='latin1')
  fileOut.truncate(0)

  k = int(kTxt.get(1.0, "end-1c"))
  pSpam = Decimal((spam.msgNum + k) / ((spam.msgNum + ham.msgNum) + 2 * k))
  pHam = Decimal((ham.msgNum + k) / ((spam.msgNum + ham.msgNum) + 2 * k))

  k = Decimal(k)
  dictSizeSpam = Decimal(spam.dictSize)
  totalWordsSpam = Decimal(spam.totalWords)
  dictSizeHam = Decimal(ham.dictSize)
  totalWordsHam = Decimal(ham.totalWords)
  fileCtr = 1

  #Making a dictionary of all the unique words found in Spam and Ham
  dictSpamHam = spam.dict.copy()

  for key in ham.dict:
    if(key in dictSpamHam):
      dictSpamHam[key] = dictSpamHam[key] + ham.dict[key]

  dictSize = len(dictSpamHam)

  for filename in messages:
    #create a bag of words using words from path
    path = msgsPath.get() + "/" + filename
    file = open(path, encoding='latin1')
    messageBow = bow.Bow(path)

    pWordSpam = []
    pWordHam = []
    pMsgSpam = Decimal(0)
    pMsgHam = Decimal(0)
    pMsg = Decimal(0)
    pSpamMsg = Decimal(0)
    pHamMsg = Decimal(0)

    #get the number of new words
    newWords = 0
    for word in messageBow.dict:
      if(word not in spam.dict and word not in ham.dict):
        newWords = newWords + 1
    newWordsD = Decimal(newWords)

    for word in messageBow.dict:
      #calculate P(w|Spam) then append to pWordSpam
      if(word in spam.dict):
        wordInSpam = Decimal(spam.dict[word])
      else:
        wordInSpam = Decimal(0)
      pWordSpam.append((wordInSpam + k) /
                        ((totalWordsSpam) + (k * (dictSize + newWordsD))))
      
      #calculate P(w|Ham) then append to pWordHam
      if(word in ham.dict):
        wordInHam = Decimal(ham.dict[word])
      else:
        wordInHam = Decimal(0)
      pWordHam.append((wordInHam + k) / 
                       ((totalWordsHam) + (k * (dictSize + newWordsD))))
    
    #calculate P(message|Spam) and P(message|Ham)
    pMsgSpam = numpy.prod(pWordSpam)
    pMsgHam = numpy.prod(pWordHam)

    pMsg = (pMsgHam * pHam) + (pMsgSpam * pSpam)#P(message)

    pSpamMsg = (pMsgSpam * pSpam)/ (pMsgSpam + pMsgHam)
    pHamMsg = (pMsgHam * pHam)/ (pMsgSpam + pMsgHam)

    zeros = "0" * (3 - len(str(fileCtr)))
    fileNum = zeros + str(fileCtr)

    if(pSpamMsg >= Decimal(0.5)):
      stringOut = fileNum + " SPAM " + str(pSpamMsg) + "\n"
    else:
      stringOut = fileNum + " HAM " + str(pHamMsg) + "\n"
    fileOut.write(stringOut)
    fileCtr += 1

  fileOut.write("\n")
  fileOut.write("HAM\n")
  temp = "Dictionary Size: " + str(dictSizeHam) + "\n"
  fileOut.write(temp)
  temp = "Total Number of Words: " + str(totalWordsHam) + "\n"
  fileOut.write(temp)
  fileOut.write("\n")

  fileOut.write("SPAM\n")
  temp = "Dictionary Size: " + str(dictSizeSpam) + "\n"
  fileOut.write(temp)
  temp = "Total Number of Words: " + str(totalWordsSpam) + "\n"
  fileOut.write(temp)
  file.close()
  fileOut.close()

  return

def makeBag(dir, bag):
  bag.empty()
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