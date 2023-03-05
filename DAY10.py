#https://www.hackerrank.com/challenges/30-binary-numbers/problem?
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    # Convert n to binary representation
    binary = bin(n)[2:]

    # Split binary representation into groups of consecutive 1's
    groups = binary.split('0')

    # Find the length of the longest group
    max_length = max(len(group) for group in groups)

    # Print the length of the longest group
    print(max_length)
