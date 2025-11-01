# lambda functions

n = lambda x:"Positivie" if x > 0 else "Negative" if x < 0 else "Zero"
print(n(5))
print(n(-3))
print(n(0))

check = lambda x:"Even" if x % 2 == 0 else "Odd"

print(check(4))
print(check(7))