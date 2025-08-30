# The most basic functions in opencv that are used with images
# Reading, displaying, resizing, cropping, converting to grayscale, blurring, edge cascade, dilating, eroding
import cv2 as cv

ruth = cv.imread('Photos/RuthImage1.jpg')
img = cv.imread('Photos/maasai.jpg')

# cv.imshow('Ruth', ruth)
# cv.imshow('Cat', img)


def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)  # Rescale width
    height = int(frame.shape[0]*scale)  # Rescale height
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


resized_image = rescaleFrame(img, scale=1)  # Rescales the image
cv.imshow("Rescaled Cat", resized_image)  # Displays the rescaled image

# 1. Converting to grayscale
gray = cv.cvtColor(resized_image, cv.COLOR_BGR2GRAY)
# gray1 = cv.cvtColor(ruth, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray Ruth', gray1)
cv.imshow('Gray', gray)

# 2. Blur
# To increase the blur effect increase the kernal size. Must be odd numbers
blur = cv.GaussianBlur(resized_image, (7, 7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# 3. Edge Cascade
# Lower the values the more edges you get
# canny = cv.Canny(resized_image, 150, 175)
# cv.imshow('Canny Edges', canny)
# To reduce the number of edges detected, blur the image first then do canny
canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', canny)

# 4. Dilating the image
dilated = cv.dilate(canny, (7, 7), iterations=3)
cv.imshow('Dilated', dilated)

# 5. Eroding the image
eroded = cv.erode(dilated, (7, 7), iterations=3)
cv.imshow('Eroded', eroded)

# 6. Resizing an image
resized = cv.resize(ruth, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# 7. Cropping an image
cropped = ruth[200:400, 300:400]    # Crops from y1:y2, x1:x2
cv.imshow('Cropped', cropped)

cv.waitKey(0)
cv.destroyAllWindows()
