import numpy as np
import matplotlib.pyplot as plt


# x = np.array([1, 1, 5, 5, 1])
# y = np.array([1, 5, 5, 1, 1])

# y = np.arange(0, 5)
# x = np.array([a*a+2 for a in y])
# y2 = [0, 1, 2, 3]
# x2 = [i+1 for i in y2]

# lines = plt.plot(x, y, 'r--', x2, y2, 'b:')
# print(lines)
# plt.setp(lines, linestyle='-.')
plt.grid()
img = plt.imread('Дерево.png')
d = np.array([[1, 0]*10, [0, 1]*10]*10)
print(d)
plt.imshow(img)
plt.colorbar()
plt.show()