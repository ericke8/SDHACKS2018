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
        frame = frame[int(width*1/5):int(width*4/5), int(height*1/5):int(height*4/5)]
        img = np.zeros((height,width,3), np.uint8)


        if not ret:
            break
        k = cv2.waitKey(1)

        if k%256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break
        elif k%256 == 32:
            # SPACE pressed
            img_name = "images/opencv_frame_{}.png".format(img_counter)
            cv2.imwrite(img_name, frame)
            print("{} written!".format(img_name))
            img_counter+=1

            cv2.rectangle(img,(10,10),(630,460),(255,255,255),1000)

            cv2.imshow("test", img)
            cv2.waitKey(1000)


        else:
            cv2.imshow("test", frame)

    cam.release()

    cv2.destroyAllWindows()

    for i in range(img_counter):
        file_name = "images/opencv_frame_{}.png".format(i)
        file_new = "images/Anathan100" + str(i) + ".png"
        os.rename(file_name, file_new)
