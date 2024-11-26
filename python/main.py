from NumberMemory import *
from ReactionTime import *
from VerbalMemory import *
from Server import *

def clear():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def CLI():
    clear()
    user_choice = input("1. ReactionTime\n2. Number Memory\n3. Verbal Memory\n4. Scores\n> ")

    while user_choice != "1" and user_choice != "2" and user_choice != "3" and user_choice != "4":
        clear()
        user_choice = input("1. ReactionTime\n2. Number Memory\n3. Verbal Memory\n4. Scores\n> ")

    if user_choice == "1":
        game = ReactionTime.ReactionTime()
        game.play()
        return
    elif user_choice == "2":
        game = NumberMemory.NumberMemory()
        game.play()
        return
    elif user_choice == "3":
        game = VerbalMemory.VerbalMemory()
        game.play()
        return
    elif user_choice == "4":
        clear()
        rt = ReactionTime.ReactionTime()
        nm = NumberMemory.NumberMemory()
        vm = VerbalMemory.VerbalMemory()

        print("---Reaction Time---")
        rt.scoreboard.printScores()
        print("")
        print("---Number Memory---")
        nm.scoreboard.printScores()
        print("")
        print("---Verbal Memory---")
        vm.scoreboard.printScores()
        print("")

        return


def run():
    clear()

    isCLI = input("1. CLI,\n2. Website\n> ")

    while isCLI != "1" or isCLI != "2":
        if isCLI == "1":
            CLI()
            return
            
        if isCLI == "2":
            clear()
            s = Server()
            s.run() 
            return

        
if __name__ == "__main__":
    run()

