ages = [2, 12, 12, 14, 15, 16, 16, 17, 18, 14, 20, 20]

ages2 = set(ages)
print(list(ages2))
print("highest number: ", max(ages2))


ages = [2, 12, 12, 14, 15, 16, 16, 17, 18, 14, 20, 20]
ages1 = [2, 4, 12, 14, 15, 16, 16, 17, 18, 14, 20, 20]

print(any(x in ages for x in ages1))


the_list = input("List your numbers: ")
tupled_list = tuple(the_list)
print("Your list", tupled_list)
print("highest number:", max(tupled_list))
print("Lowest number: ", min(tupled_list))
print("the_list: ", the_list)
print("tupled_list: ", tupled_list)
