from enum import Enum
from gameboard import GameBoard
import random

class StateManager:
    def __init__(self):
        TODO()

    def getBoard():
        TODO()
        return GameBoard()

    def saveBoard(gameboard):
        TODO()

    def postBoard(gameboard):
        TODO()

def main():
    # get previous state
    sm = StateManager()
    gameboard = GameBoard(28)

    for i in range(0, 10):
        gameboard.display()
        gameboard.update()

    gameboard.display()

def TODO():
    print("whoops, not done yet")

main()