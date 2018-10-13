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

""" parentDir = os.fsencode(os.path.join(os.path.dirname(os.path.realpath('__file__')), 'asl_alphabet_train'))

directory = os.fsencode(parentDir)

allLetters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 's', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

for file in os.listdir(directory):
    fileName = os.fsdecode(file)
    e = allLetters.index(fileName[:1])
    if fileName[:1] >= 'A' and fileName[:1] <= 'J':
        appAJ.inputs.create_image_from_filename(filename = os.path.join(directory, os.fsencode(fileName[:1] + '_test.jpg')), concepts=[fileName[:1]], not_concepts=(allLetters[:e] + allLetters[(e+1):10]))
        print(fileName[:1])
    if fileName[:1] >= "K" and fileName[:1] <= "S" or fileName[:1] == "s":
        appKs.inputs.create_image_from_filename(filename = os.path.join(directory, os.fsencode(fileName[:1] + '_test.jpg')), concepts=[fileName[:1]], not_concepts=(allLetters[10:e] + allLetters[(e+1):20]))
        print(fileName[:1])
    if fileName[:1] >= "T" and fileName[:1] <= "Z":
        appTZ.inputs.create_image_from_filename(filename = os.path.join(directory, os.fsencode(fileName[:1] + '_test.jpg')), concepts=[fileName[:1]], not_concepts=(allLetters[20:e] + allLetters[(e+1):]))
        print(fileName[:1])

appAJ.models.delete_all()
appKs.models.delete_all()
appTZ.models.delete_all()

modelAJ = appAJ.models.create(model_id='ASLAlphabet1', concepts=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'])
modelKs = appKs.models.create(model_id='ASLAlphabet2', concepts=['K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 's'])
modelTZ = appTZ.models.create(model_id='ASLAlphabet3', concepts=['T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

modelAJ.train()
modelKs.train()
modelTZ.train() """

modelAJ = appAJ.models.get('ASLAlphabet1')
modelKs = appKs.models.get('ASLAlphabet2')
modelTZ = appTZ.models.get('ASLAlphabet3')

position_flash = (10,10)
size_flash = (630,460)
rgb_flash = (255,255,255)
thickness_flash = 1000

cam = cv2.VideoCapture(0)

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
font = cv2.FONT_HERSHEY_SIMPLEX

while True:
    ret, frame = cam.read()
    height, width, channels = frame.shape
    img = np.zeros((height,width,3), np.uint8)


    if not ret:
        break
    k = cv2.waitKey(1)

    if k%KEY_MOD == ESC_KEY:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%KEY_MOD == SPACE_KEY:
        # SPACE pressed
        img_name = "opencv_frame.png" #.format(img_counter)
        cv2.imwrite(os.path.join(imageDir, img_name), frame)
        print("{} written!".format(img_name))

        cv2.rectangle(img, position_flash, size_flash, rgb_flash, thickness_flash)

        clrf_responseAJ = modelAJ.predict_by_filename(os.path.join(imageDir, img_name))
        clrf_responseKs = modelKs.predict_by_filename(os.path.join(imageDir, img_name))
        #clrf_responseTZ = modelTZ.predict_by_filename(os.path.join(imageDir, img_name))
        #TODO: train TZ set because it got deleted

        concepts = clrf_responseAJ['outputs'][0]['data']['concepts'] + clrf_responseKs['outputs'][0]['data']['concepts'] # + clrf_responseTZ['outputs'][0]['data']['concepts']

        sorted_concepts = qsort_concept(concepts)
        print(sorted_concepts)
        translate_output.write(sorted_concepts[-1]['name'])

        os.remove(os.path.join(imageDir, img_name))

        cv2.imshow("SL Translator", img)
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