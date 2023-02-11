#RGB To BGR

import cv2

image = cv2.imread("Tiger.jpg")

# converting RGB to BGR

image_rgb = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

cv2.imshow('image', image_rgb)

cv2.waitKey(0)

cv2.destroyAllWindows()

#RGB To GRAY_SCALE

import cv2

image = cv2.imread("Tiger.jpg")

# converting RGB to GRAY

image_rgb = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

cv2.imshow('image', image_rgb)

cv2.waitKey(0)

cv2.destroyAllWindows()

#RGB To HSV

import cv2

image = cv2.imread("Tiger.jpg")

# converting RGB to HSV

image_rgb = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)

cv2.imwrite("hsv_tiger.jpg",image_rgb)

cv2.imshow('image', image_rgb)

cv2.waitKey(0)

cv2.destroyAllWindows()

#RGB To YUV

import cv2

image = cv2.imread("tiger.jpg")

# converting RGB To YUV

image_rgb = cv2.cvtColor(image, cv2.COLOR_RGB2YUV)

cv2.imshow('image', image_rgb)

cv2.waitKey(0)

cv2.destroyAllWindows(
