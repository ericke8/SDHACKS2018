import cv2
from datetime import datetime
import os
import time
import numpy as np



def startCam():
    cam = cv2.VideoCapture(1)

    currentTime = datetime.now()


    cv2.namedWindow("test")

    img_counter = 0
    font = cv2.FONT_HERSHEY_SIMPLEX


    while True:
        ret, frame = cam.read()
        height, width, channels = frame.shape
        img = np.zeros((height,width,3), np.uint8)


        if not ret:
            break
        k = cv2.waitKey(1)

        if k%256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break
        elif (datetime.now() - currentTime).total_seconds() >= 2:
            # SPACE pressed
            img_name = "images/opencv_frame_{}.png".format(img_counter)
            cv2.imwrite(img_name, frame)
            print("{} written!".format(img_name))
            img_counter+=1
            currentTime = datetime.now()


        else:
            cv2.imshow("test", frame)

    cam.release()

    cv2.destroyAllWindows()

    for i in range(img_counter):
        file_name = "images/opencv_frame_{}.png".format(i)
        os.remove(file_name)
