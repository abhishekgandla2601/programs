# Natural numbers from 1 to 10 except 3 & 7

n = 10

i =0

while i < n:
    i = i + 1
    if i==3 or i==7:
        continue
    else:
        print(i)