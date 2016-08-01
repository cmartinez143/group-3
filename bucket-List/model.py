from google.appengine.ext import ndb

class Username ( ndb.Model ):
	name= ndb.StringProperty(required=True)
	date_of_birth = ndb.DateProperty(required=False)
 
		