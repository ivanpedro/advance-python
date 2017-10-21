# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 20:55:22 2017

@author: Ivan
"""

# -----------
# User Instructions
# 
# Modify the test() function to include two new test cases:
# 1) four of a kind (fk) vs. full house (fh) returns fk.
# 2) full house (fh) vs. full house (fh) returns fh.
#
# Since the program is still incomplete, clicking RUN won't do 
# anything, but clicking SUBMIT will let you know if you
# have gotten the problem right.
#HAND EXAMPLES 
# straight flush 8, 11 for Jack
#FOUR ACES IS MAJOR RANK NUMBER 7
#ACE IS CARD RANK NUMBER 14
#QUEEN RANK 12

def poker(hands):
    "Return the best hand: poker([hand, ...]) => hand"
    return max(hands, key = hand_rank)

def hand_rank(hand):
    "return a value indicationg the ranking of a hand."
    ranks = card_ranks(hand)
    if straight (ranks) and flush(hand):
        return (8, max(ranks))# 2 3 4 5 6 (8,6) 6 7 8 9 T (8, 10)
    elif kind (4 , ranks):
        return (7, kind(4,ranks), kind(1,ranks))#9 9 9 9 3 9(7,9,3)
    elif :


def test():
    "Test cases for the functions in poker program"
    sf = "6C 7C 8C 9C TC".split() # Straight Flush
    fk = "9D 9H 9S 9C 7D".split() # Four of a Kind
    fh = "TD TC TH 7C 7D".split() # Full House
    assert poker([sf, fk, fh]) == sf
    assert poker([fk, fh]) == fk
    assert poker([fh, fh]) == fh
    assert poker([sf]) == sf
    assert poker([sf] + 99*[fh]) == sf
    # For example, calling hand_rank on sf should output (8, 10)
    assert hand_rank([sf]) == (8,10)
    assert hand_rank([sf]) == (7,9,7)
    assert hand_rank([sf]) == (6,10,7)
    return "test pass"
print (test())
print (max([3,4,5,0]), max([3,2,-5,4],key = abs))
