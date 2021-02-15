from django.shortcuts import render

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

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
