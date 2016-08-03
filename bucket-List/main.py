import jinja2
import urllib
import urllib2
from google.appengine.ext import ndb 
from google.appengine.api import users
from model import UserData
from model import Events
import webapp2
import logging

env= jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))
#from form_results import Form_results

def get_user_data(email):
    p =UserData.query().filter(UserData.email==email)
    user=p.get()
    if user:
        return True
    else:
        return False
current_u_key = 0

class LoginHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            # user is logged in
            logout_url = users.create_logout_url('/')
            greeting = 'THE REAL SIGN OUT BUTTON (<a href="{}">sign out</a>)'.format(
                logout_url)
        else:
            login_url = users.create_login_url('/')
            greeting = '<a href="{}">Sign in</a>'.format(login_url)

        self.response.write(
            '<html><body>{}</body></html>'.format(greeting))
class RegistrationHandler(webapp2.RequestHandler):
    def get(self):
        main_template = env.get_template('registration.html')
        self.response.out.write(main_template.render())
    def post(self): ## here's the new POST method in the MainHandler
        results_template = env.get_template('newr.html')
        error_template = env.get_template('error.html')
        # the variables that are sent to results.html are user_answer_1 and user_answer_2
        # they contain the input values from the main.html form with names answer1 and answer2
        template_variables = {
            'noun1':self.request.get("noun1"),
            'email':self.request.get("email"),
            #"birthday":self.request.get("birthday")
           
            }
        
        u = UserData(name =template_variables['noun1'], email = template_variables['email'])
        #birthday = template_variables['birthday']
        
        exclusive = UserData.query().filter(UserData.name==template_variables['noun1'])
        only_one=exclusive.fetch()
        if len(only_one)>=1:
            self.response.out.write(error_template.render())
        else:
            self.response.out.write(results_template.render(template_variables))
            u.put()

class MainHandler(webapp2.RequestHandler):

    def get(self):
        user = users.get_current_user()
        if user:
            self.response.out.write("You are logged in")
            user_data_exists = get_user_data(user.email())
            if user_data_exists == True:
                # found user data; redirect to bucketform
                self.redirect("/bucketlistform")
            else:
                # no user data; redirect to regitration
                self.redirect("/home")
        else:
            self.redirect("/home")
class HomeHandler(webapp2.RequestHandler):
    def get(self):
        home_template=env.get_template("index.html")
        self.response.write(home_template.render())

class BucketListFormHandler(webapp2.RequestHandler):
    def get(self):
        bucketlistproto_template = env.get_template('bucket_list_form.html')
        self.response.write(bucketlistproto_template.render())
        
class BucketListHandler(webapp2.RequestHandler):
    def get(self):
        bucket_temp = env.get_template("form_results.html")
        user = users.get_current_user()
        user_email = user.email()
        logging.info (user_email)
        user_q = UserData.query().filter(UserData.email == user_email)
        user_l = user_q.fetch()
        logging.info(user_l)
        curr_u = user_l[0]
        u_key = curr_u.key
        logging.info(u_key)
        event_list_q = Events.query().filter(Events.user == u_key )
        event_list = event_list_q.fetch()
        logging.info(event_list)
        variables = {
            'user': curr_u.name,
            'events': event_list
            }
        self.response.write(bucket_temp.render(variables))

    def post(self):
        form_results_template = env.get_template('form_results.html')
        user = users.get_current_user()
        user_email = user.email()
        logging.info (user_email)
        user_q = UserData.query().filter(UserData.email == user_email)
        user_l = user_q.fetch()
        logging.info(user_l)
        curr_u = user_l[0]
        u_key = curr_u.key
        logging.info(u_key)
        e = Events(event = self.request.get('bucketListItem'), user =u_key) 
        e.put()
        event_list_q = Events.query().filter(Events.user == u_key )
        event_list = event_list_q.fetch()
        logging.info(event_list)
        variables = {
            'user': curr_u.name,
            'events': event_list
            }


        bucketlistproto_template= env.get_template('form_results.html')
        self.response.out.write(form_results_template.render(variables))

class FriendsListHandler(webapp2.RequestHandler):
    def get(self):
        friendslist_template = env.get_template('friendslist.html')
        self.response.write(friendslist_template.render())

class MessageListHandler(webapp2.RequestHandler):
    def get(self):
        messages_template = env.get_template('messages.html')
        self.response.write(messages_template.render())

class NewsfeedListHandler(webapp2.RequestHandler):
    def get(self):
        newsfeed_template = env.get_template('newsfeed.html')
        self.response.write(newsfeed_template.render())
        
        

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/register', RegistrationHandler),
    ('/bucketlistform', BucketListFormHandler),
    ('/bucketlist', BucketListHandler),
    ('/login', LoginHandler),
    ('/home',HomeHandler),
    ('/friends', FriendsListHandler),
    ('/messages', MessageListHandler),
    ('/newsfeed',NewsfeedListHandler)
], debug=True)


    


            
    