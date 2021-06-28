gas = 45  # in litres
while gas > 0:
    print("VROOOM!!")
    gas = gas - 1

    if gas == 40:  # On a reserve. Cannot use
        print("no more fuel")
        continue
