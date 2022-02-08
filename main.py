from enum import Enum
from gameboard import GameBoard
import random
import twitter_client as client
import os
import time
import json

def get_state():
    previous_tweet = client.get_latest_tweets().get('data')[0].get('text')
    lines = previous_tweet.split('\n')
    seed = lines[0].split(':')[1]
    step = lines[1].split(':')[1]
    return (int(seed), int(step))

def main(*_):
    seed, step = get_state()
    size = 100

    gameboard = GameBoard(size=size, 
                          seed=seed,
                          view_x=50,
                          view_y=50,
                          view_size=10)

    previous_rounds = []
    for i in range(0, step+1):
        gameboard.update()
        previous_rounds.append(gameboard.get_twitter_content())

    current_round = gameboard.get_twitter_content()
    for round in previous_rounds[:-1]:
        if round == current_round:
            seed += 1
            gameboard = GameBoard(size=size, seed=seed)
            client.tweet(f"Seed: {seed+1}\nStep: {0}\nCycle detected, starting new seed!\n{gameboard.get_twitter_content()}")
            return

    client.tweet(f"Seed: {seed}\nStep: {step+1}\n{current_round}")

main()