# Arbitrary Arguments

# *args in python(Non-keyword Argyments)
# **args in python(keyword Argyments)

def myfun(*args, **kwargs):
    print("Non-Keyword Arguments(*args):")
    for arg in args:
        print(arg)
    print("\nKeyword Arguments(**kwargs):")
    for key, value in kwargs.items():
        print(f"{key} == {value}")

myfun("hey", "welcome", first="Geeks", mid="for", last="Geeks")