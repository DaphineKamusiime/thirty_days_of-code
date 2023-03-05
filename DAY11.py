#https://www.hackerrank.com/challenges/30-2d-arrays/problem
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    
        
    max_sum = float('-inf')
    for i in range(1, 5):
        for j in range(1, 5):
            # Calculate sum of hourglass centered at current cell
            hourglass_sum = (arr[i-1][j-1] + arr[i-1][j] + arr[i-1][j+1] +
                             arr[i][j] +
                             arr[i+1][j-1] + arr[i+1][j] + arr[i+1][j+1])

            # Update maximum hourglass sum seen so far
            max_sum = max(max_sum, hourglass_sum)

    print(max_sum)