from google.appengine.ext import ndb


class UserData ( ndb.Model ):
    name= ndb.StringProperty(required=True)
    #birthday = ndb.DateProperty(required=False)
    email=ndb.StringProperty(required=True)
  #  password= ndb.StringProperty(required=True)

class Events (ndb.Model):
    event = ndb.StringProperty(required=True)
    location = ndb.StringProperty(indexed=False)
    User=ndb.KeyProperty(UserData)