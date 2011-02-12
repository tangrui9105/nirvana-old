from google.appengine.ext import db
from django import newforms as forms

class Post(db.Model):
    title = db.StringProperty()
    content = db.StringProperty()
    created_on = db.DateTimeProperty(auto_now_add = 1)
    created_by = db.UserProperty()
    
    def __str__(self):
        return '%s' %self.title
    
    def get_absolute_url(self):
        return '/helloworld/%s/' % self.key()
    
    
class Comment(db.Model):
    post = db.ReferenceProperty(Post)
    title = db.StringProperty()
    content = db.StringProperty()
