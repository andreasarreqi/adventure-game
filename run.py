# Importing time modules
import time


global axe
axe = "no"
global Flare
flare = "no"
global edible_fruit
edible_fruit = "no"


def game_introduction():
    """"
    Game intro
    """
    print()
    print("Quite an exciting day for you passes by.\n")
    print("You find yourself at the airport few minutes away from departing to your holiday destination.\n")
    time.sleep(2)
    print("Everything seems to be going well.\n")
    print("The flight seems to be quiet and very comfy.\n")
    time.sleep(2)
    print(".")
    print("Until..")
    print(".")
    print(".")
    print(".")
    print("One of the engines explodes...\n")
    time.sleep(2)
    print("After the pilot's struggle to keep the plane flying")
    print("And using the radio for help he fails.")
    print("Eventually the plane crashes in a deserted island\n")
    time.sleep(2)
    print("####       ###      ###     #       #  #")
    print("#    #    #   #    #   #    # #   # #  # ")
    print("### #     #   #    #   #    #   #   #  #")
    print("#    #    #   #    #   #    #       #    ")
    print("####       ###      ###     #       #  #")
    print(".")
    print(".")
    print(".")
    print("The plane has crashed!!!")
    


# The game start function
def game_start():
    """
    Setting up the game start function
    """
    print("After few hours of being unconcious, you wake up.")
    print("Confused and lost, you try to look around the cabin")
    print("You realise that you are the only one alive...")
    while True:
        find_the_way = input("Would you like to try to find a way " +
        "to leave the island? (yes/no):\n")
        if find_the_way == "no":
            print("\nWell, it was nice knowing you...")
            time.sleep(2)
            print("Enjoy a slow and painful death from dehydration...\n")
            time.sleep(3)
            print("GAME OVER\n")
            play_again()
            break
        if find_the_way == "yes":
            username()
            break
        else:
            print("Wrong input. Please type 'yes' or 'no'.")
            continue


# The username function
def username():
    """
    Continues with the story.Deals with the left/right/inland inputs a.k.a choices.
    """
    print("\nGreat! You made a life-changing decision!")
    time.sleep(2)
    print("However, the world spins when you try to get up...")
    time.sleep(2)
    print("You might have a concusion as details of the crash are blurry.\n")
    time.sleep(2)
    while True:
        name = input("Do you remember who you are? (type name):\n")
        if name == "":
            print("Wrong input. Please provide a name.")
            continue
        else:
            print(f"Hello, {name}!")
            break
    print("\nThe tide is coming in, you should get a move on!")
    time.sleep(2)
    print("You can go left along the shore, right along the shore,\n" +
          "or inland towards higher ground.\n")
    while True:
        first_choice = input("Which way will you go? (left/right/inland):\n")
        if first_choice == "right":
            second_choice()
            break
        elif first_choice == "left":
            fifth_choice()
            break
        elif first_choice == "inland":
            fourth_choice()
            break
        else:
            print("Wrong input. Please type 'left', 'right' or 'inland'.")
            continue


# Second choice function / go right find an axe
def second_choice():
    """
    Give the user the choice to pick up the axe or keep on moving
    """
    print("\nYou walk until you spot more wreckage from your plane.")
    time.sleep(2)
    print("You decide to search it.")
    time.sleep(2)
    print("You find an axe!\n")
    time.sleep(2)
    while True:
        global axe
        axe = input("Do you take it? (yes/no):\n")
        if axe == "yes":
            print("Good choice. That might be a usefool tool.")
            break
        elif axe == "no":
            print("\n Let's hope that's the right choice.")
            break
        else:
            print("Wrong input. Please type 'yes' or 'no'.")
            continue
        time.sleep(1.5)
        print("You continue looking around. It's getting dark")
        time.sleep(2)
        while True:
            third_choice = input("Do you stay or go inland? (stay/go):\n")
            if third_choice == "yes":
                print("You lay down to get some rest.")
                print("You eventually fall asleep and a poisonous snake bites you.\n")
                time.sleep(1.5)
                print("GAME OVER\n")
                play_again()
                break
            elif third_choice == "go":
                fourth_choice()
                break
            else:
                print("Wrong input. Please choose to 'go' or 'stay'.")
                continue
            time.sleep(2)
            print("You continue searching the wreckage until it gets dark.\n")
            time.sleep(2)
    while True:
        third_choice = input("Do you stay or go inland? (stay/go):\n")
        if third_choice == "stay":
            print("\nYou lay down to rest for a few minutes.")
            time.sleep(2)
            print("\nYou fall asleep without realising it.")
            time.sleep(2)
            print("You get bitten by a poisonous snake and die....\n")
            time.sleep(3)
            print("GAME OVER\n")
            play_again()
            break
        elif third_choice == "go":
            fourth_choice()
            break
        else:
            print("Wrong input. Please choose to 'go' or 'stay'.")
            continue


