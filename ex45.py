from sys import exit
import random
import time

class Scene(object):

    def enter(self):
        print("nothing")
        exit(1)

class Map(Scene):

    def FirstMap(a, b):
        print(
            b, a, a, a,
            '|\t  Second Room\t\t|\t   Third Room\t\t|',
            a, a, a, b, a, a, a,
            '|\t  First Room\t\t|\t   Final Room\t\t|',
            a, a, a,
            '-'*12 + " "*5 + "-"*48,
            '\t      \u2191',
            '\t Starting Point\n', sep='\n')

    def SecondMap(a, b):
        print(
            b, a, a, a,
            '|\t  Second Room\t\t|\t   Third Room\t\t|',
            a, a, a, b, a, a, a,
            "|" + "-"*11 + "  \u2191  " + "-"*47 + "|",
            a, a, a,
            "|\t  First Room\t\t|\t   Final Room\t\t|",
            a, a, a,
            '-'*12 + " "*5 + "-"*48 + '\n', sep='\n')

    def ThirdMap(a, b):
        print(
            b, a, a, a,
            "|\t  Second Room\t\t\u2192\t    Third Room\t\t|",
            a, a, a,
            "|" + "-"*11 + " "*5 + "-"*47 + "|",
            a, a, a,
            "|\t  First Room\t\t|\t   Final Room\t\t|",
            a, a, a,
            '-'*12 + " "*5 + "-"*48 + '\n', sep='\n')

    def FourthMap():
        print(
            b, a, a, a,
            '|\t  Second Room\t\t|\t   Third Room\t\t|',
            a, a, a, b, a, a, a,
            "|" + "-"*11 + " "*5 + "-"*29 + "  \u2193  " + "-"*13 + "|",
            a, a, a,
            "|\t  First Room\t\t|\t   Final Room\t\t|",
            a, a, a,
            '-'*12 + " "*5 + "-"*48 + '\n', sep='\n')

    def Victory():
        print(
            b, a, a, a,
            '|\t  Second Room\t\t|\t   Third Room\t\t|',
            a, a, a, b, a, a, a,
            "|\t  Second Room\t\t     \t    Third Room\t\t|",
            a, a, a,
            "|" + "-"*11 + " "*5 + "-"*29 + " "*5 + "-"*13 + "|",
            a, a, a,
            "|\t  First Room\t\t|\t   Final Room\t\t|",
            a, a, a,
            "-"*12 + " "*5 + "-"*29 + "  \u2193  " + "-"*14,
            "\t\t\t\t\t     Victory!\n", sep='\n')

a = '|\t\t\t\t|\t\t\t\t|'
b = '-'*65

class Intro(Scene):

    def intro():
        print("Before you can start the game, I am going to ask you to give your champion a name and your enemy a name.\n")

    def __init__(self, champ_name, enemy_name):
        self.champ_name = champ_name
        self.enemy_name = enemy_name

    def names(self):
        print(self.champ_name)
        print(self.enemy_name)


class Firstroom(Scene):
    def first_room(champ_name, enemy_name):
        print(f"\n{enemy_name} has been waiting for {champ_name}")
        print(f'{enemy_name} wonders if {champ_name} is willing to play a game of rock, paper, scissors?" (y/n): ')
        while True:
            choice_rps = input()
            if choice_rps == "y" or choice_rps == "yes":
                return Firstgame.rock_paper_scissors(champ_name, enemy_name)
                break
            elif choice_rps == "n" or choice_rps == "no":
                print("You're missing out. Fuck you.")
                exit()
            else:
                print("Are you retarded? Pick y or n: ")


