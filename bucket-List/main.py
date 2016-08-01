
# Hello

import jinja2
import urllib
import urllib2

from google.appengine.ext import ndb

import webapp2

env= jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))

class results(ndb.Model):
    event = ndb.StringProperty(indexed=False)
    location = ndb.StringProperty(indexed=False)


class BucketListHandler(webapp2.RequestHandler):
    def get(self):
        bucketlistproto_template = env.get_template('bucket_list_form.html')
        self.response.write(bucketlistproto_template.render())
    def post(self):
        form_results_template = env.get_template('form_results.html')
        variables = {
            'bucket_list_item': self.request.get('bucketListItem'),
        }
        bucketlistproto_template= env.get_template('form_results.html')
        self.response.write(form_results_template.render(variables))

# class ResultsHandler(webapp2.RequestHandler):
#     def get(self):
#         bucketlistprototemplate = env.get_template("form_results.html")
        
#         variables = {}
#         variables['bucket_list_item']= advice_result.bucket_list_item
        
#         self.response.write(bucketlistproto_template.render(variables))
        #self.response.write(template.render())



app = webapp2.WSGIApplication([
    ('/', BucketListHandler),
    #('/results', ResultsHandler)
], debug=True)