# The fourth choice function / inland
def fourth_choice():
    """
    If the user either choses the right path or the inland path.
    This function introduces the user to the flare.
    And the choice if they want to pick it up or move on without it.
    """
    print("\nYou keep moving forward.")
    time.sleep(1)
    print("The terrain keeps changing.\n")
    time.sleep(1)
    print("You have difficulties as there are spiky bushes.\n")
    time.sleep(1)
    print("And it's starting to rain aswell.\n")
    time.sleep(1)
    print("Trying to look for a place to stay.\n")
    time.sleep(1)
    print("You stumble upon a flare.\n")
    while True:
        global flare
        flare = input("Do you take the flare?: (yes/no)")
        time.sleep(1)
        if flare == "yes":
            print("Good choice. That might be helpful.\n")
            break
        else:
            print("Bad decision but good luck to you.")
            break
    time.sleep(2)
    print("\You keep moving forward")
    time.sleep(2)
    print("After few meters walking you come across a cave\n")
    time.sleep(1)
    print("Yuo go inside the cave")
    print("\nAs soon as you go in, you hear growling")
    print("IT'S A WOLF!!")
    while True:
        if flare == "yes":
            print("You light the flare and fortunately.\n")
            print("\nThe wolf got scared and ran away.")
            time.sleep(2)
        if flare == "yes" and axe == "yes":
            print("\nHeavy storm picking up")
            time.sleep(2)
            print("\nSo you can't go anywhere.")
            print("You end up sleeping in the cave.\n")
            time.sleep(2)
            print("Before you wake up theres an earthquake\n")
            time.sleep(2)
            print("The cave crumbles trapping you in it\n")
            time.sleep(2)
            print("You end up starving to death\n")
            time.sleep(2)
            print("GAME OVER\n")
            play_again()
            break
        elif flare == "no" and axe == "no":
            print("Without any weapons to fight the wolf\n")
            time.sleep(2)
            print("The wolf ends up biting you.\n")
            time.sleep(2)
            print("TAnd damaging your vital organs..\n")
            time.sleep(2)
            print("\nGAME OVER")
            play_again()
        else:
            print("You manage to hit the wolf but the wolf bit you back")
            print("After taking quite the serious damage")
            print("The wounbd gets infected eventually causing death..")
            print("GAME OVER")
            play_again()


# The fifth choice / Go left
def fifth_choice():
    """
    the fifth choice function
    """
    while True:
        print("Devestated yet focused.\n")
        time.sleep(2)
        print("You keep looking around..\n")
        time.sleep(2)
        print("And time is running out...\n")
        time.sleep(2)
        print(("You keep moving forward finding a way to get out.\n"))
        time.sleep(2)
        print("And you come across 2 roads\n")
        time.sleep(2)
        roads = input("Which direction do you choose ?: (left/right)\n")
        time.sleep(2)
        if roads == "left":
            global edible_fruit
            print("Good the area seems to be clear of danger")
            print("You keep exploring the terrain for food.")
            print("And you find some fruit")
            time.sleep(2)
            fruit()
            break
        elif roads == "right":
            print("Good the area seems to be clear of danger")
            bear()
            time.sleep(2)
            break
        else:
            print("Wrong input. Please type 'left', 'right'")
            continue


def fruit():
    """
    The fruit function giving the user the choice to eat the fruit or keep moving
    """
    edible_fruit = input("Do you eat the fruit ?: (yes/no)")
    if edible_fruit == "yes":
        print("Good. You are set ffor few more hours")
        print("Now you're only focusing on finding a way out...")
    elif edible_fruit == "no":
        print("Bad idea !!")
        print("You end up starving and dying...")
        print("GAME OVER !!!")
        play_again()
    else:
        print("Wrong input. Please type 'yes', 'no'")


def bear():
    """
    The bear function. Completing the right directiion of the road.
    """





game_introduction()
game_start()