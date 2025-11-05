# operations of tuples

# accessing
# contatenation
#slicing
#deleting

# accessing
#accessing tuple with indexing
tup = tuple('abhi')

print(tup[0])

#accessing a range of elements using slicing
print(tup[1:4])# 4-1    then    1to3 index values
print(tup[:4])# 0-4     then    0 1 2 3 it gives the values of 0=? 1=? 2=? 3=?

# tuple unpacking
tup = ('hi', 'hello', 'namastee')

a,b,c = tup #a="hi" b="hello" c="namastee"

print(a)
print(b)
print(c)