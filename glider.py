import math
import numpy as np
import pickle
import matplotlib.pyplot as plt


data = pickle.load(open('data.p', 'wb'))

def find_intersection(x1, y1, x2, y2, x3, y3, x4, y4):
    x_c = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / (
                (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4))
    y_c = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / (
                (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4))
    return (x_c, y_c)

vertical_line_length = 10
relative_height = []
directions = []
center_points = []

for vertical_back, vertical_front, horizontal_left, horizontal_right in data:
    x1, y1 = vertical_back
    x2, y2 = vertical_front
    x3, y3 = horizontal_left
    x4, y4 = horizontal_right

    x_center, y_center = find_intersection(x1, y1, x2, y2, x3, y3, x4, y4)
    center_points.append(x_center, y_center)

    vertical_length = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    angle = math.atan((y1-y2)/(x1-x2))  # this is the angle with respect to the horizon (positive x-axis)
    directions.append(height)

    height = vertical_length/vertical_line_length
    relative_height.append(relative_height)

    horizontal_length = math.sqrt((x3-x4)**2 + (y3-y4)**2)
    left_wing_length = math.sqrt((x3-x_center)**2 + (y3-y_center)**2)
    right_wing_length = math.sqrt((x4-x_center)**2 + (y4-y_center)**2)

fig, ax = plt.subplots()
plt.imshow(str('vid2img/paddle-4-frame-' + str(0) + '.jpg'))
plt.show()

