# iterating through a dictionary

d = {1:"abhi", 2:"for", 3:"remember"}
# iterate over keys

for key in d:
    print(key)

# iterate over values
for value in d.values():
    print(value)

# iterate over key-value pairs
for key, value in d.items():
    print(f"{key}:{value}")