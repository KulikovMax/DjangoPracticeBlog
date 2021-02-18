from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.urls import reverse

from .models import Post


def index(request):
    posts_list = Post.objects.order_by('-time_create')
    paginator = Paginator(posts_list, 5)

    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'blogs/index.html', {'posts': posts})


def detail(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, 'blogs/detail.html', {'post': post})


def add_post(request):
    user = request.user
    if user.is_authenticated:
        post = Post(author=user.username)
        post.save()
        return render(request, 'blogs/add_post.html', {'user': user, 'post': post})
    else:
        return redirect('register')


def save_post(request, post_id):
    post = Post.objects.get(pk=post_id)
    post.title = request.POST['post_title']
    post.text = request.POST['post_text']

    if len(post.title) == 0 or len(post.text) == 0:
        post.delete()
        return HttpResponseRedirect(reverse('blogs_add_post'))
    else:
        post.save()
        return HttpResponseRedirect(reverse('blogs_detail', args=(post_id,)))
