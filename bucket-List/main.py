
# Hello

import jinja2
import urllib

from google.appengine.ext import ndb

import webapp2

env= jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))

class results(ndb.Model):
    event = ndb.StringProperty(indexed=False)
    location = ndb.StringProperty(indexed=False)


class BucketListHandler(webapp2.RequestHandler):
    def get(self):
    	bucketlistproto_template= env.get_template('bucket_list_form.html')
    	self.response.out.write(bucketlistproto_template.render())
    def post(self):
    	form_results_template= env.get_template('form_results.html')
    	variables = {
    		'bucketListItem':self.response.get('bucketListItem'),
    	}
        bucketlistproto_template= env.get_template('bucket_list_form.html')
        self.response.out.write(bucketlistproto_template.render(variables))


#class ResultsHandler(webapp2.ResultsHandler):

app = webapp2.WSGIApplication([
    ('/', BucketListHandler),
    #('/results', ResultsLishandler)
], debug=True)
