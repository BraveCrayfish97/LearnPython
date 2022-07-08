from tkinter import *
import tkinter.messagebox
tk = Tk()


tk.title("Dots and Boxes")

screen_height = tk.winfo_screenheight()
screen_width = screen_height

circle_radius = 45

tk.maxsize(width = screen_width, height = screen_height )


player = True

box1_status = True
box2_status = True
box3_status = True
box4_status = True
box5_status = True
box6_status = True
box7_status = True
box8_status = True
box9_status = True

red_score = 0
blue_score = 0

game_over = Label(tk, text = "GAME OVER", font = "Arial 45 bold", fg = "orange")

label_1 = Label(tk, text = "B", fg = "blue", font = "Arial 70 bold")
label_2 = Label(tk, text = "B", fg = "blue", font = "Arial 70 bold")
label_3 = Label(tk, text = "B", fg = "blue", font = "Arial 70 bold")
label_4 = Label(tk, text = "B", fg = "blue", font = "Arial 70 bold")
label_5 = Label(tk, text = "B", fg = "blue", font = "Arial 70 bold")
label_6 = Label(tk, text = "B", fg = "blue", font = "Arial 70 bold")
label_7 = Label(tk, text = "B", fg = "blue", font = "Arial 70 bold")
label_8 = Label(tk, text = "B", fg = "blue", font = "Arial 70 bold")
label_72 = Label(tk, text = "B", fg = "blue", font = "Arial 70 bold")
label_82 = Label(tk, text = "B", fg = "blue", font = "Arial 70 bold")
label_9 = Label(tk, text = "B", fg = "blue", font = "Arial 70 bold")
label_10 = Label(tk, text = "B", fg = "blue", font = "Arial 70 bold")
label_11 = Label(tk, text = "B", fg = "blue", font = "Arial 70 bold")
label_12 = Label(tk, text = "B", fg = "blue", font = "Arial 70 bold")
label_13 = Label(tk, text = "B", fg = "blue", font = "Arial 70 bold")
label_14 = Label(tk, text = "B", fg = "blue", font = "Arial 70 bold")
label_15 = Label(tk, text = "B", fg = "blue", font = "Arial 70 bold")
label_16 = Label(tk, text = "B", fg = "blue", font = "Arial 70 bold")

