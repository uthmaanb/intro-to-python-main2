
usernames = ["Uthmaan", "Abdul", "Cassiem", "Zaid", "Gideon", "Aaliyah"]
passwords = ["Polonykop100", "abdul360", "cassiemisthebest", "0000", "binary101", "5555"]

userinput = input("What is your username?: ")
passinput = input("What is your password?: ")
found = False

for x in range(len(usernames)):
    if userinput == usernames[x] and passinput == passwords[x]:
        found = True

if found == True:
    print("Welcome Madam/Sir!")

else:
    print("Access Denied!!!")
