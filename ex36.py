from sys import exit

def start():
    print("Your mother is angry at you for leaving out the dishes.")
    print("Do you \nA: Go do the dishes right away\nB: Yell at your mother")
    choice = input("> ")
    if choice == "A":
        not_angry()
    elif choice == "B":
        print("You have awaken the beast, she's at war with you.")
        print("A war you're not going to win")
        dead("You have chosen the wrong option,")
    else:
        start()


def not_angry():
    print("You are lucky to escape this time.")
    print("The washing machine has just finished")
    print("You see your mother giving you an eye.")
    print("Do you leave the washing machine alone or do you take out the clothes and hang them up?")
    wm = input("> ")
    if wm == "leave":
        print("You have awaken the beast, she's at war with you.")
        print("A war you're not going to win")
        dead("You have chosen the wrong option, ")
    elif wm == "take out clothes":
        print("You have survived this time.")
        happy_place()
    else:
        not_angry()


def happy_place():
    print("Your mother is happy with you.")
    print("There's still tention in the air.")
    print("Everyone's afraid of her next move.")
    print("You can either leave the scenario or face it.")
    print("What do you do?")
    happy_tension = input("> ")
    if happy_tension == "leave":
        print("You're unhappy, you son of a bitch.")
        print("But you need to make money to buy your first place.")
        print("Therefore you allow the tension to be there.")
        exit()
    elif happy_tension == "face it":
        dead("You really shouldn't have done that,")
    else:
        happy_place()

def dead(why):
    print(why, "prepare to die!")
    exit(0)

start()
