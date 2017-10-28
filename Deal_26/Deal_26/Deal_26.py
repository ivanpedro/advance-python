
# -----------
# User Instructions
# 
# Write a function, deal(numhands, n=5, deck), that 
# deals numhands hands with n cards each.
#

import random # this will be a useful library for shuffling

# This builds a deck of 52 cards. If you are unfamiliar
# with this notation, check out Andy's supplemental video
# on list comprehensions (you can find the link in the 
# Instructor Comments box below).

##mydeck = [r+s for r in '23456789TJQKA' for s in 'SHDC'] 

#def deal(numhands, n=5, deck=mydeck):
#    # Your code here.

mydeck = [r+s for r in '23456789TJQKA' for s in 'SHDC'] 
#mydeck generate a list in this format
# ['2S', '2H', '2D', '2C',
# '3S', '3H', '3D', '3C', 
# '4S', '4H', '4D', '4C',
# '5S', '5H', '5D', '5C',
# '6S', '6H', '6D', '6C',
# '7S', '7H', '7D', '7C',
# '8S', '8H', '8D', '8C',
# '9S', '9H', '9D', '9C',
# 'TS', 'TH', 'TD', 'TC',
# 'JS', 'JH', 'JD', 'JC',
# 'QS', 'QH', 'QD', 'QC',
# 'KS', 'KH', 'KD', 'KC',
# 'AS', 'AH', 'AD', 'AC']

def deal(numhands, n=5, deck= mydeck):
    # "Shuffle the deck and deal out numhands n-card hands."
    random.shuffle(deck)
    return [deck[n*i:n*(i + 1)] for i in range(numhands)]

#print(deal(5))
print(mydeck)