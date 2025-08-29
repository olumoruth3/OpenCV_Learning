import cv2 as cv
import numpy as np
# Drawing shapes and Puttig text on images
# Create a blank image (500x500 pixels, 3 color channels)
blank = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow("Blank", blank)

# 1. Paint the image a certain color
blank[200:300, 300:400] = 0, 255, 0  # Paints the image green
# You can color a certain portion of the image by specifying the coordinates
# blank[200:300, 300:400]
cv.imshow("Green", blank)

# 2. Draw a rectangle
# cv.rectangle(blank, (0, 0), (250, 250), (0, 255, 0),
#              thickness=-1)  # thickness=-1 fills the rectangle, thickness=2 draws only the border,thickness= cv.FILLED also fills the rectangle
# Instead of specifying the actual values of the coordinates, you can also use variables
cv.rectangle(
    blank, (0, 0), (blank.shape[1]//2, blank.shape[0]//2), (255, 0, 0), thickness=cv.FILLED)
cv.imshow("Rectangle", blank)

# 3. Draw a circle
# (image, center, radius, color, thickness)
cv.circle(blank, (250, 250), 40, (0, 0, 255), thickness=3)
# Setting thickness=-1 fills the circle
cv.imshow("Circle", blank)

# 4. Draw a line
# (image, start_point, end_point, color, thickness)
cv.line(blank, (0, 0), (500, 500), (255, 255, 255), thickness=3)
cv.imshow("Line", blank)

# 5. Write text on the image
# (image, text, start_point, font, font_scale, color, thickness)

cv.putText(blank, "Hello, my name is Elliot, you've been hacked", (0, 225), cv.FONT_HERSHEY_SIMPLEX,
           0.6, (0, 255, 0), thickness=1)
cv.imshow("Text", blank)

cv.waitKey(0)
cv.destroyAllWindows()  # Closes all OpenCV windows when any key is pressed
