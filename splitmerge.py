# How to split and merge color channels in OpenCV
# A color image is made up of three color channels: Red, Green, and Blue (RGB).
# Each channel is a grayscale image that represents the intensity of that color in the image.
# OpenCV allows us to split an image into its individual color channels using the split() function.
# The split() function takes an image as input and returns a list of the individual color channels

import cv2 as cv
import numpy as np

img = cv.imread("Photos/maasai.jpg")
cv.imshow("Original", img)

blank = np.zeros(img.shape[:2], dtype='uint8')

b, g, r = cv.split(img)  # Split the image into its individual color channels

# Create an image with only the blue channel
blue = cv.merge([b, blank, blank])
# Create an image with only the green channel
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])  # Create an image with only the red channel

cv.imshow("Blue", blue)
cv.imshow("Green", green)
cv.imshow("Red", red)

print(img.shape)  # (height, width, channels)
print(b.shape)    # (height, width) - single channel
print(g.shape)    # (height, width) - single channel
print(r.shape)    # (height, width) - single channel

# Merge the individual color channels back into a single image
merged = cv.merge([b, g, r])
cv.imshow("Merged", merged)

cv.waitKey(0)
cv.destroyAllWindows()
