# list comprehension

squares = [x**2 for x in range(1,6)]

print(squares)
print(type(squares))

# how this works

# where from a range of 1 to 6 x iterates on the range
# 1**2=1

# 2**2=4

# 3**2=9

# 4**2=16

# 5**2=25

#  now collects every element from 1 to 25

# such as [1,4,9,16,25]