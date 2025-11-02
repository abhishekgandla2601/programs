# updating elements into list
# since lists are mutable, we can update elements by accessing them via their index
a=[10,20,30,40,50]
a[1] =5
print(a)

# removing Elements from List

'''
remove()
pop()
del statement: deletes an element at a specified index
'''

b = [100, 233, 2322, 1442, 4413]

b.remove(100)
print(b)

b.pop()# pop out the last element
print(b)

del b[0]
print(b)

