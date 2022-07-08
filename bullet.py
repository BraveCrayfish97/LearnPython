from tkinter import *
import time
tk = Tk()
canvas = Canvas(tk, width = 600, height = 600)
canvas.pack()
bullet = canvas.create_oval(90, 90, 120, 120)
i = 0
while(i < 20):
    canvas.move(bullet, 5, 0)
    i = i + 1
    tk.update()
    time.sleep(0.1)
    tk.update()

tk.mainloop()