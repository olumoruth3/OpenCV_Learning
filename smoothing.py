# Smoothing and blur techniques in OpenCV
#  we generally smooth an image to reduce noise and improve the quality of the image.

# A kernel is a window that you draw over a specific part of an image and apply a mathematical operation to it.
# The kernel is usually a small matrix (e.g., 3x3, 5x5) that is moved across the image, pixel by pixel.
# The values in the kernel matrix determine how the pixels in the image are weighted during the operation

# Blur is applied to the middle pixel of the kernel as a result of the surrounding pixels.
import cv2 as cv

img = cv.imread("Photos/RuthImage1.jpg")
cv.imshow("Original", img)

# Methods of blurring
# 1. Averaging - the pixel value is replaced by the average of the pixel values in the kernel area.

average = cv.blur(img, (3, 3))
# (3,3) is the kernel size. The higher the kernel size the more the blur
cv.imshow("Averaging Blur", average)

# 2. Gaussian Blur - The kernel is a Gaussian function. The result is a weighted average of the pixel values in the kernel area.
# The center pixel is given more weight than the surrounding pixels.
gauss = cv.GaussianBlur(img, (3, 3), 0)
cv.imshow("Gaussian Blur", gauss)

# 3. Median Blur - The pixel value is replaced by the median of the pixel values in the kernel area.
# This is particularly effective for removing "salt and pepper" noise from an image.
median = cv.medianBlur(img, 3)
cv.imshow("Median Blur", median)

# 4. Bilateral  blurring - This method is more advanced and preserves edges while reducing noise.
bilateral = cv.bilateralFilter(img, 10, 15, 15)
# (image, diameter of each pixel neighborhood, sigmaColor, sigmaSpace)
cv.imshow("Bilateral Blur", bilateral)

cv.waitKey(0)
cv.destroyAllWindows()
