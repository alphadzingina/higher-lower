from art import logo
from game_data import data
import random


print(logo)

#rabdomly select celebrity from data
celebrity1 = random.choice(data)
celebrity2 = random.choice(data)

print(celebrity1)
print(celebrity2)