#https://www.hackerrank.com/challenges/30-dictionaries-and-maps/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT

# read in the number of entries in the phone book
n = int(input())

# create an empty dictionary to store the phone book entries
phone_book = {}

# read in the phone book entries and store them in the dictionary
for i in range(n):
    name, number = input().split()
    phone_book[name] = number

# loop through the queries and print the corresponding phone numbers
while True:
    try:
        query = input()
        if query in phone_book:
            print(query + "=" + phone_book[query])
        else:
            print("Not found")
    except:
        break
