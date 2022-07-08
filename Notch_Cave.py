def start():
    botguy = True
    print("\nYou, also known as Steve, are going to fight the evil Enderdragon in 2 days. \nYou have your godly bow, your potions, and your godly sword ready for action, but you only have iron armor. \nSo you decide to go to the Notch Cave. The Notch Cave is the most dangerous, yet rewarding, cave in all of Minecraft. \nMany have entered, but only a few have returned from this mysterious cave.")
    while(botguy):
        lft_or_rght = input("\nYou have entered the Notch Cave with only your pickaxe and botty bow, and the cave branches off into 2 directions: Left and Right. \nWhich direction would you like to go? ")
        
        if lft_or_rght.lower() == "right":

            botguy = False 
            parkour()
        elif lft_or_rght.lower() == "left":
            botguy = False
            Fall_Into_Water()
        else:
            print('\nPlease enter "Right" or "Left", nothing else.')
            botguy = True

def parkour():
    badinput = True
    print("-----------------------------")
    print('\nAs you venture further into this part of the cave, you find a big open room and a sign that says, \n"This is a dangerous parkour challenge to see if you are worthy enough to claim the reward at the top. \nNext to this sign, there are 2 chests, but you can only take the items from one of them.\n\nWARNING! Noobs are not advised to attempt this precarious challenge" ')
    print("\nThe first chest has 2 diamonds, while the second chest has a potion of jump boost.")
    while(badinput):
        dimds_or_jmpbst = input("\nDo you want to take the 2 extra diamonds which contributes to your goal of getting full diamond armor?\nOr do you want the potion of jump boost which could help in the parkour? \nType Diamonds or Jump Boost\n>")
    
        if dimds_or_jmpbst.lower() == "jump boost":
            badinput = False
            print("\nAfter a lot of fence post, slime block, and cactus parkour, you have finally made it to the last jump. The last jump is ,by far, the hardest jump in the entire parkour challenge. It is a 4 block jump onto an ice block. After some thinking, you decided to use your jump boost potion causing you to make the jump easily.\nYou thanked yourself for taking the jump boost potion and looked in the reward chest and found 5 DIAMONDS.")
        elif dimds_or_jmpbst.lower() == "diamonds":
            badinput = False
            print("\nAfter a lot of fence post, slime block, and cactus parkour, you have finally made it to the last jump. The last jump is ,by far, the hardest jump in the entire parkour challenge. It is a 4 block jump onto an ice block. After a lot of thinking, you decide that you will jump. 3, 2, 1 ... LEAP! You timed the jump perfectly and made it! You celebrated your accomplishment in joy! Until you realized ... that you were standing on ice. You slipped off the ice, and not long after ...\n\nSteve fell from a high place\n\nYOU DIED!")
            nubanswer = True
            while(nubanswer):
                again = input("Would you like to play again?")
                if again.lower() == "yes":
                    start()
                    nubanswer = False
                elif again.lower() == "no":
                    print("Because of this failed mission, you will not be able to have diamond armor when fighting the Ender Dragon which will make the fight all the more difficult\n\nThanks for Playing!")
                    nubanswer = False
                else:
                    print("Please enter Yes or No, nothing else.")
                    nubanswer = True
        else:
            badinput = True
            print('\nPlease enter "Diamonds" or "Jump Boost" nothing else.')

def Fall_Into_Water():
    badanswer = True
    print("-----------------------------")
    print("\nAs you walk down this section of the cave, you hear the sound of dripping water getting louder and louder.\nAnd right as you consider going back, you plumet 20 blocks into an underground lake.\nYou see a small island that you could swim to, but the island is full of witches and skeletons.\nYou also see an airpocket down below, but there are a bunch of creepers sitting on the bed of the lake.")
    while(badanswer):
        shre_or_airpckt = input("\nDo you want to swim down to the airpocket?\nOr do you want to swim to shore?\nType Airpocket or Shore.\n> ")
        if shre_or_airpckt.lower() == "airpocket":
            badanswer = False
            print("-----------------------------")
            print("\nAs you start swimming towards the airpocket, you see a creeper swmming towards you from the right, so you start swimming left. But then you see another creeper only 10 blocks in front of you, and then you realize that you are surrounded by almost 20 creepers. You feel like all hope is lost, so you curl up into a ball on the bottom of the lake and await your explosive death. You then hear an ear-piercing BOOM, and open your eyes expecting to be laying in bed at home base. But instead, you are still at the bottom of the lake about to drown. You then frantically swim to the airpocket and take a deep breathe. You wonder why the creepers' explosion didn't kill you, but then it hit you. Explosions of any kind don't do damage while in water.")
        elif shre_or_airpckt.lower() == "shore":
            badanswer = False
            print("You're swimming to shore now")
            uncmptblinpt = True
            print("-----------------------------")
            while(uncmptblinpt):
                play_again = input("Would you like to play again and redeem yourself? ")
                if play_again.lower() == "yes":
                    uncmptblinpt = False
                    start()
                if play_again.lower() == "no":
                    uncmptblinpt = False
                    print("Ok. Thanks for Playing! :)")
        else:
            badanswer = True

start()
