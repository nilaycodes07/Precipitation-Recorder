import cv2

cam = cv2.VideoCapture(0)

if not cam.isOpened():
    raise IOError("Cannot open webcam")

result, image = cam.read()

if result:
    cv2.imwrite("capture_image.jpg", image)
    print("Image captured and saved as captured_image.jpg")

cam.release()
cv2.destroyAllWindows()