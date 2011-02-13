from django.conf.urls.defaults import *
from nirvana.piston.resource import Resource
from nirvana.piston.authentication import HttpBasicAuthentication
from nirvana.api.handlers import BlogpostHandler

auth = HttpBasicAuthentication(realm = 'My sample API')

blogposts = Resource(handler = BlogpostHandler, authentication = auth)

urlpatterns = patterns('',
	url(r'^posts/$', blogposts),
	url(r'^posts/(?P<emitter_format>.+)/$', blogposts),
	url(r'^posts\.(?P<emitter_format>.+)', blogposts, name='blogposts'),
)
