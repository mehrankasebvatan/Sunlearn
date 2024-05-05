from django.http.response import HttpResponse
from .models import Article
from django.shortcuts import render
from django.http import Http404


# Create your views here.


def article_list(request):
    try:
        articles = Article.objects.filter(is_active=True)
        context = {
            'articles': articles
        }
        return render(request, 'blog/blog.html', context)
    except Article.DoesNotExist:
        return render(request, '404.html')

def article_detail(request, article_id):
    try:
        article = Article.objects.get(id=article_id)
        context = {
            'article': article
        }
        return render(request, 'blog/detail.html', context)
    except Article.DoesNotExist:
        return render(request, '404.html')
