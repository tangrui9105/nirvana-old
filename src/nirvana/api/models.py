from google.appengine.ext import db

class Blogpost(db.Model):
	title = db.StringProperty()
	content = db.StringProperty()
	author = db.UserProperty()
	created_on = db.DateTimeProperty(auto_now_add = 1)

	def __str__(self):
		return '%s' %self.title

	def get_absolute_url(self):
		return '/helloworld/%s/' % self.key()
