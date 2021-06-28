grade = float(input("Enter your Grade in %: "))

if grade >= 90:
    print("Your grade is A")

else:
    if grade >= 80:
        print("Your grade is B")

    else:
        if grade >= 70:
            print("Your grade is C")

        else:
            if grade >= 60:
                print("Your grade is D")

            else:
                if grade >= 50:
                    print("Your grade is E")

                else:
                    if grade < 50:
                        print("Your grade is F")
