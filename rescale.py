# Rescaling and Resizing Images and Video frames in OpenCV
# To prevent computational overhead, we can rescale images and video frames.
import cv2 as cv

img = cv.imread("Photos/cat.jpg")
cv.imshow("Cat", img)


def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)  # Rescale width
    height = int(frame.shape[0]*scale)  # Rescale height
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


resized_image = rescaleFrame(img, scale=0.2)  # Rescales the image
cv.imshow("Rescaled Cat", resized_image)  # Displays the rescaled image


def ChangeRes(width, height):
    # Live video capture object
    # Changes the resolution of the video capture object
    capture.set(3, width)  # Width
    capture.set(4, height)  # Height


# Reading Videos in OpenCV
capture = cv.VideoCapture("Videos/Dogvideo.mp4")

while True:
    isTrue, frame = capture.read()  # Reads the video frame by frame

    if not isTrue:
        break
    cv.imshow("Video", frame)
    cv.imshow("Rescaled Video", rescaleFrame(frame, scale=0.2))

    if cv.waitKey(20) & 0xFF == ord('d'):  # Waits for 'd' key to be pressed
        break

capture.release()  # Releases the video capture object
cv.destroyAllWindows()  # Closes all OpenCV windows
cv.waitKey(0)
