# natural numbers 1 to 10 except 6

n = 10

i = 0

while i < n:
    i=i+1
    if i %6 ==0:
        continue
    else:
        print(i)