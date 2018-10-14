import cv2
import os
import numpy as np
import json
from qsort import qsort_concept

from clarifai.rest import ClarifaiApp

KEY_MOD = 256
SPACE_KEY = 32
ESC_KEY = 27

json_data = open(os.path.join(os.path.dirname(os.path.realpath('__file__')),"api_keys.json")).read()
api_keys = json.loads(json_data)

appAJ = ClarifaiApp(api_key=api_keys['key1'])
appKs = ClarifaiApp(api_key=api_keys['key2'])
appTZ = ClarifaiApp(api_key=api_keys['key3'])

modelAJ = appAJ.models.get('ASLAlphabet1')
modelKs = appKs.models.get('ASLAlphabet2')
modelTZ = appTZ.models.get('ASLAlphabet3')
text = ""

position_flash = (10,10)
size_flash = (630,460)
rgb_flash = (255,255,255)
thickness_flash = 1000

while(True):
    cam_num = input("How many webcams does your device have? Enter a numerical value: ")
    if int(cam_num) == 0:
        print("Sorry, you need a webcam to use this app!")
        exit()
    elif int(cam_num) == 1:
        cam = cv2.VideoCapture(0)
        break
    elif int(cam_num) == 2:
        cam_choice = input("Which camera would you like to use? front/rear: ")
        if cam_choice == "front":
            cam = cv2.VideoCapture(1)
            break
        elif cam_choice == "rear":
            cam = cv2.VideoCapture(0)
            break
        else:
            print("Enter valid choice")
    else:
        print("Only 1 or 2 webcams are usable.")

translate_output = open("output.txt", "w+")
translate_output.write("Welcome to Sign Language Translator.\n")

dirName = 'images'

try:
    # Create target Directory
    os.mkdir(dirName)
    print("Directory " , dirName ,  " Created.")
except FileExistsError:
    print("Directory " , dirName ,  " already exists.")

imageDir = os.path.join(os.path.dirname(os.path.realpath('__file__')), dirName)

cv2.namedWindow("SL Translator")
cv2.namedWindow("Output")
font = cv2.FONT_HERSHEY_SIMPLEX


while True:
    ret, frame = cam.read()
    height, width, channels = frame.shape
    frame = frame[int(width*1/5):int(width*4/5), int(height*1/5):int(height*4/5)]
    height, width, channels = frame.shape
    img = np.zeros((height,width,3), np.uint8)
    img2 = np.zeros((800,800,3), np.uint8)

    if not ret:
        break
    k = cv2.waitKey(1)

    if k%KEY_MOD == ESC_KEY:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%KEY_MOD == SPACE_KEY:
        # SPACE pressed
        img_name = "opencv_frame.png"
        cv2.imwrite(os.path.join(imageDir, img_name), frame)
        # print("{} written!".format(img_name))

        cv2.rectangle(img, position_flash, size_flash, rgb_flash, thickness_flash)

        clrf_responseAJ = modelAJ.predict_by_filename(os.path.join(imageDir, img_name))
        clrf_responseKs = modelKs.predict_by_filename(os.path.join(imageDir, img_name))
        clrf_responseTZ = modelTZ.predict_by_filename(os.path.join(imageDir, img_name))

        concepts = clrf_responseAJ['outputs'][0]['data']['concepts'] + clrf_responseKs['outputs'][0]['data']['concepts'] + clrf_responseTZ['outputs'][0]['data']['concepts']

        sorted_concepts = qsort_concept(concepts)
        print(sorted_concepts[-1]['id'])
        if sorted_concepts[-1]['id'] == 's':
            text+= " "
        else:
            text+= sorted_concepts[-1]['id']
        translate_output.write(sorted_concepts[-1]['name'])

        os.remove(os.path.join(imageDir, img_name))

        cv2.imshow("SL Translator", img)
        cv2.putText(img2, text, (50, 50), font, 1, (255, 255, 255))
        cv2.imshow("Output", img2)
        cv2.waitKey(500)
    else:
        cv2.imshow("SL Translator", frame)

open("output.txt","w").close
cam.release()
cv2.destroyAllWindows()

'''
for i in range(img_counter):
    file_name = "images/opencv_frame_{}.png".format(i)
    os.remove(file_name)
'''
