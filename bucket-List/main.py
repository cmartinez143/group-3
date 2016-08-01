#Errors 
import webapp2
import jinja2

env= jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))

class results(ndb.Model):
	event = ndb.StringProperty(indexed=False)
	location = ndb.StringProperty(indexed=Fals)


class BucketListHandler(webapp2.RequestHandler):
    def get(self):
    	bucketlistproto_template= env.get_template('bucket-list-form.html')
    	'bucketListItem': self.request.get("bucketListItem")
    	self.response.out.write(bucketlistproto_template.render())
    def post(self):
    	form-results_template= env.get_template('form-results.html')
    	variables = {
    		'bucketListItem':self.response.get('bucketListItem'),
    	}
    self.repsonse.out.write(form-results_template.render(variables))

app = webapp2.WSGIApplication([
    ('/bucket', BucketListHandler)
], debug=True)
