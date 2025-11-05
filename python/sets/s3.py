# removing elements from the set in python
# using remove(), pop(), discard()

# clear()

set1 = {1,2,3,4,5}
set1.remove(3)
print(set1)

# attempting to remove an element that does not exist
try:
    set1.remove(10)
except KeyError as e:
    print("error", e)

# using discard() Method
set1.discard(4)
print(set1)

# Attempting to discard an element that does not exist
set1.discard(10)# no error raised

print(set1)

# using pop() method

set1 = {1,2,3,4,5}
val = set1.pop()
print(val)
print(set1)

# using pop on an empty set

set1.clear() # clear the set to make it empty
try:
    set1.pop()
except KeyError as e:
    print('error',e)

