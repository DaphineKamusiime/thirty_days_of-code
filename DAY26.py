#https://www.hackerrank.com/challenges/30-nested-logic/
return_date = list(map(int, input().split()))
due_date = list(map(int, input().split()))

if return_date[2] > due_date[2]:
    fine = 10000
elif return_date[2] < due_date[2]:
    fine = 0
elif return_date[1] > due_date[1]:
    fine = 500 * (return_date[1] - due_date[1])
elif return_date[0] > due_date[0]:
    fine = 15 * (return_date[0] - due_date[0])
else:
    fine = 0
    
print(fine)
