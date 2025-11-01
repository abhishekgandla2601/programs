# Multiples of given number in a given range

n = int(input("Enter a number: "))

for i in range(1, 50):
    if i % n == 0:
        print(i)