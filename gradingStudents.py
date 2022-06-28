#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    new_grades = list()
    for i in range(len(grades)):
        if grades[i] < 38:
            new_grades.append(grades[i])
        else:
            if grades[i] % 5 == 4:
                grades[i] += 1
                new_grades.append(grades[i])
            elif grades[i] % 5 == 3:
                grades[i] += 2
                new_grades.append(grades[i])
            else:
                new_grades.append(grades[i])
    return new_grades
    

if __name__ == '__main__':

    # grades_count = int(input().strip())
    grades = [73, 67, 38, 33]

    result = gradingStudents(grades)
    print(result)
