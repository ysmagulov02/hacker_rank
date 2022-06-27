#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    arr.sort()
    min = 0
    max = 0
    for i in range(len(arr)):
        min += arr[i]
        if (i == len(arr) - 2):
            break

    for j in range(len(arr)):
        if (j == 0):
            continue
        max += arr[j]
    
    print(min, max)


if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
