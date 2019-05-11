from tkinter import *
import pandas as pd

def submit_fields():
    path = 'excel.xlsx'
    df1 = pd.read_excel(path)
    SeriesA = df1['Operator']
    SeriesB = df1['Number']
    A = pd.Series(entry1.get())
    B = pd.Series(entry2.get())
    SeriesA = SeriesA.append(A)
    SeriesB = SeriesB.append(B)
    df2 = pd.DataFrame({"Operator":SeriesA, "Number":SeriesB})
    df2.to_excel(path, index=False)
    entry1.delete(0, END)
    entry2.delete(0, END)

master = Tk()

Label(master, text="Operator").grid(row=0)
Label(master, text="Number").grid(row=1)

entry1 = Entry(master)
entry2 = Entry(master)

entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)

Button(master, text='Quit', command=master.quit).grid(row=3,column=0, pady=4)
Button(master, text='Submit', command=submit_fields).grid(row=3,column=1, pady=4)

mainloop()
