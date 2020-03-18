import psutil
from tkinter import *

def window():
    window = Tk()
    window.title("")
    window.mainloop()

num = 1
while num == 1:
    for process in psutil.process_iter():
        if process.name() == 'notepad.exe':
            window()
if window():
    exit(0)
