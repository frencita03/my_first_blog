from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.contrib.auth.models import User


def post_list(request):
    me=User.objects.get(username='frencita')
    published_date__lte=timezone.now()
    posts = Post.objects.filter(author=me).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