def make_line(buttons):
    global label_1
    global label_2
    global label_3
    global label_4
    global label_5
    global label_6
    global label_7
    global label_8
    global label_72
    global label_82
    global label_9
    global label_10
    global label_11
    global label_12
    global label_13
    global label_14
    global label_15
    global label_16

    global red_score
    global blue_score
    global screen_width
    global screen_height
    global player
    global box1_status
    global box2_status
    global box3_status
    global box4_status
    global box5_status
    global box6_status
    global box7_status
    global box8_status
    global box9_status

    

    if player == True:
        buttons.config(state = DISABLED, bg = "red")
        player = False
        
        

    elif player == False:
        buttons.config(state = DISABLED, bg = "blue")
        player = True
    
    if button1["bg"] != "lightgrey" and button4["bg"] != "lightgrey" and button5["bg"] != "lightgrey" and button8["bg"] != "lightgrey" and box1_status == True:
        box1_winner = buttons["bg"]
        box1_status = False

        if box1_winner == "blue":
            player = False
            label_1 = Label(tk, text = "B", fg = "blue", font = "Arial 70 bold")
            label_1.pack()
            label_1.place(x = screen_width/4.4, y = screen_height/4.4)
            blue_score = blue_score + 1

        if box1_winner == "red":
            player = True
            label_2 = Label(tk, text = "R", fg = "red", font = "Arial 70 bold")
            label_2.pack()
            label_2.place(x = screen_width/4.4, y = screen_height/4.4)
            red_score = red_score + 1

    if button2["bg"] != "lightgrey" and button5["bg"] != "lightgrey" and button6["bg"] != "lightgrey" and button9["bg"] != "lightgrey" and box2_status == True:
        box2_winner = buttons["bg"]
        box2_status = False

        if box2_winner == "blue":

            player = False
            label_3 = Label(tk, text = "B", fg = "blue", font = "Arial 70 bold")
            label_3.pack()
            label_3.place(x = screen_width/2.07, y = screen_height/4.4)
            blue_score = blue_score + 1

        if box2_winner == "red":

            player = True
            label_4 = Label(tk, text = "R", fg = "red", font = "Arial 70 bold")
            label_4.pack()
            label_4.place(x = screen_width/2.07, y = screen_height/4.4)
            red_score = red_score + 1

    if button3["bg"] != "lightgrey" and button6["bg"] != "lightgrey" and button7["bg"] != "lightgrey" and button10["bg"] != "lightgrey" and box3_status == True:
        box3_winner = buttons["bg"]
        box3_status = False

        if box3_winner == "blue":
            player = False 

            label_5 = Label(tk, text = "B", fg = "blue", font = "Arial 70 bold")
            label_5.pack()
            label_5.place(x = screen_width/1.36, y = screen_height/4.4)
            blue_score = blue_score + 1

        if box3_winner == "red":
            player = True

            label_6 = Label(tk, text = "R", fg = "red", font = "Arial 70 bold")
            label_6.pack()
            label_6.place(x = screen_width/1.36, y = screen_height/4.4)
            red_score = red_score + 1
    if button8["bg"] != "lightgrey" and button11["bg"] != "lightgrey" and button12["bg"] != "lightgrey" and button15["bg"] != "lightgrey" and box4_status == True:
        box4_winner = buttons["bg"]
        box4_status = False

        if box4_winner == "blue":
            player = False

            label_72 = Label(tk, text = "B", fg = "blue", font = "Arial 70 bold")
            label_72.pack()
            label_72.place(x = screen_width/4.4, y = screen_height/2.07)
            blue_score = blue_score + 1
        if box4_winner == "red":
            player = True
            
            label_82 = Label(tk, text = "R", fg = "red", font = "Arial 70 bold")
            label_82.pack()
            label_82.place(x = screen_width/4.4, y = screen_height/2.07)
            red_score = red_score + 1

    if button9["bg"] != "lightgrey" and button12["bg"] != "lightgrey" and button13["bg"] != "lightgrey" and button16["bg"] != "lightgrey" and box5_status == True:
        box5_winner = buttons["bg"]
        box5_status = False

        if box5_winner == "blue":
            player = False

            label_7 = Label(tk, text = "B", fg = "blue", font = "Arial 70 bold")
            label_7.pack()
            label_7.place(x = screen_width/2.07, y = screen_height/2.07)
            blue_score = blue_score + 1
        if box5_winner == "red":
            player = True
            
            label_8 = Label(tk, text = "R", fg = "red", font = "Arial 70 bold")
            label_8.pack()
            label_8.place(x = screen_width/2.07, y = screen_height/2.07)
            red_score = red_score + 1
    
    if button10["bg"] != "lightgrey" and button13["bg"] != "lightgrey" and button14["bg"] != "lightgrey" and button17["bg"] != "lightgrey" and box6_status == True:
        box6_winner = buttons["bg"]
        box6_status = False

        if box6_winner == "blue":
            player = False

            label_9 = Label(tk, text = "B", fg = "blue", font = "Arial 70 bold")
            label_9.pack()
            label_9.place(x = screen_width/1.36, y = screen_height/2.07)
            blue_score = blue_score + 1
        if box6_winner == "red":
            player = True
            
            label_10 = Label(tk, text = "R", fg = "red", font = "Arial 70 bold")
            label_10.pack()
            label_10.place(x = screen_width/1.36, y = screen_height/2.07)
            red_score = red_score + 1

    if button15["bg"] != "lightgrey" and button18["bg"] != "lightgrey" and button19["bg"] != "lightgrey" and button22["bg"] != "lightgrey" and box7_status == True:
        box7_winner = buttons["bg"]
        box7_status = False

        if box7_winner == "blue":
            player = False

            label_11 = Label(tk, text = "B", fg = "blue", font = "Arial 70 bold")
            label_11.pack()
            label_11.place(x = screen_width/4.4, y = screen_height/1.36)
            blue_score = blue_score + 1
        if box7_winner == "red":
            player = True
            
            label_12 = Label(tk, text = "R", fg = "red", font = "Arial 70 bold")
            label_12.pack()
            label_12.place(x = screen_width/4.4, y = screen_height/1.36)
            red_score = red_score + 1
    
    if button16["bg"] != "lightgrey" and button19["bg"] != "lightgrey" and button20["bg"] != "lightgrey" and button23["bg"] != "lightgrey" and box8_status == True:
        box8_winner = buttons["bg"]
        box8_status = False

        if box8_winner == "blue":
            player = False

            label_13 = Label(tk, text = "B", fg = "blue", font = "Arial 70 bold")
            label_13.pack()
            label_13.place(x = screen_width/2.07, y = screen_height/1.36)
            blue_score = blue_score + 1
        if box8_winner == "red":
            player = True
            
            label_14 = Label(tk, text = "R", fg = "red", font = "Arial 70 bold")
            label_14.pack()
            label_14.place(x = screen_width/2.07, y = screen_height/1.36)
            red_score = red_score + 1
    
    if button17["bg"] != "lightgrey" and button20["bg"] != "lightgrey" and button21["bg"] != "lightgrey" and button24["bg"] != "lightgrey" and box9_status == True:
        box9_winner = buttons["bg"]
        box9_status = False

        if box9_winner == "blue":
            player = False

            label_15 = Label(tk, text = "B", fg = "blue", font = "Arial 70 bold")
            label_15.pack()
            label_15.place(x = screen_width/1.36, y = screen_height/1.36)
            blue_score = blue_score + 1
        if box9_winner == "red":
            player = True
            
            label_16 = Label(tk, text = "R", fg = "red", font = "Arial 70 bold")
            label_16.pack()
            label_16.place(x = screen_width/1.36, y = screen_height/1.36)
            red_score = red_score + 1


    if red_score + blue_score == 9:

        game_over.pack()
        game_over.place(x = screen_width/3, y = 0)
        if red_score > blue_score:
            
            game_over.pack()
            game_over.place(x = screen_width/3, y = 0)
            
            tkinter.messagebox.showinfo("Red Wins","Red is GODDLIEST Dots and Boxes player EVER!" )
        if red_score < blue_score:
            tkinter.messagebox.showinfo("Blue Wins","Blue is GODDLIEST Dots and Boxes player EVER!" )

        tkinter.messagebox.showinfo(" ", "Let's play again")
        tkinter.messagebox.showinfo(" ",  "Hover over the buttons to make them appear.")
        reset()

    blue_score_board.config(text = "Blue: " + str(blue_score))
    red_score_board.config(text = "Red: " + str(red_score))
    

