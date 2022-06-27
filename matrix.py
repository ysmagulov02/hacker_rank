#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    x1 = 0
    x2 = 0
    
    # print("range: " + str(len(arr)))
    for i in range((len(arr))):
        x1 += arr[i][i]
    # print("x1: " + str(x1))
        
    j = int(len(arr)) - 1
    for k in range(len(arr)):
        x2 += arr[k][j]
        j -= 1
    # print("x2: " + str(x2))
            
    return abs(x1 - x2)
    
    

if __name__ == '__main__':
    # n = int(input().strip())
    n = 3

    arr = [[11, 2, 4],
           [4, 5, 6],
           [10, 8, -12]
        ]

    result = diagonalDifference(arr)
    
    print(result)
