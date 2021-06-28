# def create_dictionary(clean_word_list):
#     word_count = {}
#     f = open("filename.txt", "w")
#     for word in clean_word_list:
#         if word in word_count:
#             word_count[word] += 1
#         else:
#             word_count[word] = 1
#     for key, value in sorted(word_count.items(), key=operator.itemgetter(1)):
#         print(key, value)
#         f.write('{} {}'.format(key, value))
#     f.close()

details = {'Name': " Alice",
           'Age': 21,
           'Degree': " Bachelor Cse",
           'University': " Northeastern Univ"}

with open("myfile.txt", 'w') as f:
    for key, value in details.items():
        f.write('%s:%s\n' % (key, value))
