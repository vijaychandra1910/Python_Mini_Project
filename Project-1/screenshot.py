# install virtualenv for installing packages in a virtual environment
# Package pyautogui - Used for screenshots
import time
import pyautogui as ss
import tkinter as tk #Tkinter is a standard GUI library for Python

#Define a function to take a screenshot
def screenshot():
    name = int(round(time.time()*1000))
    name = 'D:/Python_Pro/Project-1/screenshortdata/{}.png'.format(name)
    img = ss.screenshot(name)
    img.show()

root = tk.Tk() #parent or root window
frame = tk.Frame(root) #children of the root window
frame.pack()
button = tk.Button(
    frame,
    text = "Take Screenshot",
    command = screenshot
)
button.pack(side=tk.LEFT)
close = tk.Button(
    frame,
    text = "Quit",
    command = quit
)
close.pack(side=tk.LEFT)
root.mainloop()
 