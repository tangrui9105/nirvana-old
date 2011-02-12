from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^$', 'nirvana.helloworld.views.index'),
    #(?P<username>[^\.^/]+)
    )