def reset():

    global label_1
    global label_2
    global label_3
    global label_4
    global label_5
    global label_6
    global label_7
    global label_8
    global label_72
    global label_82
    global label_9
    global label_10
    global label_11
    global label_12
    global label_13
    global label_14
    global label_15
    global label_16

    global red_score
    global blue_score
    global game_over

    for button in button_list:
        button.config(state = ACTIVE, bg = "lightgrey")
    
    label_1.destroy()
    label_2.destroy()
    label_3.destroy()
    label_4.destroy()
    label_5.destroy()
    label_6.destroy()
    label_7.destroy()
    label_8.destroy()
    label_72.destroy()
    label_82.destroy()
    label_9.destroy()
    label_10.destroy()
    label_11.destroy()
    label_12.destroy()
    label_13.destroy()
    label_14.destroy()
    label_15.destroy()
    label_16.destroy()

    red_score = 0
    blue_score = 0
    game_over.destroy()
        

canvas = Canvas(tk, width = screen_height, height = screen_height)


blue_score_board = Label(tk, text = "Blue: " + str(blue_score), font = "Arial 35 bold", fg = "blue")
blue_score_board.pack()
blue_score_board.place(x = screen_width/20, y = screen_height/40)

red_score_board = Label(tk, text = "Red: " + str(blue_score), font = "Arial 35 bold", fg = "red")
red_score_board.pack()
red_score_board.place(x = screen_width/1.3, y = screen_height/40)

