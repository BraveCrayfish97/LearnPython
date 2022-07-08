from tkinter import *
import random
import time

tk = Tk()

canvas_width = 1000
canvas_height = 800
canvas = Canvas(tk, width = canvas_width, height = canvas_height)
canvas.pack()

speeds = [-1 , -1.2, -1.3, -1.5, -1.7, -2, -2.1, -2.3, -2.5, -2.8, -3, -3.2, -3.5, -3.7, -4,1.2, 1.3, 1.5, 1.7, 2, 2.1, 2.3,2.5, 2.8, 3, 3.2, 3.5, 3.7, 4]
colors = ["red", "purple","blue", "yellow", "cyan", "lawn green", "orange", "maroon2", "navy blue"]
sizes = [350, 370, 380, 390, 400, 410, 420, 430]


class Ball():
    def __init__(self):
        self.xspeed = random.choice(speeds)
        self.yspeed = random.choice(speeds)
        self.size = random.choice(sizes)
        self.shape = canvas.create_oval(300, 300, self.size, self.size, fill = random.choice(colors))
    
    def move(self):
        canvas.move(self.shape, self.xspeed, self.yspeed)
        pos = canvas.coords(self.shape)
        if pos[3] >= canvas_height or pos[1]<= 0:
            self.yspeed = -self.yspeed
        if pos[2] >= canvas_width or pos[0] <= 0:
            self.xspeed = -self.xspeed


ball_lst = []
for i in range(100):
    ball_lst.append(Ball())

while(True):
    for ball in ball_lst:
        ball.move()
    tk.update()
    time.sleep(0.01)
    tk.update()

tk.mainloop()