class Firstgame(Scene):
    time.sleep(2)
    Map.FirstMap(a, b)
    def rock_paper_scissors(champ_name, enemy_name):
        print("\nFirst player to reach 3 points wins.")
        print("Good luck!")
        champ_score = 0
        enemy_score = 0
        winscore = 3
        while True:
            if champ_score == winscore:
                secondroom.secondgame()
                break
            if enemy_score == winscore:
                Death.death1(enemy_name, champ_name)
                break
            user_action = input("Enter a choice (rock, paper, scissors): ")
            possible_actions = ["rock", "paper", "scissors"]
            computer_action = random.choice(possible_actions)
            print(f"\n{champ_name} chose {user_action}, {enemy_name} chose {computer_action}.\n")
            if user_action == computer_action:
                print(f"Both players selected {user_action}. It's a tie!")
            elif user_action == "rock":
                if computer_action == "scissors":
                    time.sleep(1)
                    print(f"Rock smashes scissors! {champ_name} wins!")
                    champ_score += 1
                    time.sleep(0.5)
                    print(f"{champ_name} has {champ_score} points while {enemy_name} has {enemy_score}")
                else:
                    time.sleep(1)
                    print(f"Paper covers rock! {enemy_name} wins!.")
                    enemy_score += 1
                    time.sleep(0.5)
                    print(f"{champ_name} has {champ_score} points while {enemy_name} has {enemy_score}")
            elif user_action == "paper":
                if computer_action == "rock":
                    time.sleep(1)
                    print(f"Paper covers rock! {champ_name} wins!")
                    champ_score += 1
                    time.sleep(0.5)
                    print(f"{champ_name} has {champ_score} points while {enemy_name} has {enemy_score}")
                else:
                    time.sleep(1)
                    print(f"Scissors cuts paper! {enemy_name} wins!")
                    enemy_score += 1
                    time.sleep(0.5)
                    print(f"{champ_name} has {champ_score} points while {enemy_name} has {enemy_score}")
            elif user_action == "scissors":
                if computer_action == "paper":
                    time.sleep(1)
                    print(f"Scissors cuts paper! {champ_name} wins!")
                    champ_score += 1
                    time.sleep(0.5)
                    print(f"{champ_name} has {champ_score} points while {enemy_name} has {enemy_score}")
                else:
                    time.sleep(1)
                    print(f"Rock smashes scissors! {enemy_name} wins!")
                    enemy_score += 1
                    time.sleep(0.5)
                    print(f"{champ_name} has {champ_score} points while {enemy_name} has {enemy_score}")
            else:
                time.sleep(0.5)
                print("Please choose between rock, paper and scissors.")

class Death(Scene):
    def death1(enemy_name, champ_name):
        time.sleep(2)
        deathstyle = random.randint(1,12)
        if deathstyle == 1:
            print(f"{champ_name} falls out of his bed and dies!")
            exit()
        if deathstyle == 2:
            print(f"{champ_name} falls off a ladder and lands head first in a water butt. {champ_name} dies on impact!")
            exit()
        if deathstyle == 3:
            print(f"{champ_name} killed himself by his own explosive while trying to steal from a condom dispenser")
            exit()
        if deathstyle == 4:
            print(f"{champ_name} gets hit by a coconut falling from a tree. {champ_name} dies from impact!")
            exit()
        if deathstyle == 5:
            print(f"{champ_name} dies from a stab in the eye with an umbrella.")
            exit()
        if deathstyle == 6:
            print(f"{champ_name} takes a selfie with a loaded handgun and shots himself in the throat. Dead!")
            exit()
        if deathstyle == 7:
            print(f"{champ_name} gets crushed while moving a fridge freezer!")
            exit()
        if deathstyle == 8:
            print(f"{champ_name} laughs so hard that he dies of heart failure")
            exit()
        if deathstyle == 9:
            print(f"{champ_name} decides to try a Sherry enema. {champ_name} dies from it.")
            exit()
        if deathstyle == 10:
            print(f"{champ_name} eats himself to death.")
            exit()
        if deathstyle == 11:
            print(f"{champ_name} is suicidal and threatens to kill himself with a knife but gets shot dead by the police.")
            exit()
        if deathstyle == 12:
            print(f"{champ_name} gets eaten alive by {enemy_name}.")
            exit()

