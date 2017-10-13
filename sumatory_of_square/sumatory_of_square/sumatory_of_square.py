
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 17:34:24 2017

@author: Ivan
sumatoria xi **2
CS 212 -CS 101 basic
"""
"""
#thsis funsion provided by the teacher is wrong

def ss(nums):
    total=0
    for i in range(len(nums)):
        total = (total + nums[:]**2)
    return total
"""
import numpy as np

#secuencial style
nums = [2,2,2]
#np_nums = np.array(nums)

def ss(nums):
    total = 0
    for i in nums:
        total= total + (i**2)
    return total

print(ss(nums))

"""

#or can be solved by the following generator 
nums = [2,2,2]
def ss2(nums):
    return sum (x**2 for x in nums)

print(ss2(nums))
"""