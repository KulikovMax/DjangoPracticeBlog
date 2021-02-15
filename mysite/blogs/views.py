from django.shortcuts import render
from django.http import HttpResponse

from .models import Post


def index(request):
    posts = Post.objects.order_by('-time_create')[:5]
    return render(request, 'blogs/index.html', {'posts': posts})


def detail(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, 'blogs/detail.html', {'post': post})
