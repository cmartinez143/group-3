
import jinja2
import webapp2

#from form_results import Form_results

env= jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))
































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
        self.response.out.write(form_results_template.render(variables))


app = webapp2.WSGIApplication([
    ('/', BucketListHandler),
    ('/results', ResultsHandler)
], debug=True)
