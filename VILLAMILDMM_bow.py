import re

tokens = []
dictionary = {}
totalWords = 0

fp = open("003.txt", "r")

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

#write to output.txt
fp = open("output.txt", "w")

#write header
tempStr = "Dictionary Size: " + str(len(dictionary)) + "\n"
fp.write(tempStr)
tempStr = "Total Number of Words: " + str(totalWords) + "\n"
fp.write(tempStr)

#write words
for word in dictionary:
  tempStr = word + " " + str(dictionary[word]) + "\n"
  fp.write(tempStr)

fp.close()