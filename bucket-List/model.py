from google.appengine.ext import ndb

class bucketList(ndb.Model):
    item = ndb.StringProperty(required=True)
    location = ndb.StringProperty(required=False)