class secondroom(Intro):

    def secondgame():
        Map.SecondMap(a, b)
        time.sleep(2)
        print(f"Congratulations {champ_name} on making it to the second room.")
        print(f"The second room is a quiz room. Is {champ_name} ready? (y/n): ")
        while True:
            choice_rps = input()
            if choice_rps == "y" or choice_rps == "yes":
                return secondroom.quiz(enemy_name, champ_name)
                break
            elif choice_rps == "n" or choice_rps == "no":
                print("You're missing out. Fuck you.")
                exit()
            else:
                print("Are you retarded? Pick y or n: ")

    def quiz(enemy_name, champ_name):
        print(f"Good choice {champ_name}.")
        print("There are a few topics to choose from. Disney, Computer, Europe or Music. Which will it be? ")
        while True:
            quiz_choice = input().capitalize()
            if quiz_choice == "Disney":
                secondroom.quiz_disney()
                break
            if quiz_choice == "Computer":
                secondroom.quiz_computer()
                break
            if quiz_choice == "Europe":
                secondroom.quiz_europe()
                break
            if quiz_choice == "Music":
                secondroom.quiz_music()
                break
            else:
                print("Please pick a topic.")

    def quiz_disney():
        while True:
            quiz_choice = random.randint(1,4)
            if quiz_choice == 1:
                print("What was Mickey Mouse originally called?")
                print("A: Keith Mouse")
                print("B: Martin Mouse")
                print("C: Mortimer Mouse")
                print("D: Michael Mouse")
                disney_answer = input().capitalize()
                if disney_answer == "A" or disney_answer == "B" or disney_answer == "D":
                    print("Too bad, it's incorrect.")
                    Death.death1(enemy_name, champ_name)
                    break
                if disney_answer == "C":
                    print(f"Congratulations, {champ_name}, you succeed!")
                    ThirdRoom.ThirdGame(champ_name, enemy_name)
                    break
                else:
                    print("A, B, C or D, please.")

            if quiz_choice == 2:
                print("Who was Bambi's rabbit pal?")
                print("A: Peter")
                print("B: Thumper")
                print("C: Fiver")
                print("D: Rick")
                disney_answer = input().capitalize()
                if disney_answer == "A" or disney_answer == "C" or disney_answer == "D":
                    print("Too bad, it's incorrect.")
                    Death.death1(enemy_name, champ_name)
                    break
                if disney_answer == "B":
                    print(f"Congratulations, {champ_name}, you succeed!")
                    ThirdRoom.ThirdGame(champ_name, enemy_name)
                    break
                else:
                    print("A, B, C or D, please.")

            if quiz_choice == 3:
                print("Who was Snow White's enemy?")
                print("A: The Evil Queen")
                print("B: Maleficent")
                print("C: Cruella De Vil")
                print("Scar")
                disney_answer = input().capitalize()
                if disney_answer == "B" or disney_answer == "C" or disney_answer == "D":
                    print("Too bad, it's incorrect.")
                    Death.death1(enemy_name, champ_name)
                    break
                if disney_answer == "A":
                    print(f"Congratulations, {champ_name}, you succeed!")
                    ThirdRoom.ThirdGame(champ_name, enemy_name)
                    break
                else:
                    print("A, B, C or D, please.")
            if quiz_choice == 4:
                print("What was the name of the man who created Pinocchio?")
                print("A: Lionel")
                print("B: Paul")
                print("C: Geppetto")
                print("D: Rusty")
                disney_answer = input().capitalize()
                if disney_answer == "A" or disney_answer == "B" or disney_answer == "D":
                    print("Too bad, it's incorrect.")
                    Death.death1(enemy_name, champ_name)
                    break
                if disney_answer == "C":
                    print(f"Congratulations, {champ_name}, you succeed!")
                    ThirdRoom.ThirdGame(champ_name, enemy_name)
                    break
                else:
                    print("A, B, C or D, please.")
    def quiz_computer():
        while True:
            quiz_choice = random.randint(1,4)
            if quiz_choice == 1:
                print("How many bytes are in 1 Kilobyte?\n")
                quiz_answer = int(input())
                if quiz_answer == 1000:
                    print(f"Congratulations, {champ_name}, you succeed!")
                    ThirdRoom.ThirdGame(champ_name, enemy_name)
                    break
                if quiz_answer > 1000:
                    print("Too bad, it's incorrect.")
                    Death.death1(enemy_name, champ_name)
                    break
                if quiz_answer < 1000:
                    print("Too bad, it's incorrect.")
                    Death.death1(enemy_name, champ_name)
                    break
                else:
                    print("Please only use numbers.")
            if quiz_choice == 2:
                print("Windows 3 was released in which year?")
                quiz_answer = input()
                if quiz_answer == 1990:
                    print(f"Congratulations, {champ_name}, you succeed!")
                    ThirdRoom.ThirdGame(champ_name, enemy_name)
                    break
                if quiz_answer < 1990:
                    print("Too bad, it's incorrect.")
                    Death.death1(enemy_name, champ_name)
                    break
                if quiz_answer > 1990:
                    print("Too bad, it's incorrect.")
                    Death.death1(enemy_name, champ_name)
                    break
                else:
                    print("Please only use numbers.")
            if quiz_choice == 3:
                print("What was the fastest growing web browser in 2020?")
                print("A: Microsoft Edge")
                print("B: Firefox")
                print("C: DuckDuckGo")
                print("D: Internet Explorer")
                computer_answer = input().capitalize()
                if computer_answer == "B" or computer_answer == "C" or computer_answer == "D":
                    print("Too bad, it's incorrect.")
                    Death.death1(enemy_name, champ_name)
                    break
                if computer_answer == "A":
                    print(f"Congratulations, {champ_name}, you succeed!")
                    ThirdRoom.ThirdGame(champ_name, enemy_name)
                    break
                else:
                    print("A, B, C or D, please.")
            if quiz_choice == 4:
                print("Which University offered the first-ever academic programme in Computer Science?")
                print("A: Harvard University")
                print("B: MIT")
                print("C: University of Glasgow")
                print("D: Cambridge University")
                computer_answer = input().capitalize()
                if computer_answer == "A" or computer_answer == "B" or computer_answer == "C":
                    print("Too bad, it's incorrect.")
                    Death.death1(enemy_name, champ_name)
                    break
                if computer_answer == "D":
                    print(f"Congratulations, {champ_name}, you succeed!")
                    ThirdRoom.ThirdGame(champ_name, enemy_name)
                    break
                else:
                    print("A, B, C or D, please.")
    def quiz_europe():
        while True:
            quiz_choice = random.randint(1,4)
            if quiz_choice == 1:
                print("Which of the following is the nickname of Europe?")
                print("A: The Great Continet")
                print("B: The Old Continent")
                print("C: The Holy Continent")
                europe_answer = input().capitalize()
                if europe_answer == "A" or europe_answer == "C":
                    print("Too bad, it's incorrect.")
                    Death.death1(enemy_name, champ_name)
                    break
                if computer_answer == "B":
                    print(f"Congratulations, {champ_name}, you succeed!")
                    ThirdRoom.ThirdGame(champ_name, enemy_name)
                    break
                else:
                    print("A, B or C, please.")
            if quiz_choice == 2:
                print("What percentage of the world’s population lives in Europe?")
                print("A: Around 15 percent")
                print("B: Around 25 percent")
                print("C: Around 35 percent")
                europe_answer = input().capitalize()
                if europe_answer == "A" or europe_answer == "C":
                    print("Too bad, it's incorrect.")
                    Death.death1(enemy_name, champ_name)
                    break
                if computer_answer == "B":
                    print(f"Congratulations, {champ_name}, you succeed!")
                    ThirdRoom.ThirdGame(champ_name, enemy_name)
                    break
                else:
                    print("A, B or C, please.")
            if quiz_choice == 3:
                print("3. Which nation has won the most titles in the Eurovision Song Contest?")
                print("A: Ireland")
                print("B: Sweden")
                print("C: France")
                europe_answer = input().capitalize()
                if europe_answer == "B" or europe_answer == "C":
                    print("Too bad, it's incorrect.")
                    Death.death1(enemy_name, champ_name)
                    break
                if computer_answer == "A":
                    print(f"Congratulations, {champ_name}, you succeed!")
                    ThirdRoom.ThirdGame(champ_name, enemy_name)
                    break
                else:
                    print("A, B or C, please.")
    def quiz_music():
        while True:
            quiz_choice = random.randint(1,4)
            if quiz_choice == 1:
                print("What was Ludwig van Beethoven's final complete symphony?")
                print("A: Symphony no. 9")
                print("B: Symphony no. 10")
                print("C: Symphony no. 8")
                print("D: Symphony no. 7")
                music_answer = input().capitalize()
                if music_answer == "D" or music_answer == "B" or music_answer == "C":
                    print("Too bad, it's incorrect.")
                    Death.death1(enemy_name, champ_name)
                    break
                if music_answer == "A":
                    print(f"Congratulations, {champ_name}, you succeed!")
                    ThirdRoom.ThirdGame(champ_name, enemy_name)
                    break
                else:
                    print("A, B, C or D, please.")
            if quiz_choice == 2:
                print("Who composed the music for The Nutcracker?")
                print("A: Aram Khachaturian")
                print("B: Igor Stravinsky")
                print("C: Sergei Prokofiev")
                print("D: Pyotr Ilyich Tchaikovsky")
                music_answer = input().capitalize()
                if music_answer == "A" or music_answer == "B" or music_answer == "C":
                    print("Too bad, it's incorrect.")
                    Death.death1(enemy_name, champ_name)
                    break
                if music_answer == "D":
                    print(f"Congratulations, {champ_name}, you succeed!")
                    ThirdRoom.ThirdGame(champ_name, enemy_name)
                    break
                else:
                    print("A, B, C or D, please.")
            if quiz_choice == 3:
                print("What violinist was rumored to have sold his soul to the devil?")
                print("A: George Enescu")
                print("B: Niccolo Paganini")
                print("C: Itzhak Perlman")
                print("D: Yehudi Menuhin")
                music_answer = input().capitalize()
                if music_answer == "A" or music_answer == "D" or music_answer == "C":
                    print("Too bad, it's incorrect.")
                    Death.death1(enemy_name, champ_name)
                    break
                if music_answer == "B":
                    print(f"Congratulations, {champ_name}, you succeed!")
                    ThirdRoom.ThirdGame(champ_name, enemy_name)
                    break
                else:
                    print("A, B, C or D, please.")
            if quiz_choice == 4:
                print('Which Austrian composer was nicknamed "Little Mushroom" by his friends?')
                print("A: Franz Schubert")
                print("B: Johann Strauss")
                print("C: Wolfgang Amadeus Mozart")
                print("D: Arnold Schoenberg")
                music_answer = input().capitalize()
                if music_answer == "B" or music_answer == "D" or music_answer == "C":
                    print("Too bad, it's incorrect.")
                    Death.death1(enemy_name, champ_name)
                    break
                if music_answer == "A":
                    print(f"Congratulations, {champ_name}, you succeed!")
                    ThirdRoom.ThirdGame(champ_name, enemy_name)
                    break
                else:
                    print("A, B, C or D, please.")


