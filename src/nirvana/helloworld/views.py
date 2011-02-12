from django.http import HttpResponse, HttpResponseRedirect
from nirvana.helloworld import models
from django.shortcuts import render_to_response

def render(template, payload):
    payload['recents'] = models.Post.all().order('-created_on').fetch(5)
    return render_to_response(template, payload)

def index(request):
    posts = models.Post.all().order('-created_on').fetch(20)
    payload = dict(posts = posts)
    return render('index.html', payload)
