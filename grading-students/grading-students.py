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
    result = []
    for i in grades:
        temp = i % 5
        temp2 = i + (5-temp)
        temp3 = temp2 - i
        if i < 38:
            result.append(i)
            continue
        elif temp3<3:
            result.append(i + temp3)
        else:
            result.append(i)
    return result
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)
    
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')