from math import sqrt

print("pythagoras calculator")
print("Assume sides are named a, b, and c. c being the hypotenuse")
pythagoras = input("which side are you calculating? side> ")

if pythagoras == "a":
    side_b = int(input("input length of b > "))
    side_c = int(input("input length of c > "))

    side_a = sqrt((side_c**2) - (side_b**2))

    print("a = ")
    print(side_a)

elif pythagoras == "b":
    side_a = int(input("input length of a > "))
    side_c = int(input("input length of c > "))

    side_b = sqrt(side_c**2 - side_a**2)

    print("b = ")
    print(side_b)

elif pythagoras == "c":
    side_a = int(input("input length of a > "))
    side_b = int(input("input length of b > "))

    side_c = sqrt(side_a**2 + side_b**2)

    print("c = ")
    print(side_c)

else: print("either a, b or c my guy")

