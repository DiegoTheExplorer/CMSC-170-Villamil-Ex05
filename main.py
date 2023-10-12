#Remember to use the decimal datatype for precision
import Bow as bow

import tkinter as tk
from tkinter import filedialog
from functools import partial

def getFile(file):
  path = filedialog.askdirectory()
  file.set(path)
  print(file.get())

#Start of app
root = tk.Tk()
root.geometry("500x500")
root.title('Spam Ham')

file = tk.StringVar()
fileSelect = tk.Button(root, text="Select Dir", command=partial(getFile, file))
fileSelect.grid(row = 0, column = 0, sticky = 'nesw')

root.mainloop()

