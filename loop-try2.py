for x in range(100):

    if x % 3 == 0 and x % 5 == 0:
        print("FIZZBUZZ")
        continue

    elif x % 5 == 0:
        print("BUZZ")
        continue

    elif x % 3 == 0:
        print("FIZZ")
        continue

    print(x)
