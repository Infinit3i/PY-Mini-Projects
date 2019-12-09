from tkinter import *

window = Tk()
window.title("My Computer Science Glossary")

robot = PhotoImage(file="robot.gif")
Label (window, image=robot, bg="black") .grid(row=0, column=0, sticky=E)

window.mainloop()