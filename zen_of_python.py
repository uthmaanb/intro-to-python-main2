

# def long_word(name_of_file):
with open("zen.txt", "r") as reader:
    list_words = reader.read().split()
    fnd_long = max(list_words, key=len)
    print(fnd_long)
