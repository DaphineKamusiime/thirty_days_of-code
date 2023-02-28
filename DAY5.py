#!/bin/python3
#https://www.hackerrank.com/challenges/30-loops/problem?h_r=email&unlock_token=d2d05949ad03b92ed5a9e793e4d173aaee3fd95a&utm_campaign=30_days_of_code_continuous&utm_medium=email&utm_source=daily_reminder
import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    for i in range(1,11):
        print(n, "x", i , "=", n*i)
        
