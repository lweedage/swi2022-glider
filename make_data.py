import numpy as np
import matplotlib.pyplot as plt

vertical_length = 10
horizontal_length = 30

center_point = [0, 0]
center_x = []
center_y = []

data = []

number_of_iterations = 100
for i in range(number_of_iterations):
    center_x.append(center_point[0])
    center_y.append(center_point[1])

    center_point[0] += np.random.normal(0, 0.4)
    center_point[1] += np.random.normal(0, 1)

    x1, y1 = 

    data.append()

plt.plot(center_x, center_y)
plt.show()