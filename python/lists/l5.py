# Adding Elements into List

# append    -   adds an element at the end of the list
# extend    -   adds multiple elements at the end of the list
# insert    -   adds an element at a specific position
# clear     -   removes all items
a = []

a.append(1)
print("After append(1)", a)

a.extend([2,3,5,6,7,8])
print("After extend([2,3,5,6,7,8])", a)

a.insert(1,980)
print("After insert(1,980)", a)

a.clear()
print("After clear()", a)
