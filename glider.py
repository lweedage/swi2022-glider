import math
import numpy as np
import pickle
import matplotlib.pyplot as plt

#data = pickle.load(open('data.p', 'wb'))

dat = [[[np.random.uniform(0.0, 1.0), np.random.uniform(0.0, 1.0)] for i in range(4)]]

for k in range(200):
    newp = [[0,0],[0,0],[0,0],[0,0]]
    for j in range(4):
        newp[j][0] = dat[-1][j][0] + np.random.uniform(-0.05, 0.05)
        newp[j][1] = dat[-1][j][1] + np.random.uniform(-0.05, 0.05)  #+ [[np.random.uniform(-0.1, 0.1), np.random.uniform(-0.1, 0.1)] for i in range(2)]
    dat.append(newp)

t = range(1,len(dat)+1)

data = dat
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

    angle = math.atan((y1-y2)/(x1-x2))  # this is the angle with respect to the horizon (positive x-axis)

    height = vertical_length/vertical_line_length
    directions.append(height)
    #relative_height.append(relative_height)

    left_wing_length = math.sqrt((x3-x_center)**2 + (y3-y_center)**2)
    right_wing_length = math.sqrt((x4-x_center)**2 + (y4-y_center)**2)

#print(center_points)
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

xc, yc = cpoints
xvf, yvf = vf
xvb, yvb = vb

xhl, yhl = hl
xhr, yhr = hr

print(xvf)
Nshow = 20
for k in range(Nshow):
    xval = [xvf[k],xvb[k]]
    yval = [yvf[k],yvb[k]]
    xval2 = [xhl[k],xhr[k]]
    yval2 = [yhl[k],yhr[k]]
    plt.plot(xval,yval,'k-')
    plt.plot(xval2,yval2,'k-')
    plt.show()

plt.plot(t,xc)
plt.show()

plt.plot(t,yc)
plt.show()

plt.plot(t,vlength)
plt.show()

plt.plot(t,hlength)
plt.show()

