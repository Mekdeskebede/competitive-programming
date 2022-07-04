#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    if 1<=n <= 1000:
        insertion = arr[n-1]
        
        for i in reversed(range(n)):
            if arr[i] == insertion:
                arr[i]= arr[i-1]
                continue
                
            if arr[i] >insertion:
                arr[i+1] = arr[i]
            elif arr[i] < insertion:
                arr[i+1] = insertion
            
            print(*arr)
        

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
