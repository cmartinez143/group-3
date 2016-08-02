from google.appengine.ext import ndb

<<<<<<< HEAD
class Username ( ndb.Model ):
	name= ndb.StringProperty(required=True)
	date_of_birth = ndb.DateProperty(required=False)
 
		
=======
class bucketList(ndb.Model):
    item = ndb.StringProperty(required=True)
    location = ndb.StringProperty(required=False)
>>>>>>> a27b90e9c09544611923eedf7412f27e6064acfd
