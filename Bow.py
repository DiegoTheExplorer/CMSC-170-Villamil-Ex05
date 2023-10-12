import re

class Bow:

  def __init__(self, file):
    self.file = file
    self.dict = self.makeDict(file)
    self.totalWords = 0
    self.dictSize = 0

  def makeDict(self, file):
    tokens = []
    dictionary = {}
    totalWords = 0

    fp = open(file)

    #tokenize
    for line in fp:
      tempLine = line.split()
      for word in tempLine:
          tokens.append(word)

    fp.close()

    #clean
    for idx in range(0,len(tokens)):
      if(tokens[idx] != ""):
        tokens[idx] = re.sub('\W+',"",tokens[idx]).lower()
    totalWords = len(tokens)
    tokens = sorted(tokens)

    #create dictionary
    for tkn in tokens:
      if(tkn == ""):
        tokens.remove(tkn)
      elif(tkn in dictionary):
        dictionary[tkn] += 1
      else:
        dictionary[tkn] = 1
    
    self.totalWords = totalWords
    self.dictSize = len(dictionary)

    return dictionary