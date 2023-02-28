#https://www.hackerrank.com/challenges/30-review-loop/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
# number of test cases
T = int(input())

for i in range(T):
    # read in the string
    s = input()
    
    # initialize even and odd strings
    even_chars = ""
    odd_chars = ""
    
    # iterate through the string
    for j in range(len(s)):
        # if the index is even, add the character to the even string
        if j % 2 == 0:
            even_chars += s[j]
        # if the index is odd, add the character to the odd string
        else:
            odd_chars += s[j]
    
    # print the even and odd strings separated by a space
    print(even_chars + " " + odd_chars)

