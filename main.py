from clarifai.rest import ClarifaiApp
import os

app = ClarifaiApp(api_key='b6fdc0bdb31847798c3568d6922aa2c8')
# model = app.public_models.general_model
# response = model.predict_by_url(url='https://samples.clarifai.com/metro-north.jpg')

# concepts = response['outputs'][0]['data']['concepts']
# for concept in concepts:
#     print(concept['name'], concept['value'])

parentDir = os.path.dirname(os.path.realpath('__file__'))

app.inputs.create_image_from_filename(filename= os.path.join(parentDir,'asl_alphabet_test/A_test.jpg'), concepts=['A'])
app.inputs.create_image_from_filename(filename= os.path.join(parentDir,'asl_alphabet_test/B_test.jpg'), not_concepts=['A'])
app.models.delete_all()
model = app.models.create(model_id="ASLAlphabet", concepts=["A"])
model.train()
model = app.models.get('ASLAlphabet')
response = model.predict_by_filename(os.path.join(parentDir,'asl_alphabet_test/C_test.jpg'))
concepts = response['outputs'][0]['data']['concepts']
for concept in concepts:
    print(concept['name'], concept['value'])
