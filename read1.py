import cv2 as cv
# Reading Images in OpenCV
img = cv.imread("Photos/cat.jpg")

cv.imshow("Cat", img)
cv.waitKey(0)

# Reading Videos in OpenCV
capture = cv.VideoCapture("Videos/Dogvideo.mp4")

while True:
    isTrue, frame = capture.read()  # Reads the video frame by frame

    if not isTrue:
        break  # Breaks the loop if no frame is read

    cv.imshow("Video", frame)  # Displays the current frame

    if cv.waitKey(20) & 0xFF == ord('d'):  # Waits for 'd' key to be pressed
        break
capture.release()  # Releases the video capture object
cv.destroyAllWindows()  # Closes all OpenCV windows
cv.waitKey(0)
