# pass by reference  &  pass by value
def myfun(x):
    x[0] = 20

lst = [10,11,12,13]

myfun(lst)
print(lst)  # list is modified

# function tries to modify an integer

def myfun2(x):
    x = 20

a= 10

myfun2(a)
print(a)