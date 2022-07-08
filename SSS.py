import random
nm_lst = [1,2,3,4,5,6,7,8,9,10]
print('This game is called "Sword, Shield, Save", or SSS.\nIn this game, you have a robot that has 10 health, and your enemy also has a robot with 10 health.\n')
def start():
    tie = True
    while(tie):
        right_ans = random.choice(nm_lst)
        comp_choice = random.choice(nm_lst)
        user_choice = int(input("Pick a number between 1 and 10. Whoever is closest, will go first\n > ")) 
        right_comp_diff = abs(right_ans - comp_choice)
        right_user_diff = abs(right_ans - user_choice)
        print(f"The number was {right_ans}.")
        print(f"The enemy chose {comp_choice}.")
        print(f"The enemy was {right_comp_diff} away from the right number.")
        print(f"And you were {right_user_diff} away from the right number.")
        if right_comp_diff > right_user_diff:
            print("So you go first")
            tie = False
        elif right_comp_diff < right_user_diff:
            print("So the enemy goes first.")
            tie = False
        else:
            tie = True

start()
#lst = ["Sword", "Shield", "Save"]
#comp_sss_choice = random.choice(lst)
#print(rndm)