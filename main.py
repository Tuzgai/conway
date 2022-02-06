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

def main():
    seed, step = get_state()

    gameboard = GameBoard(size=5, seed=seed)

    for i in range(0, step):
        gameboard.update()

    client.tweet(f"Seed: {seed}\nStep: {step+1}\n{gameboard.serialize()}")

main()