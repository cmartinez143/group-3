
# Hello

import webapp2
import jinja2

env= jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))

class results(ndb.Model):
    event = ndb.StringProperty(indexed=False)
    location = ndb.StringProperty(indexed=False)


class BucketListHandler(webapp2.RequestHandler):
    def get(self):
<<<<<<< Updated upstream
    	bucketlistproto_template= env.get_template('bucket_list_form.html')
    	'bucketListItem': self.request.get("bucketListItem")
    	self.response.out.write(bucketlistproto_template.render())
    def post(self):
    	form-results_template= env.get_template('form_results.html')
    	variables = {
    		'bucketListItem':self.response.get('bucketListItem'),
    	}
=======
        bucketlistproto_template= env.get_template('bucket-list-form.html')
        self.response.out.write(bucketlistproto_template.render())
    def post(self):
        form-results_template= env.get_template('form-results.html')
        variables = {
        'bucketListItem':self.response.get('bucketListItem'),
        }
>>>>>>> Stashed changes
    self.repsonse.out.write(form-results_template.render(variables))

app = webapp2.WSGIApplication([
    ('/', BucketListHandler)
], debug=True)
