from tkinter import *
import tkinter.messagebox
import random
import time
tk = Tk()

class StickMan():
    def __init__(self, x, y, x1_n, y1_n ,x2_n, y2_n, ll_x2, ll_y2, rl_x, rl_y, la_x, la_y, la_x2, la_y2):
        self.head = canvas.create_oval(x - 30, y - 30, x + 30, y + 30, fill = "black")
        self.neck = canvas.create_line(x1_n, y1_n,x2_n, y2_n, width = 7)
        self.left_leg = canvas.create_line(x2_n, y2_n - 2, ll_x2, ll_y2, width = 7)
        self.right_leg = canvas.create_line(x2_n, y2_n, rl_x, rl_y, width = 7)
        self.left_arm = canvas.create_line(la_x, la_y, la_x2, la_y2, width = 6)

    def shoot(self, bullet_x, bullet_y):
        self.bullet = canvas.create_oval(bullet_x - 10, bullet_y - 10, bullet_x + 10, bullet_y + 10, fill = "black")
        i = 0
        #while(i < 20):
         #   canvas.move(self.bullet, 5, 0)
          #  i = i + 1
           # tk.update()
            #time.sleep(0.1)

screen_width = tk.winfo_screenwidth()
screen_height = tk.winfo_screenheight()

canvas_width = screen_width/1.5
canvas_height = screen_height/1.5

tk.maxsize(width = int(canvas_width), height = int(canvas_height))
tk.minsize(width = int(canvas_width), height = int(canvas_height))

canvas = Canvas(tk, width = canvas_width, height = canvas_height)
canvas.pack()


player = StickMan(canvas_width/7, canvas_height/1.6, canvas_width/7, canvas_height/1.55, canvas_width/7, canvas_height/1.27, canvas_width/15, canvas_height, canvas_width/4.7, canvas_height, canvas_width/7, canvas_height/1.37, canvas_width/12, canvas_height/1.45)
player.shoot(canvas_width/4.7, canvas_height/1.45)
#computer = StickMan(canvas_width/1.15, canvas_height/1.6)
war_label = Label(tk, text = "STICKMAN FIGHT", font = "Verdana 40 bold", fg = "red")
war_label.pack()
###############

shoot_input = "shoot"
shoot_btn = Button(tk, text = "Shoot", width = 7,border = 1, command = lambda:game(shoot_input), fg = "black")
shoot_btn.pack()
shoot_btn.place(x = canvas_width/5, y = canvas_height/1.5)


ammo_input = "ammo"
ammo_btn = Button(tk, text = "Ammo", border = 1, command = lambda:game(ammo_input),fg = "black")
ammo_btn.pack()
ammo_btn.place(x = canvas_width/8, y = canvas_height/1.5)


shield_input = "shield"
shield_btn = Button(tk, text = "Shield", border = 1, command = lambda:game(shield_input),fg = "black")
shield_btn.pack()
shield_btn.place(x = canvas_width/3.5, y = canvas_height/1.5)

story_label = Label(tk, text = "", font = "Verdana 15 bold")
story_label.pack()
#story_label.place(x = canvas_width/3.5, y = canvas_height/3)

def Computer_Wins():
    user_win_lbl = Label(tk, text = "You Lost! :(", font = "Verdana 70 bold", fg = "red3")
    user_win_lbl.pack()
    user_win_lbl.place(x = canvas_width/4.8, y = canvas_height/3)

    story_label.config(text = " ")

    ammo_btn.destroy()
    shoot_btn.destroy()
    shield_btn.destroy()

def User_Wins():
    comp_win_lbl = Label(tk, text = "You Won! :)", font = "Verdana 70 bold", fg = "blue2")
    comp_win_lbl.pack()
    comp_win_lbl.place(x = canvas_width/4.8, y = canvas_height/1.8)

    story_label.config(text = " ")

    ammo_btn.destroy()
    shoot_btn.destroy()
    shield_btn.destroy()

def Tie():
    print("You tied.")

comp_ammo = 0
user_ammo = 0
comp_living = True
user_livng = True
game_running = True
aggressive_choices = ["ammo", "shoot", "shield", "shield", "shoot", "shoot"]
no_ammo_choices = ["ammo", "shield"]

user_ammo_lbl = Label(tk, text = "Bullets: 0", font = "Verdana 20 bold")
user_ammo_lbl.pack()
user_ammo_lbl.place(x = 0, y = canvas_height/9)

#print("This game is called War. Every turn you can either get one more bullet by typing Ammo, shoot your opponent by typing Shoot, or use your shield by typing Shield")

def game(user_choice):
    global user_ammo_lbl
    global comp_ammo
    global user_ammo
    global game_running
    global aggressive_choices
    global no_ammo_choices
    global user_livng
    global comp_living

    
    if comp_ammo > 0:
        comp_choice = random.choice(aggressive_choices)
        
    if comp_ammo == 0:
        comp_choice = random.choice(no_ammo_choices)
    print(comp_choice)
    print(user_choice)

    if user_ammo == 0 and user_choice.lower() == "shoot":
        story_label.config(text = "You have no ammo, so you cannot shoot. Choose an action other than Shoot.")
        
    
    else:
        game_logic(comp_choice, user_choice)




def game_logic(comp_choice, user_choice):
    
    global comp_ammo
    global user_ammo
    global game_running
    global aggressive_choices
    global no_ammo_choices
    global user_livng
    global comp_living

    if comp_choice.lower() == "ammo" and user_choice.lower() == "ammo":
        comp_ammo = comp_ammo + 1
        user_ammo = user_ammo + 1
        story_label.config(text = "You both chose to get ammo.")
        
    elif comp_choice.lower() == "ammo" and user_choice.lower() == "shield":
        
        comp_ammo = comp_ammo + 1
        story_label.config(text = "They chose to get ammo. You shielded, but it didn't do anything.")

    elif comp_choice.lower() == "ammo" and user_choice.lower() == "shoot":
        
        comp_ammo = comp_ammo + 1
        story_label.config(text = "You shot them while they were getting ammo, so they died")
        User_Wins()
        
    elif comp_choice.lower() == "shoot" and user_choice.lower() == "ammo":
        story_label.config(text = "They shot you while you were getting more ammo, so you died.")
        comp_ammo = comp_ammo - 1
        Computer_Wins()


    elif comp_choice.lower() == "shoot" and user_choice.lower() == "shield":
        comp_ammo = comp_ammo - 1
        story_label.config(text = "They shot at you, but your shield saved you. They have " + str(comp_ammo) + " bullets left.")

    elif comp_choice.lower() == "shoot" and user_choice.lower() == "shoot":
        print("They shot, and you shot, so you both died")
        Tie()
        

    elif comp_choice.lower() == "shield" and user_choice.lower() == "ammo":
        print("They shielded, but it was pointless becuase you got more ammo")
        user_ammo = user_ammo + 1
    elif comp_choice.lower() == "shield" and user_choice.lower() == "shield":
        print("You both sheilded, so nothing happened")

    elif comp_choice.lower() == "shield" and user_choice.lower() == "shoot":
        print("You shot, but they shielded, so they are still alive")
        user_ammo = user_ammo - 1
        print(f"You now have {user_ammo} bullets left")

        


    else:
        print("Please type a valid action")
        game_running = True
    user_ammo_lbl.config(text = "Bullets: " + str(user_ammo))
#canvas.pack()
tk.mainloop()