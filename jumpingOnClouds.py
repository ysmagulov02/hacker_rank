#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumpingOnClouds(c):
    # Write your code here
    i = 0
    jump_count = 0
    last_cloud_postion = len(c)-1
    last_second_postion = len(c)-2
    
    while i < last_second_postion:
        # Checking if the cloud next to the next cloud is thunderstorm
        if c[i+2] == 0:
            i += 2
            jump_count += 1
        else:
            i += 1
            jump_count += 1
    # Checking if we are in the last cloud or the last second cloud
    if i != last_cloud_postion:
        jump_count += 1
        
    return jump_count
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
