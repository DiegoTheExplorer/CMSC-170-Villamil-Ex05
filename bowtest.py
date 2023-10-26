import Bow as bow

file = "data/data01/classify/0013.1999-12-14.kaminski.ham.txt"

bag = bow.Bow(file)
print("Dictionary Size: " + str(bag.dictSize))
print("Total Number of Words: " + str(bag.totalWords))
for key in bag.dict:
  print(key)