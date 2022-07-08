import random 
correct_num = random.randint(1, 100)
print("The goal of this game is to guess the number that is between 1-100 in less than 7 guesses.")
print("If your guess is within 25 of the number, I will say Warm.")
print("If your guess is within 10 of the number, I will say Hot.")
print("If your guess is within 5 of the number, I will say BOILING OIL!")
print("If your guess more than 25 away from the number, I will say Cool.")
print("If your guess more than 50 away from the number, I will say Cold.")
print("If your guess more than 75 away from the number, I will say SUPER COLD.")
print("\nI will also tell you if the number is greater than or less than your number.")
num_of_guesses = 1
game_running = True



while(game_running):
    bad_input = True
    while(bad_input):
        try:
            user_guess = int(input("What number do you want to guess?"))
            bad_input = False
        except ValueError:
            print("botty boi")
            bad_input = True

    if correct_num < user_guess:
        print("The correct number is LESS than your guess")
    if correct_num > user_guess:
        print("The correct number is GREATER than your guess")
    if correct_num == user_guess:
        game_running = False
        print("You have guessed the number!")
        break
    if abs(correct_num - user_guess) <= 25 and abs(correct_num - user_guess) > 10 and abs(correct_num - user_guess) > 5:
        print("Warm.")
    if abs(correct_num - user_guess) <= 10 and abs(correct_num - user_guess) > 5:
        print("Hot!")
    if abs(correct_num - user_guess) <= 5:
        print("BOILING OIL!")
    
    if abs(correct_num - user_guess) > 25 and abs(correct_num - user_guess) <= 50 and abs(correct_num - user_guess) <= 75:
        print("Cool.")
    if abs(correct_num - user_guess) > 50 and abs(correct_num - user_guess) <= 75:
        print("Cold!")
    if abs(correct_num - user_guess) > 75:
        print("SUPER COLD!")
    num_of_guesses = num_of_guesses + 1

if num_of_guesses == 1:
    print(f"You took ONLY {num_of_guesses} GUESS!???! YOU ARE AN ACTUAL HACKER. ")
if num_of_guesses > 1 and num_of_guesses <= 3:
    print(f"You took ONLY {num_of_guesses} GUESSES!?!? YOU ARE AN ABSOLUTE GOD. ")
if num_of_guesses > 3 and num_of_guesses <= 5:
    print(f"Good Job! You took {num_of_guesses} guesses. Your pretty good at this.")
if num_of_guesses > 5 and num_of_guesses <= 7:
    print(f"You took {num_of_guesses} guesses. Your average at this game.")
if num_of_guesses > 7:
    print(f"You took {num_of_guesses} guesses. YoU ARe AN ActuAl BBBBBOOOOOOOTTTTTTTTTTT at life.")

        