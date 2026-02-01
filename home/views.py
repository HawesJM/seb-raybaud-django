from articles.models import Article
from django.shortcuts import render
from articles.models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all().order_by('-published_date')
    latest_article = articles.first()
    penultimate_article = articles[1] if articles.count() > 1 else None
    latest_article_url = latest_article.url

    context = {
        'articles': articles,
        'latest_article': latest_article,
        'penultimate_article': penultimate_article,
        'latest_article_url': latest_article_url,
    }
    return render(request, 'home/index.html', context)
