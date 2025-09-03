#  How to switch between different color spaces in OpenCV
# Color spaces are different ways of representing the color of an image.
# The most common color space is BGR (Blue, Green, Red) which is used by OpenCV by default.
# Other color spaces include Grayscale, HSV (Hue, Saturation, Value), LAB (Lightness, A, B), and many more.
# Each color space has its own advantages and disadvantages, and some color spaces are better suited for certain tasks than others.
# For example, the HSV color space is often used for color-based segmentation because it separates the color information (hue) from the intensity information (value).
# This makes it easier to identify and isolate specific colors in an image. The LAB color space is often used for color correction and color balancing because it is designed to be more perceptually uniform than other color spaces.
# This means that small changes in color are more consistent across the entire color space, making it easier to adjust the colors in an image.
# In this tutorial, we will learn how to switch between different color spaces in OpenCV using  the cvtColor() function.
# The cvtColor() function takes two arguments: the source image and the color space conversion code.
# The color space conversion code is a constant that specifies the type of conversion to be performed.
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("Photos/RuthImage1.jpg")
cv.imshow("Original", img)

# plt.imshow(img)
# plt.show()

# Convert BGR to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

# Convert BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow("HSV", hsv)


# Convert BGR to LAB
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow("LAB", lab)
# Convert BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow("RGB", rgb)

plt.imshow(rgb)
plt.show()

# we can invert the colorspaces back to BGR
# Convert HSV to BGR
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow("HSV to BGR", hsv_bgr)
# You cannot convert lab to bgr, or hsv to lab directly. You have to convert it to rgb first

cv.waitKey(0)
cv.destroyAllWindows()
