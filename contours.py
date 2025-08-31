# Contour detection - How to identify contours in an image
# Contours can be explained simply as a curve joining all the continuous points (along the boundary), having same color or intensity.
# The contours are a useful tool for shape analysis and object detection and recognition.
import cv2 as cv
import numpy as np

img = cv.imread("Photos/maasai.jpg")
cv.imshow("Original", img)

# Create a blank image for drawing the contours later
blank = np.zeros(img.shape, dtype='uint8')
cv.imshow("Blank", blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY  # Attempt to convert the image to a binary image
                           # 125 is the threshold value, 255 is the max value to use with the THRESH_BINARY.
                           )
cv.imshow("Thresholded", thresh)
# blur = cv.GaussianBlur(gray, (7, 7), cv.BORDER_DEFAULT)

# canny = cv.Canny(blur, 125, 175)
# cv.imshow("Canny Edges", canny)

# returns a list of all the contours found in the image
contours, hierarchies = cv.findContours(
    thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
# cv.RETR_LIST retrieves all of the contours without establishing any hierarchical relationships.
# (image, mode, method)
# cv.chain_approx_none stores all the points of the contours. Other method is cv.CHAIN_APPROX_SIMPLE which removes all redundant points and compresses the contour, thereby saving memory.
print(f'{len(contours)} contours found!')

cv.drawContours(blank, contours, -1, (0, 0, 255),
                2)  # -1 means draw all contours
# (image to draw on, contours, contour index to draw (-1 means draw all), color, thickness)
cv.imshow("Contours Drawn", blank)
cv.waitKey(0)
cv.destroyAllWindows()
