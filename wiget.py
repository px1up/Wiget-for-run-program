import psutil
from tkinter import *

programm =str("program.exe")

def message_window():
    window = Tk()
    window.title("")
    window.geometry('250x150')
    lbl = Label( width=30, height=10, text="message",font=("Arial Bold", 10))
    lbl.grid(column=0, row=0)
    window.mainloop()


num = 1
while num == 1:
    for process in psutil.process_iter():
        if process.name() == programm:
            num = 2
        else:
            num == 2
message_window()
