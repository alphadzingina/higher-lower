from art import logo
from game_data import data
import random

print(logo)

player_a = random.choice(data)
player_b = random.choice(data)
if player_a == player_b:
    player_b = random.choice(data)