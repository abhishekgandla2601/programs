# Given an integer n find the sum of the first n natural number.

def nSum(n):
    # code here
    add = []
    for i in range(1,n+1):
        add.append(i)
    total = 0
    for j in add:
        total = total + j

    ans = total

    return ans
nSum(10)