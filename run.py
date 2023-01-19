#Importing sys and time modules
import sys
import time

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
    print("BOOM...\n")
    print(".")
    print(".")


game_introduction()


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
            get_username()
            break
        else:
            print("Wrong input. Please type 'yes' or 'no'.")
            continue


game_start()


def username():
 """
    Continues with the story, asks user to input a name. If no input,
    user asked again. If input provided, game continues giving the user
    three directions to choose from: right (second_choice function), left
    (eightth_choice function), move forward (fourth_choice function). If incorrect input
    provided, user is asked the question again.
    """