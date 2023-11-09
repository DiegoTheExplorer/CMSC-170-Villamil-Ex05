import Bow as bow
import os

def makeBag(dir, bag):
  path = dir
  files = os.listdir(dir)#gets a list of all the filenames in path

  #for every file update the bag of words
  for file in range(0,len(files)):
    pathToFile = path + "/" + files[file]
    bag.updateDict(pathToFile)
  
  # print(path)
  # print("Dictionary size: ", bag.dictSize)
  # print("Total number of words: ", bag.totalWords)

  return


bag = bow.Bow(None)
dir = "data/data01/ham"
makeBag(dir,bag)

fp = open("ham01out.txt", "w")

#write words
for word in bag.dict:
  tempStr = word + " " + str(bag.dict[word]) + "\n"
  fp.write(tempStr)

tempStr = "Dictionary Size: " + str(bag.dictSize) + "\n"
fp.write(tempStr)
tempStr = "Total Number of Words: " + str(bag.totalWords) + "\n"
fp.write(tempStr)

fp.close()