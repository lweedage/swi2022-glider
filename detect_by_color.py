import cv2
import numpy as np

img = cv2.imread('paddle4/frame0011.jpg')

scale_percent = 35  # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)

# resize image
resized_img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
img_gray = cv2.cvtColor(resized_img, cv2.COLOR_BGR2GRAY)

lower = np.uint8([150, 230, 150])
upper = np.uint8([255, 255, 255])
white_mask = cv2.inRange(resized_img, lower, upper)
img_mask = cv2.medianBlur(white_mask, 7)

cv2.imshow("mask",img_mask)
cv2.waitKey(0)

seed = (10, 10)
cv2.floodFill(img_mask, None, seedPoint=seed, newVal=(255, 255, 255), loDiff=(5, 5, 5, 5), upDiff=(5, 5, 5, 5))

result = resized_img.copy()
img = cv2.bitwise_not(img_mask)

contours, hierarchy = cv2.findContours(image=img, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)
image_copy = img.copy()
print(contours)
cv2.drawContours(image=image_copy, contours=contours, contourIdx=-1, color=(0,0,255), thickness=3, lineType=cv2.LINE_AA)
cv2.imshow("contour",image_copy)
cv2.waitKey(0)


lines = cv2.HoughLinesP(img,1,np.pi/180,100, minLineLength = 0, maxLineGap=10)
for x1,y1,x2,y2 in lines[0]:
    print(x1, y1, x2, y2)
    cv2.line(result,(x1,y1),(x2,y2),(255,0,0),1)

cv2.imshow("linesDetected", result)
cv2.waitKey(0)