class ThirdRoom(Scene):
    def ThirdGame(champ_name, enemy_name):
        time.sleep(1)
        print(f"Well done, {champ_name}! You've made it to the third room")
        Map.ThirdMap(a, b)
        time.sleep(1)
        print("Your next challenge is a math challenge.")
        print("First question: What's 2 + 2 * 2?")
        time.sleep(1)
        while True:
            math_answer = int(input())
            if math_answer == 6:
                print("Great job!")
                break
            if math_answer == 8:
                time.sleep(2)
                print("You're an idiot. Go back to school.")
                death.death1()
                break
            if math_answer > 6 and math_answer < 8:
                print("Incorrect. Sorry.")
                death.death1()
                break
            if math_answer < 6:
                print("Incorrect. Sorry.")
                death.death1()
                break
            if math_answer > 8:
                print("Incorrect. Sorry.")
                death.death1()
                break
            else:
                print("Please use numbers only")
        print("Next round!")
        time.sleep(1)
        print("If 1 = 3")
        print("2 = 3")
        print("3 = 5")
        print("4 = 4")
        print("5 = 4")
        print("Then, 6 = ?")
        time.sleep(1)
        while True:
            math_answer = int(input())
            if math_answer == 3:
                print("Correct, because 6 has three letters in it.")
                break
            if math_answer > 3:
                print("Incorrect. Sorry.")
                death.death1()
                break
            if math_answer < 3:
                print("Incorrect. Sorry.")
                death.death1()
                break
            else:
                print("Please use numbers only.")
                time.sleep(1)
        print(f"Good job {champ_name}, soon you'll beat {enemy_name}.")
        time.sleep(0.5)
        print("Next and final question for this room.")
        time.sleep(1)
        print("I am an odd number. Take away one letter and I become even. What number am I?")
        time.sleep(0.5)
        while True:
            math_answer = input().capitalize()
            if math_answer == "Seven":
                print("Correct. Congratulations, you're not dumb.")
                print("Seven without the s is even.")
                print("On to the final room.")
                time.sleep(2)
                Fourthroom.Fourthgame(champ_name, enemy_name)
                break
            if math_answer == "7":
                print("Correct. Congratulations, you're not dumb.")
                print("Seven without the s is even.")
                print("On to the final room.")
                time.sleep(2)
                Fourthroom.Fourthgame(champ_name, enemy_name)
                break
            else:
                print("You're an idiot. WRONG.")
                death.death1()

