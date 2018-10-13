from clarifai.rest import ClarifaiApp

app = ClarifaiApp(api_key='b6fdc0bdb31847798c3568d6922aa2c8')
model = app.public_models.general_model
response = model.predict_by_url(url='https://samples.clarifai.com/metro-north.jpg')

concepts = response['outputs'][0]['data']['concepts']
for concept in concepts:
    print(concept['name'], concept['value'])

#app.inputs.create_image_from_url(url='https://samples.clarifai.com/puppy.jpeg', concepts=['A'])