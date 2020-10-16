import tkinter as tk
from tkinter import messagebox

def startCalc():
    if v.get() == 1:
        unit = " kg"
    elif v.get() == 2:
        unit = " lbs"
    else:
        unit = ""
    messagebox.showinfo("Result", "Your weight is "+entry.get()+unit+"!")

window = tk.Tk()
window.title("Weight Calculator Tool")
window.resizable(False,False)

fr_top = tk.Frame(window)
fr_top.grid(row=0, column=0, pady=5)

fr_bot = tk.Frame(window)
fr_bot.grid(row=1, column=0, sticky="e", pady=(0,5))

label = tk.Label(master=fr_top, text="Input your weight: ")
label.grid(row=0, column=0, padx=(5,0))

entry = tk.Entry(master=fr_top, width=10)
entry.grid(row=0, column=1, padx=(0,5))

v = tk.IntVar()

rButton1 = tk.Radiobutton(master=fr_top, text="kg", variable=v, value="1")
rButton1.grid(row=0, column=2)

rButton2 = tk.Radiobutton(master=fr_top, text="lbs", variable=v, value="2")
rButton2.grid(row=0, column=3)

startButton = tk.Button(master=fr_bot, text="Start", width=10, command=startCalc)
startButton.pack(padx=(0,5))

window.mainloop()