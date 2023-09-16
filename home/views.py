from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import (
    DetailView,
    ListView)

from weblog.models import Post

def index(request):
    post = Post.objects.all()
    template = 'home.html'
    context = {'post': post}
    return render(request, template , context)
