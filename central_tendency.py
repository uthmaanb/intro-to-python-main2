import numpy as np
from scipy import stats  # used to find mode coz theres no mode in numpy
import matplotlib.pyplot as plt  # to generate a graphical graph


marks = [100, 72, 82, 90, 90, 69, 19, 70, 150, 45, 5]
names = ['uthmaan', 'thabo', 'thando', 'gideon', 'moses', 'elon', 'zaid', 'aaliyah', 'cassiem', 'Abdul-malik', 'gary']

# my_mean = np.mean(marks)
# print(my_mean)
#
# my_mode = stats.mode(marks)
# print(my_mode)
#
# my_med = np.median(marks)
# print(my_med)
#
# my_range = np.ptp(marks)
# print(my_range)
#
# my_interq = np.percentile(marks, (25, 50, 75))
# print(my_interq)
#
# my_var = np.var(marks)
# print(my_var)


# x_pos = [i for i, _ in enumerate(names)]  # labels on the x-axis
# # labeling and visuals
# plt.bar(x_pos, marks, color='green')
# plt.xlabel("Students")
# plt.ylabel("Marks in percentage")
# plt.title("MARKS")
# plt.xticks(x_pos, names)
# # plt.show()

marks2 = np.array([70, 45, 90, 12])
names2 = np.array(['memphis', 'godwin', 'thando', 'thabo'])
plt.hist(names, marks)
plt.axes().set_aspect("equal")
plt.xlabel("Students")
plt.ylabel("Marks in percentage")
plt.title("MARKS")
plt.show()


# sizes = [25, 20, 45, 10, 26]
# labels = ["Cats", "Dogs", "Tigers", "Goats", 'Children']
# plt.pie(sizes, labels=labels, autopct="%.0f")  # float and percentage value
# # plt.axes().set_aspect("equal")  # auto # num # aspect ratio
# plt.show()


# y = np.array([35, 25, 25, 15])
#
# plt.pie(y)
# plt.show()


x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6]
y = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

slope, intercept, r, p, std_err = stats.linregress(x, y)


def myfunc(a):
    return slope * a + intercept


mymodel = list(map(myfunc, x))

plt.subplot(122)
plt.scatter(x, y)
plt.plot(x, mymodel)


sizes = [25, 20, 45, 10, 26]
labels = ["Cats", "Dogs", "Tigers", "Goats", 'Children']
plt.subplot(121)
plt.pie(marks, labels=names, autopct="%.0f")  # float and percentage value

# plt.subplot(122)
plt.boxplot(marks)
plt.show()
