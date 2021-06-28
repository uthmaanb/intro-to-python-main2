import numpy as np
import matplotlib.pyplot as plt  # to generate a graphical graph


nums = [0.5, 0.7, 1.0, 1.2, 1.3, 2.1, 3.1, 3.2, 3.3, 3.4, 3.5]
bins = [0, 1, 2, 3, 4]
plt.hist(nums, bins)
plt.xlabel("nums")
plt.ylabel("bins")
plt.title("Histogram of nums against bins")
plt.show()


list1 = np.arange(1, 21)
print(list1)
print(np.mean(list1))
print(np.std(list1))
print(np.var(list1))
