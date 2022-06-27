#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    # Write your code here
    space_num = n-1
    for i in range(n):
        pound_num = i + 1
        print(" " * space_num + "#" * pound_num)
        space_num -= 1

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
