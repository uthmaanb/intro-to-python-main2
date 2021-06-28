import time

# create function for sorting
start = time.time()
def quick_sort(sequence):  # pass in sequence name
    length = len(sequence)  # variable for sequence name
    # return the sequence if there is 1 or 0 values
    if length <= 1:
        return sequence
    # otherwise bring out the last value
    else:
        pivot = sequence.pop()

    # create 2 lists for items greater than and lower than the pivot number
    items_greater = []
    items_lower = []

    # if the item selected is greater than the pivot number, put it in items_greater
    for item in sequence:
        if item > pivot:
            items_greater.append(item)

        # otherwise if it is lower put it in items_lower
        else:
            items_lower.append(item)

    # then return an array with lower items, pivot number and greater items. and perform the function on created lists
    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)


# print function with list
print(quick_sort([42, 12, 13, 89, 63, 11]))
end = time.time()
print(end-start)