circle1 = canvas.create_oval(screen_width/8 - circle_radius, screen_height/8 - circle_radius, screen_width/8 + circle_radius, screen_height/8 + circle_radius, fill = "black")
circle2 = canvas.create_oval(screen_width/2.60 - circle_radius, screen_height/8 - circle_radius, screen_width/2.60 + circle_radius, screen_height/8 + circle_radius, fill = "black")
circle3 = canvas.create_oval(screen_width/1.553 - circle_radius, screen_height/8 - circle_radius, screen_width/1.553 + circle_radius, screen_height/8 + circle_radius, fill = "black")
circle4 = canvas.create_oval(screen_width/1.108 - circle_radius, screen_height/8 - circle_radius, screen_width/1.108 + circle_radius, screen_height/8 + circle_radius, fill = "black")
circle5 = canvas.create_oval(screen_width/8 - circle_radius, screen_height/2.59 - circle_radius, screen_width/8 + circle_radius, screen_height/2.59 + circle_radius, fill = "black")
circle6 = canvas.create_oval(screen_width/2.60 - circle_radius, screen_height/2.59 - circle_radius, screen_width/2.60 + circle_radius, screen_height/2.59 + circle_radius, fill = "black")
circle7 = canvas.create_oval(screen_width/1.553 - circle_radius, screen_height/2.59 - circle_radius, screen_width/1.553 + circle_radius, screen_height/2.59 + circle_radius, fill = "black")
circle8 = canvas.create_oval(screen_width/1.108 - circle_radius, screen_height/2.59 - circle_radius, screen_width/1.108 + circle_radius, screen_height/2.59 + circle_radius, fill = "black")
circle9 = canvas.create_oval(screen_width/8 - circle_radius, screen_height/1.545 - circle_radius, screen_width/8 + circle_radius, screen_height/1.545 + circle_radius, fill = "black")
circle10 = canvas.create_oval(screen_width/2.60 - circle_radius, screen_height/1.545 - circle_radius, screen_width/2.60 + circle_radius, screen_height/1.545 + circle_radius, fill = "black")
circle11 = canvas.create_oval(screen_width/1.553 - circle_radius, screen_height/1.545 - circle_radius, screen_width/1.553 + circle_radius, screen_height/1.545 + circle_radius, fill = "black")
circle12 = canvas.create_oval(screen_width/1.108 - circle_radius, screen_height/1.545 - circle_radius, screen_width/1.108 + circle_radius, screen_height/1.545 + circle_radius, fill = "black")
circle13 = canvas.create_oval(screen_width/8 - circle_radius, screen_height/1.101 - circle_radius, screen_width/8 + circle_radius, screen_height/1.101 + circle_radius, fill = "black")
circle14 = canvas.create_oval(screen_width/2.60 - circle_radius, screen_height/1.101 - circle_radius, screen_width/2.60 + circle_radius, screen_height/1.101 + circle_radius, fill = "black")
circle15 = canvas.create_oval(screen_width/1.553 - circle_radius, screen_height/1.101 - circle_radius, screen_width/1.553 + circle_radius, screen_height/1.101 + circle_radius, fill = "black")
circle16 = canvas.create_oval(screen_width/1.108 - circle_radius, screen_height/1.101 - circle_radius, screen_width/1.108 + circle_radius, screen_height/1.101 + circle_radius, fill = "black")


button_list = []

button1_x = screen_width/6.17
button1_y = screen_height/8.8
button1 = Button(tk, text = " ", bg = "lightgrey", border = 0, width = 32, height = 1, command = lambda:make_line(button1))
button_list.append(button1)

button1.pack()
button1.place(x = button1_x, y = button1_y)


button2_x = screen_width/2.375
button2_y = screen_height/8.8
button2 = Button(tk, text = " ", bg = "lightgrey", border = 0, width = 32, height = 1,command = lambda:make_line(button2))
button_list.append(button2)

button2.pack()
button2.place(x = button2_x, y = button2_y)


button3_x = screen_width/1.472
button3_y = screen_height/8.8
button3 = Button(tk, text = " ", bg = "lightgrey", border = 0, width = 32, height = 1,command = lambda:make_line(button3))
button_list.append(button3)

button3.pack()
button3.place(x = button3_x, y = button3_y)


button4_x = screen_width/8.55
button4_y = screen_height/6.17
button4 = Button(tk, text = " ", bg = "lightgrey", border = 0, width = 2, height = 15,command = lambda:make_line(button4))
button_list.append(button4)

button4.pack()
button4.place(x = button4_x, y = button4_y)

button5_x = screen_width/2.655
button5_y = screen_height/6.17
button5 = Button(tk, text = " ", bg = "lightgrey", border = 0, width = 2, height = 15,command = lambda:make_line(button5))
button_list.append(button5)

button5.pack()
button5.place(x = button5_x, y = button5_y)


button6_x = screen_width/1.573
button6_y = screen_height/6.17
button6 = Button(tk, text = " ", bg = "lightgrey", border = 0, width = 2, height = 15,command = lambda:make_line(button6))
button_list.append(button6)

button6.pack()
button6.place(x = button6_x, y = button6_y)


button7_x = screen_width/1.118
button7_y = screen_height/6.17
button7 = Button(tk, text = " ", bg = "lightgrey", border = 0, width = 2, height = 15,command = lambda:make_line(button7))
button_list.append(button7)

button7.pack()
button7.place(x = button7_x, y = button7_y)


button8_x = screen_width/6.17
button8_y = screen_height/2.65
button8 = Button(tk, text = " ", bg = "lightgrey", border = 0, width = 32, height = 1,command = lambda:make_line(button8))
button_list.append(button8)

button8.pack()
button8.place(x = button8_x, y = button8_y)


button9_x = screen_width/2.375
button9_y = screen_height/2.65
button9 = Button(tk, text = " ", bg = "lightgrey", border = 0, width = 32, height = 1,command = lambda:make_line(button9))
button_list.append(button9)

