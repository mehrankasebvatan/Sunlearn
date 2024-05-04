from django.http.response import HttpResponse
from .models import Article
from django.shortcuts import render


# Create your views here.


def article_list(request):
    articles = Article.objects.all()
    context = {
        'name': 'Mehran',
        'articles': articles
    }
    return render(request, 'blog/blog.html', context)
