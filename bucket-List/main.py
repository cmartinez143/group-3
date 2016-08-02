import jinja2
import urllib
import urllib2
from google.appengine.ext import ndb
import webapp2

env= jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))
#from form_results import Form_results
class Username ( ndb.Model ):
    name= ndb.StringProperty(required=True)
    date_of_birth = ndb.DateProperty(required=False)
class MainHandler(webapp2.RequestHandler):
    
    def get(self):
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

class results(ndb.Model):
    event = ndb.StringProperty(indexed=False)
    location = ndb.StringProperty(indexed=False)

class BucketListHandler(webapp2.RequestHandler):
    def get(self):
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
        bucketlistproto_template= env.get_template('form_results.html')
        self.response.write(form_results_template.render(variables))

# class ResultsHandler(webapp2.RequestHandler):
#     def get(self):
#         bucketlistprototemplate = env.get_template("form_results.html")
        
#         variables = {}
#         variables['bucket_list_item']= advice_result.bucket_list_item
        
#         self.response.write(bucketlistproto_template.render(variables))
        #self.response.write(template.render())

     #   self.response.out.write(form_results_template.render(variables))


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/', BucketListHandler)
    ('/results', ResultsHandler)
], debug=True)


