from NumberMemory import *
from ReactionTime import *
from server import *

def startServer():
    server = Server()
    server.run()

startServer()

# isCLI = int(input("1. CLI\n2. Website\n"))
# if isCLI:
#     ...
# else:
#     startServer()

# user_choice = int(input("1. ReactionTime\n2. NumberMemory\n"))
# game = ReactionTime()

# if user_choice == 1:
#     game = ReactionTime()
# elif user_choice == 2:
#     game = NumberMemory()
    
# game.play()
# game.showScores()