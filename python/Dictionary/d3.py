# adding and updating dictionary items

d = {1:"Naruto", 2:"Death Note", 3:"life"}

# adding a new key-value pair
d['age']=22
print(d)

# updating an existing value
d[1]="python dict"
print(d)

# removing dictionary items
# del removes an item by key

#pop(), clear(), popitem()

d={1:'Abhi', 2:'for',3:"abhi"}
#using del to remove an item
del d[2]
print(d)

# using pop() to remove an item and return the value
val = d.pop(1)
print(val)

# using popitem() to removes and returns
# the last key - value pair

key, val = d.popitem()
print(f"key:{key}, Value:{val}")

# clear all items from the dictionary
d.clear()
print(d)