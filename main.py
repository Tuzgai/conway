from enum import Enum
from gameboard import GameBoard
import random
import twitter_client as client
import os
import time

class StateManager:

    def __init__(self):
        pass

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
    gameboard = GameBoard(size=5, seed=4)

    client.tweet("Test run! 5")
    for i in range(0, 5):
        gameboard.display()
        gameboard.update()
        client.tweet(f"Round {i}\n{gameboard.serialize()}")
        time.sleep(5)

def TODO():
    print("whoops, not done yet")

main()