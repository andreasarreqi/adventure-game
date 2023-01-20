# Importing sys and time modules
import sys
import time


global knife
knife = "no"


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
    Continues with the story, asks user to input a name. If no input,
    user asked again. If input provided, game continues giving the user
    three directions to choose from: right (second_choice function), left
    (eightth_choice function), move forward (fourth_choice function). If incorrect input
    provided, user is asked the question again.
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
            choice_eight()
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



# The function control tower
def main():
    game_introduction()
    game_start()
    username()


main()