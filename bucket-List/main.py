#This is a comment

#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

<<<<<<< HEAD

import logging
from google.appengine.ext import ndb
import webapp2
=======
>>>>>>> a27b90e9c09544611923eedf7412f27e6064acfd
import jinja2
import webapp2

<<<<<<< HEAD
=======
#from form_results import Form_results

env= jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))
>>>>>>> a27b90e9c09544611923eedf7412f27e6064acfd

env = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))

class Username ( ndb.Model ):
    name= ndb.StringProperty(required=True)
    date_of_birth = ndb.DateProperty(required=False)
class MainHandler(webapp2.RequestHandler):
    
    def get(self):
<<<<<<< HEAD
        main_template = env.get_template('bucketlistproto.html')
        self.response.out.write(main_template.render())
    def post(self): ## here's the new POST method in the MainHandler
        results_template = env.get_template('newr.html')
        error_template = env.get_template('error.html')
        # the variables that are sent to results.html are user_answer_1 and user_answer_2
        # they contain the input values from the main.html form with names answer1 and answer2
        template_variables = {
            'noun1':self.request.get("noun1"),
            'password':self.request.get("password"),
            'email':self.request.get("email"),
           
            }
        
        u = Username(name =template_variables['noun1'])
        
        exclusive = Username.query().filter(Username.name==template_variables['noun1'])
        only_one=exclusive.fetch()
        if len(only_one)>=1:
            self.response.out.write(error_template.render())
        else:
            self.response.out.write(results_template.render(template_variables))
            u.put()

app = webapp2.WSGIApplication([
    ('/', MainHandler)
=======
        bucketlistproto_template = env.get_template('bucket_list_form.html')
        self.response.write(bucketlistproto_template.render())
    # def post(self):
    #     form_results_template = env.get_template('form_results.html')
    #     variables = {
    #         'bucket_list_item': self.request.get('bucketListItem'),
    #     }
    #     self.response.out.write(form_results_template.render(variables))

class ResultsHandler(webapp2.RequestHandler):
    def post(self):
        form_results_template = env.get_template('form_results.html')
        variables = {
            'bucket_list_item': self.request.get('bucketListItem'),
        }
        self.response.out.write(form_results_template.render(variables))


app = webapp2.WSGIApplication([
    ('/', BucketListHandler),
    ('/results', ResultsHandler)
>>>>>>> a27b90e9c09544611923eedf7412f27e6064acfd
], debug=True)
