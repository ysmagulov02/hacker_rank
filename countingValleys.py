#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

#
# A valley is a sequence of consecutive steps below sea level, 
# starting with a step down from sea level and 
# ending with a step up to sea level.
#

def countingValleys(steps, path):
    # Write your code here
    sea_level = 0
    valley_count = 0

    for step in path:
        if step == 'D':
            sea_level -= 1
        elif step == 'U':
            sea_level += 1
        
        if sea_level == 0 and step == 'U':
            valley_count += 1
        

    return valley_count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()