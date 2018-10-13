from clarifai.rest import ClarifaiApp
import os
import json

json_data = open("./api_keys.json")
api_keys = json.loads(json_data)

appAJ = ClarifaiApp(api_key=api_keys['key1']) # Letters A-J
appKT = ClarifaiApp(api_key=api_keys['key2']) # Letters K-T
appUSpace = ClarifaiApp(api_key=api_keys['key3']) # Letters U-Z and space
# model = app.public_models.general_model
# response = model.predict_by_url(url='https://samples.clarifai.com/metro-north.jpg')

# concepts = response['outputs'][0]['data']['concepts']
# for concept in concepts:
#     print(concept['name'], concept['value'])

parentDir = os.fsencode(os.path.join(os.path.dirname(os.path.realpath('__file__')), 'asl_alphabet_train'))

directory = os.fsencode(parentDir)

for file in os.listdir(directory):
    fileName = os.fsdecode(file)
    app.inputs.create_image_from_filename(filename = os.path.join(directory, os.fsencode(fileName[:1] + '_test.jpg')), concepts=[fileName[:1]])
    print(fileName[:1])



appAJ.models.delete_all()
model1 = appAJ.models.create(model_id='ASLAlphabet1', concepts=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'])
# model2 = app.models.create(model_id='ASLAlphabet2', concepts=['F', 'G', 'H', 'I', 'J'])
# model3 = app.models.create(model_id='ASLAlphabet3', concepts=[])
# model4 = app.models.create(model_id='ASLAlphabet4', concepts=['P', 'Q', 'R', 'S', 'T'])
# model5 = app.models.create(model_id='ASLAlphabet5', concepts=['U', 'V', 'W', 'X', 'Y'])
# model6 = app.models.create(model_id='ASLAlphabet6', concepts=['Z', 's'])

model1.train()
# model2.train()
# model3.train()
# model4.train()
# model5.train()
# model6.train()

model1 = appAJ.models.get('ASLAlphabet1')
# model2 = app.models.get('ASLAlphabet2')
# model3 = app.models.get('ASLAlphabet3')
# model4 = app.models.get('ASLAlphabet4')
# model5 = app.models.get('ASLAlphabet5')
# model6 = app.models.get('ASLAlphabet6')

response1 = model1.predict_by_filename(os.path.join(directory,os.fsencode('C_test.jpg')))
# response2 = model2.predict_by_filename(os.path.join(directory,os.fsencode('F_test.jpg')))
# response3 = model3.predict_by_filename(os.path.join(directory,os.fsencode('O_test.jpg')))
# response4 = model4.predict_by_filename(os.path.join(directory,os.fsencode('T_test.jpg')))
# response5 = model5.predict_by_filename(os.path.join(directory,os.fsencode('V_test.jpg')))
# response6 = model6.predict_by_filename(os.path.join(directory,os.fsencode('Z_test.jpg')))

concepts = response1['outputs'][0]['data']['concepts']
for concept in concepts:
    print(concept['name'], concept['value'])

# concepts2 = response2['outputs'][0]['data']['concepts']
# for concept in concepts2:
#     print(concept['name'], concept['value'])

# concepts3 = response3['outputs'][0]['data']['concepts']
# for concept in concepts3:
#     print(concept['name'], concept['value'])

# concepts4 = response4['outputs'][0]['data']['concepts']
# for concept in concepts4:
#     print(concept['name'], concept['value'])

# concepts5 = response5['outputs'][0]['data']['concepts']
# for concept in concepts4:
#     print(concept['name'], concept['value'])

# concepts6 = response6['outputs'][0]['data']['concepts']
# for concept in concepts6:
#     print(concept['name'], concept['value'])
