n = 2

match n:
    case 1:
        print("one")

    case 2|3:
        print("Two or Three")
    case _:
        print("Other number")