# Image Transformations
# transformations include resizing, rotating, translating (shifting), and flipping images

import cv2 as cv
import numpy as np

img = cv.imread("Photos/maasai.jpg")
ruth = cv.imread('Photos/RuthImage1.jpg')
cv.imshow("Ruth", ruth)
cv.imshow("Original", img)

# 1. Translation - shifting the image along the x and y axis (up, down, left, right)


def translate(img, x, y):  # x is right, y is down. x and y stand for the number of pixels you want to shift
    transMat = np.float32([[1, 0, x], [0, 1, y]])  # Transformation matrix
    dimensions = (img.shape[1], img.shape[0])  # width, height
    return cv.warpAffine(img, transMat, dimensions)


# -x = left and +x = right
# -y = up and +y = down
# Shift the image 100 pixels right and 100 pixels down
translated = translate(img, 100, 100)
cv.imshow("Translated", translated)

# 2. Rotation - rotating the image around a certain point by a certain angle


def rotate(image, angle, rotPoint=None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)  # 1.0 is the scale
    dimensions = (width, height)
    return cv.warpAffine(image, rotMat, dimensions)


rotated = rotate(img, -45)  # Rotate 45 degrees clockwise
cv.imshow("Rotated", rotated)

rotated_rotated = rotate(rotated, -45)  # Rotate another 45 degrees clockwise
cv.imshow("Rotated Twice", rotated_rotated)

# Rotate 45 degrees counter clockwise around the top left corner (0,0)
rotated_rotated_rotated = rotate(img, 45, (0, 0))
cv.imshow("Rotated around top left corner", rotated_rotated_rotated)

# 3. Resizing
resized = cv.resize(img, (600, 600), interpolation=cv.INTER_CUBIC)
cv.imshow("Resized", resized)

# 4. Flipping - 0 means flipping around the x axis, 1 means flipping around y axis, -1 means flipping around both axes
flipped = cv.flip(ruth, 1)
cv.imshow("Flipped", flipped)

# 5. Cropping
cropped = ruth[200:400, 300:400]    # Crops from y1:y2, x1:x2
cv.imshow("Cropped", cropped)

cv.waitKey(0)
cv.destroyAllWindows()
