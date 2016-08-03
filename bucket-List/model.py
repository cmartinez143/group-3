from google.appengine.ext import ndb


class UserData ( ndb.Model ):
    name= ndb.StringProperty(required=True)
    #birthday = ndb.DateProperty(required=False)
    email=ndb.StringProperty(required=True)
  #  password= ndb.StringProperty(required=True)