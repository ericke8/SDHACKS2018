import webapp2
import json
import os
import jinja2
import datetime
import time
import math
import logging
from google.appengine.ext import ndb
from google.appengine.api import users
from google.appengine.ext import vendor

vendor.add('lib')

from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage
from clarifai.rest import Video as ClVideo

current_jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class WelcomeHandler(webapp2.RequestHandler):
    def get(self):
        template_vars = {}
        clarifaiApp = ClarifaiApp(api_key='b6fdc0bdb31847798c3568d6922aa2c8')
        model = clarifaiApp.models.get('general-v1.3')
        image = ClImage(url='http://tineye.com/images/widgets/mona.jpg')
        template_vars["stuff"] = str(model.predict([image]))

        welcome_template = current_jinja_environment.get_template('/templates/welcome.html')

        self.response.write(welcome_template.render())

app = webapp2.WSGIApplication([
    ('/', WelcomeHandler),
])
