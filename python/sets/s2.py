# unordered, unindexed and mutability

set1 = {3,1,4,1,5,9,2}

print(set1)

try:
    print(set1[0])
except TypeError as e:
    print(e)

# adding elements to a set in python

#  creating a set
set1 = {1,2,3}

# add one item
set1.add(4)

# accessing a set in python
set1 = set(['geeks', 'for', 'geeks'])

# accessing element using for loop
for i in set1:
    print(i, end="")
