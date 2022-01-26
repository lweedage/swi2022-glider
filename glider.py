import math
from msilib.schema import ListView
import numpy as np
import pickle
import seaborn as sns
import matplotlib.pyplot as plt

data = pickle.load(open('data_points-paddle4-zoom75.p', 'rb'))

fnd = False
ind = 0

print('datapunt: ', data[40])
t = list(range(1,len(data)+1))


# clean data
for k in range(len(data)):
    if data[k][0] == [0,0]:
        if k+1 != len(data) and data[k+1][0] != [0,0]:
            data[k] = (np.add(data[k-1],data[k+1]))/2
        else:
            data[k] = data[k-1]

    rem = False
    if k > 0:
        for j in range(4):
            print(np.linalg.norm(np.subtract(data[k][j], data[k-1][j])))
            if np.linalg.norm(np.subtract(data[k][j], data[k-1][j])) > 200:
                rem = True
    
    if rem:
        data[k] = data[k-1]

ma_data = np.copy(data)
for k in range(len(data)):
    ma_data[k] = np.sum(data[k:k+30],axis=0)/30

data = ma_data

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
hlength = []
vlength = []
vf = []
vb = []
hl = []
hr = []
alphavec = []
contrvec = []

ind = 0
LV = 7
LH = 18
K = LH/LV


for vertical_back, vertical_front, horizontal_left, horizontal_right in data:

    x1, y1 = vertical_back
    x2, y2 = vertical_front
    x3, y3 = horizontal_left
    x4, y4 = horizontal_right

    vf.append(vertical_front)
    vb.append(vertical_back)
    hl.append(horizontal_left)
    hr.append(horizontal_right)

    # center coordinates
    x_center, y_center = find_intersection(x1, y1, x2, y2, x3, y3, x4, y4)

    center_points.append((x_center, y_center))

    # append vertical and horizontal length
    vertical_length = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    vlength.append(vertical_length)

    horizontal_length = math.sqrt((x3-x4)**2 + (y3-y4)**2)
    hlength.append(horizontal_length)

    ex_horiz_length = K*vertical_length
    horiz_contr = horizontal_length/ex_horiz_length
    contrvec.append(horiz_contr)
    angle = math.atan((y1-y2)/(x1-x2))  # this is the angle with respect to the horizon (positive x-axis)

    m1 = (y2-y1)/(x2-x1)
    m2 = (y4-y3)/(x4-x3)
    alpha = np.arctan(abs((m2-m1)/(1+m1*m2)))
    alphavec.append(alpha)
    height = vertical_length/vertical_line_length
    directions.append(height)
    #relative_height.append(relative_height)

    left_wing_length = math.sqrt((x3-x_center)**2 + (y3-y_center)**2)
    right_wing_length = math.sqrt((x4-x_center)**2 + (y4-y_center)**2)

    ind += 1

# collect data
cpoints = np.array(center_points)
cpoints = cpoints.T

vf = np.array(vf)
vf = vf.T

vb = np.array(vb)
vb = vb.T

hl = np.array(hl)
hl = hl.T

hr = np.array(hr)
hr = hr.T

# set center, left, right points
xc, yc = cpoints

xvf, yvf = vf
xvb, yvb = vb

xhl, yhl = hl
xhr, yhr = hr

# heatmap
xedges = np.linspace(-2,2.1,22)
yedges = np.linspace(-2,2.1,22)
fig, ax = plt.subplots()
h = plt.hist2d(xc, yc, bins=(10, 10))
fig.colorbar(h[3], ax=ax)
plt.title('Heatmap of glider position')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

plt.plot(xc,yc)
plt.show()

# x center trajectory
plt.plot(t,xc)
plt.title('Center of glider trajectory')
plt.xlabel('t')
plt.ylabel('x center')
plt.show()

# y center trajectory
plt.plot(t,yc)
plt.title('Center of glider trajectory')
plt.xlabel('t')
plt.ylabel('y center')
plt.show()

# angle on cross
plt.plot(t,alphavec)
plt.title('Center of glider trajectory')
plt.xlabel('t')
plt.ylabel('alpha')
plt.show()

# contraction
plt.plot(t,contrvec)
plt.title('Contraction of glider')
plt.xlabel('t')
plt.ylabel('Contraction')
plt.show()
