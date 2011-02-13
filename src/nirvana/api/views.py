from django.core import serializers
from django.http import HttpResponse
from nirvana.helloworld import models

def index(request):
	post = models.Post(title = 'aaa', content = 'bbb')
	post.save()
	data = serializers.serialize("xml", models.Post.all())
	return HttpResponse(data)
