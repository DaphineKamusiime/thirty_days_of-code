#https://www.hackerrank.com/challenges/30-bitwise-and
import math
import os
import random
import re
import sys

#
# Complete the 'bitwiseAnd' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER N
#  2. INTEGER K
#

def bitwiseAnd(N, K):
    # Write your code here
    max_bitwise_and = 0
    for i in range(N, 0, -1):
        for j in range(i-1, 0, -1):
            bitwise_and = i & j
            if bitwise_and > max_bitwise_and and bitwise_and < K:
                max_bitwise_and = bitwise_and
                if max_bitwise_and == K-1:
                    return max_bitwise_and
    return max_bitwise_and

    t = int(input().strip())
    for _ in range(t):
        n, k = map(int, input().strip().split())
        print(bitwiseAnd(n, k))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        count = int(first_multiple_input[0])

        lim = int(first_multiple_input[1])

        res = bitwiseAnd(count, lim)

        fptr.write(str(res) + '\n')

    fptr.close()
