income = float(input("Enter your income per year in $: "))

if income >= 30000:
    work_period = int(input("how long have you been working?: "))
    if work_period >= 2:
        print("you qualify for a loan.")
    else:
        print("you do not qualify")

else:
    print("you do not qualify")
