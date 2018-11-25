import tkinter as tk
from random import *
import datetime

now = datetime.datetime.now()
seed(now)

dares = ["Watch another video",
"Subscribe to the channel",
"Like this video",]

truths = ["Was this tutorial easy to follow?",
"Did you learn something new about Python?",
"Why aren't you subscribed to the channel?",]

def dare():
    dareoutput = choice(dares)
    print(dareoutput)

def truth():
    truthoutput = choice(truths)
    print(truthoutput)

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame,
                   text="Truth",
                   fg="red",
                   command=truth)
button.pack(side=tk.LEFT)
DareButton = tk.Button(frame,
                   text="Dare",
                   command=dare)
DareButton.pack(side=tk.LEFT)

root.mainloop()
