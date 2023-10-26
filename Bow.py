import re

class Bow:

  def __init__(self, file):
    self.file = file
    self.dict = {}
    self.totalWords = 0
    self.dictSize = 0
    self.updateDict(file)

  def updateDict(self, file):
    tokens = []
    totalWords = 0

    if(file == None):
      print("Created an empty bag of words")
      return
  
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
        tokens[idx] = re.sub('[^0-9a-zA-Z]',"",tokens[idx]).lower()
    totalWords = len(tokens)
    tokens = sorted(tokens)

    #create dictionary
    for tkn in tokens:
      if(tkn == ""):
        tokens.remove(tkn)
      elif(tkn in self.dict):
        self.dict[tkn] += 1
      else:
        self.dict[tkn] = 1
    
    self.totalWords = self.totalWords + totalWords
    self.dictSize = len(self.dict)

    return 