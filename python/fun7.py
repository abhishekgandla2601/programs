# function within functions
def f1():
    s="I love coding"
    def f2():
        print(s)
    f2()
f1()