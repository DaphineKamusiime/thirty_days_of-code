#https://www.hackerrank.com/challenges/30-exceptions-string-to-integer
#!/bin/python3

import math
import os
import random
import re
import sys

S = input().strip()

try:
    num = int(S)
    print(num)
except ValueError:
    print("Bad String")
