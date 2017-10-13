
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 20:55:22 2017

@author: Ivan
"""

# -----------
# User Instructions
# 
# Modify the test() function to include two new test cases:
# 1) A single hand.
# 2) 100 hands.
#
# Since the program is still incomplete, clicking RUN won't do 
# anything, but clicking SUBMIT will let you know if you
# have gotten the problem right. 

def poker(hands):
    "Return the best hand: poker([hand,...]) => hand"
    return max(hands, key=hand_rank)

def test():
    "Test cases for the functions in poker program"
    sf = "6C 7C 8C 9C TC".split() 
    fk = "9D 9H 9S 9C 7D".split() 
    fh = "TD TC TH 7C 7D".split()
    assert poker([sf, fk, fh]) == sf
    assert poker([fk, fh]) == fk
    assert poker([fh, fh]) == fh
    #99 *[fh] it makes 99 items list and concatenate adding to [sf] list making 100 ithems
    assert poker([sf]) == sf
    assert poker([sf]+ 99*[fh]) == sf
   
    # Add 2 new assert statements here. The first 
    # should assert that when poker is called with a
    # single hand, it returns that hand. The second 
    # should check for the case of 100 hands.
    return 'tests pass'

print (test())
print (max([3,4,5,0]), max([3,2,-5,4],key = abs))