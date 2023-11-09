import re

class Bow:

  def __init__(self, file):
    self.file = file
    self.dict = {}
    self.totalWords = 0
    self.dictSize = 0
    self.msgNum = 0
    self.updateDict(file)

  def empty(self):
    self.__init__(None)

  def sortDict(self):
    view = self.dict.items()
    view = sorted(view)
    self.dict = dict(view)
    return

  def updateDict(self, file):

    if(file == None):
      print("Created an empty bag of words")
      return
    
    tokens = []
    totalWords = 0
  
    fp = open(file, encoding='latin1')

    #tokenize
    for line in fp:
      tempLine = line.split()
      for word in tempLine:
          tokens.append(word)

    fp.close()

    #clean
    for idx in range(0,len(tokens)):
      if(tokens[idx] != ""):
        tokens[idx] = re.sub("[^0-9a-zA-Z]","",tokens[idx]).lower()

    #create dictionary
    for tkn in tokens.copy():
      if(tkn == ""):
        tokens.remove(tkn)
      elif(tkn in self.dict):
        self.dict[tkn] += 1
      else:
        self.dict[tkn] = 1
    totalWords = len(tokens)

    self.sortDict()
    self.totalWords = self.totalWords + totalWords
    self.dictSize = len(self.dict)
    self.msgNum += 1

    return 