# creating tuple with mixed datatypes

tup = (5,'welcome', 7, "geeks", True)

print(tup)

# creating tuple with nested tuples

tup1 = (0,1,2,3)

tup2 = ("python", "flask")

tup3 = (tup1, tup2)

print(tup3)

# creating a tuple with repetition
tup1 = ('Geeks',)*3
print(tup1)

# creating a tuple with use of loop
tup = ('abhi')

n=5
for i in range(n):
    tup = (tup,)
    print(tup)