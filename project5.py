import random

print("Welcome to the coin flip game")
heads_or_tails = random.randint(0, 1)

if heads_or_tails == 1:
    print("Heads")
else:
    print('Tails')
