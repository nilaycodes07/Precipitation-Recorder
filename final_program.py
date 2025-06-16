import cv2
import time
import os

def TakePic(cam, picNum):
    output_directory = "/Users/User/Documents/Precipitation Recorder/image_captures"
    imgName = "capture_image_" + str(picNum) + ".jpg" #str
    output_path = os.path.join(output_directory, imgName)

    for _ in range(5):
        cam.read()
        time.sleep(0.1)

    result, image = cam.read()
    if result:
        cv2.imwrite(output_path, image)
        print("Image captured and saved as " + imgName)
    else:
        print("Failed to capture image")

cam = cv2.VideoCapture(0)
if not cam.isOpened():
    raise IOError("Cannot open webcam")

picNum = 0 #int
try: 
    while True:
        TakePic(cam, picNum)
        print("picture attempt completed")
        time.sleep(5)
        picNum += 1
except KeyboardInterrupt:
        print("Stopping...")
finally:
    cam.release()
    cv2.destroyAllWindows()