class FourthRoom(Scene):
    def Fourthgame(champ_name, enemy_name):
        Map.FourthMap(a, b)
        time.sleep(1)
        print(f"Congratulations on making it to the last room, {champ_name}")
        time.sleep(1)
        print("Your last challenge is hangman")
        time.sleep(1)
        print(f"If you can beat {enemy_name} in hangman, you win the game!")
    def hangman():
        words_to_guess = ["january","border","image","film","promise","kids","lungs","doll","rhyme","damage"
                       ,"plants"]
        word = random.choice(words_to_guess)
        length = len(word)
        count = 0
        display = '_' * length
        already_guessed = []
        play_game = ""
        limit = 8
        while True:
            guess = input("This is the Hangman Word: " + display + " Enter your guess: \n")
            guess = guess.strip()
            if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
                print("Invalid Input, Try a letter\n")
            elif guess in word:
                already_guessed.extend([guess])
                index = word.find(guess)
                word = word[:index] + "_" + word[index + 1:]
                display = display[:index] + guess + display[index + 1:]
                print(display + "\n")
            elif guess in already_guessed:
                print("Try another letter.\n")
            else:
                count += 1
                if count == 1:
                    time.sleep(1)
                    print("   _____ \n"
                          "  |      \n"
                          "  |      \n"
                          "  |      \n"
                          "  |      \n"
                          "  |      \n"
                          "  |      \n"
                          "__|__\n")
                    print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
                elif count == 2:
                    time.sleep(1)
                    print("   _____ \n"
                          "  |     | \n"
                          "  |     |\n"
                          "  |      \n"
                          "  |      \n"
                          "  |      \n"
                          "  |      \n"
                          "__|__\n")
                    print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
                elif count == 3:
                   time.sleep(1)
                   print("   _____ \n"
                         "  |     | \n"
                         "  |     |\n"
                         "  |     | \n"
                         "  |      \n"
                         "  |      \n"
                         "  |      \n"
                         "__|__\n")
                   print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
                elif count == 4:
                    time.sleep(1)
                    print("   _____ \n"
                          "  |     | \n"
                          "  |     |\n"
                          "  |     | \n"
                          "  |     O \n"
                          "  |      \n"
                          "  |      \n"
                          "__|__\n")
                    print("Wrong guess. " + str(limit - count) + " last guess remaining\n")
                elif count == 5:
                    time.sleep(1)
                    print("   _____ \n"
                          "  |     | \n"
                          "  |     |\n"
                          "  |     | \n"
                          "  |     O \n"
                          "  |     | \n"
                          "  |        \n"
                          "__|__\n")
                    print("Wrong guess. " + str(limit - count) + " last guess remaining\n")
                elif count == 6:
                    time.sleep(1)
                    print("   _____ \n"
                          "  |     | \n"
                          "  |     |\n"
                          "  |     | \n"
                          "  |     O \n"
                          "  |    /|  \n"
                          "  |        \n"
                          "__|__\n")
                    print("Wrong guess. " + str(limit - count) + " last guess remaining\n")

                elif count == 7:
                    time.sleep(1)
                    print("   _____ \n"
                          "  |     | \n"
                          "  |     |\n"
                          "  |     | \n"
                          "  |     O \n"
                          "  |    /|\  \n"
                          "  |        \n"
                          "__|__\n")
                    print("Wrong guess. " + str(limit - count) + " last guess remaining\n")
                elif count == 8:
                    time.sleep(1)
                    print("   _____ \n"
                          "  |     | \n"
                          "  |     |\n"
                          "  |     | \n"
                          "  |     O \n"
                          "  |    /|\ \n"
                          "  |    / \ \n"
                          "__|__\n")
                    print("Wrong guess. You are hanged!!!\n")
                    print("The word was:",word)
                    time.sleep(2)
                    print("You're a loser. Goodbye!")
                    death.death1()
                    break
            if word == '_' * length:
                print("Congrats! You have guessed the word correctly!")
                FourthRoom.victory(champ_name, enemy_name)
                break
    def victory(champ_name, enemy_name):
        Map.Victory(a,b)
        print(f"Congratulations {champ_name}, you've won the game!")
        print("Also, fuck you, it took me way too long to create this game.")
        exit()











Intro.intro()
champ_name = input("What would you like your champion to be called? ")
enemy_name = input("\nWhat would you like the enemy name to be? ")
Firstroom.first_room(champ_name, enemy_name)
a = '|\t\t\t\t|\t\t\t\t|'
b = '-'*65