button9.pack()
button9.place(x = button9_x, y = button9_y)



button10_x = screen_width/1.472
button10_y = screen_height/2.65
button10 = Button(tk, text = " ", bg = "lightgrey", border = 0, width = 32, height = 1,command = lambda:make_line(button10))
button_list.append(button10)

button10.pack()
button10.place(x = button10_x, y = button10_y)


button11_x = screen_width/8.5
button11_y = screen_height/2.365
button11 = Button(tk, text = " ", bg = "lightgrey", border = 0, width = 2, height = 15,command = lambda:make_line(button11))
button_list.append(button11)

button11.pack()
button11.place(x = button11_x, y = button11_y)


button12_x = screen_width/2.655
button12_y = screen_height/2.365
button12 = Button(tk, text = " ", bg = "lightgrey", border = 0, width = 2, height = 15,command = lambda:make_line(button12))
button_list.append(button12)

button12.pack()
button12.place(x = button12_x, y = button12_y)


button13_x = screen_width/1.573
button13_y = screen_height/2.365
button13 = Button(tk, text = " ", bg = "lightgrey", border = 0, width = 2, height = 15,command = lambda:make_line(button13))
button_list.append(button13)

button13.pack()
button13.place(x = button13_x, y = button13_y)


button14_x = screen_width/1.118
button14_y = screen_height/2.365
button14 = Button(tk, text = " ", bg = "lightgrey", border = 0, width = 2, height = 15,command = lambda:make_line(button14))
button_list.append(button14)

button14.pack()
button14.place(x = button14_x, y = button14_y)


button15_x = screen_width/6.17
button15_y = screen_height/1.565
button15 = Button(tk, text = " ", bg = "lightgrey", border = 0, width = 32, height = 1,command = lambda:make_line(button15))
button_list.append(button15)

button15.pack()
button15.place(x = button15_x, y = button15_y)


button16_x = screen_width/2.375
button16_y = screen_height/1.565
button16 = Button(tk, text = " ", bg = "lightgrey", border = 0, width = 32, height = 1,command = lambda:make_line(button16))
button_list.append(button16)

button16.pack()
button16.place(x = button16_x, y = button16_y)


button17_x = screen_width/1.472
button17_y = screen_height/1.565
button17 = Button(tk, text = " ", bg = "lightgrey", border = 0, width = 32, height = 1,command = lambda:make_line(button17))
button_list.append(button17)

button17.pack()
button17.place(x = button17_x, y = button17_y)


button18_x = screen_width/8.5
button18_y = screen_height/1.463
button18 = Button(tk, text = " ", bg = "lightgrey", border = 0, width = 2, height = 15,command = lambda:make_line(button18))
button_list.append(button18)

button18.pack()
button18.place(x = button18_x, y = button18_y)


button19_x = screen_width/2.655
button19_y = screen_height/1.463
button19 = Button(tk, text = " ", bg = "lightgrey", border = 0, width = 2, height = 15,command = lambda:make_line(button19))
button_list.append(button19)

button19.pack()
button19.place(x = button19_x, y = button19_y)


button20_x = screen_width/1.573
button20_y = screen_height/1.463
button20 = Button(tk, text = " ", bg = "lightgrey", border = 0, width = 2, height = 15,command = lambda:make_line(button20))
button_list.append(button20)

button20.pack()
button20.place(x = button20_x, y = button20_y)


button21_x = screen_width/1.118
button21_y = screen_height/1.463
button21 = Button(tk, text = " ", bg = "lightgrey", border = 0, width = 2, height = 15,command = lambda:make_line(button21))
button_list.append(button21)

button21.pack()
button21.place(x = button21_x, y = button21_y)


button22_x = screen_width/6.17
button22_y = screen_height/1.112
button22 = Button(tk, text = " ", bg = "lightgrey", border = 0, width = 32, height = 1,command = lambda:make_line(button22))
button_list.append(button22)

button22.pack()
button22.place(x = button22_x, y = button22_y)


button23_x = screen_width/2.375
button23_y = screen_height/1.112
button23 = Button(tk, text = " ", bg = "lightgrey", border = 0, width = 32, height = 1,command = lambda:make_line(button23))
button_list.append(button23)

button23.pack()
button23.place(x = button23_x, y = button23_y)


button24_x = screen_width/1.472
button24_y = screen_height/1.112
button24 = Button(tk, text = " ", bg = "lightgrey", border = 0, width = 32, height = 1,command = lambda:make_line(button24))
button_list.append(button24)

button24.pack()
button24.place(x = button24_x, y = button24_y)



canvas.pack()
tk.mainloop()