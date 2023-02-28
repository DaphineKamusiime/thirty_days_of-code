#https://www.hackerrank.com/challenges/30-arrays/problem
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

# read in the array of integers
arr = list(map(int, input().split()))

# print the array in reverse order
for i in range(n-1, -1, -1):
    print(arr[i], end=" ")
