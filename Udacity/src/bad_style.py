#Texto con mal estilo de codificación, corregido abajo

# import random, os

# catString = "--Whiskers--, --Spot--, --Meowmeow--, --Tiger--,  --Kitty--, --Henry--, --Mr.Paws--"
# def RANDOM_CAT(string_list):
#     cat_list = catString.split(', ')# split the cats
#     cat_list = [cat.strip('--') for cat in cat_list]
#         return random.choice(cat_list)

# print(  f'{RANDOM_CAT(catString)} is a good kitty'  )

import random
import os

catString = "--Whiskers--, --Spot--, --Meowmeow--, --Tiger--," \
            "  --Kitty--, --Henry--, --Mr.Paws--"


def RANDOM_CAT(string_list):
    cat_list = catString.split(', ')  # split the cats
    cat_list = [cat.strip('--') for cat in cat_list]
    return random.choice(cat_list)


print(f'{RANDOM_CAT(catString)} is a good kitty')
