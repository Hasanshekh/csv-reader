######################CSV_Reader##########################
import os
import tkinter as tk
from tkinter import filedialog as fd 
from tkinter import *
import pandas as pd

class import_csv_data():
    def __init__(self):
        print('yes')
        global v
        csv_file_path = askopenfilename()
        print(csv_file_path)
        v.set(csv_file_path)
        Dataset= pd.read_csv(csv_file_path)
        print(Dataset.head)

root = Tk()
root.configure(background='white')

# Heading
root.title("by- Paritosh Verma")
w2 = Label(root, justify=LEFT, text="CSV Reader", fg="white", bg="blue")
w2.config(font=("Elephant", 10))
w2.grid(row=1, column=0, columnspan=2, padx=100)
"""w2 = Label(root, justify=LEFT, text=" ", fg="white", bg="blue")
w2.config(font=("Aharoni", 10))
w2.grid(row=2, column=0, columnspan=2, padx=100)"""

#tk.mainloop()
bt=Button(root, text='Browse Data Set',command=import_csv_data,bg="green",fg="yellow")
bt.grid(row=4,column=0,padx=100)
ct=Button(root, text='Close',command=root.destroy,bg="green",fg="yellow")
ct.grid(row=6,column=0,padx=100)

tk.mainloop()   
.
