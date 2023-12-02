from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.
def article_list(request):
    posts = Post.objects.all().order_by("-created_at")
    return render(request, "articles/article_list.html", {"posts": posts})


def article_detail(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, "articles/article_detail.html", {"post": post})
