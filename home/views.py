from articles.models import Article
from django.shortcuts import render

# Create your views here.
def index(request):
    articles = Article.objects.all().order_by('-published_date')
    latest_article = articles.first()
    penultimate_article = articles[1] if articles.count() > 1 else None

    context = {
        'articles': articles,
        'latest_article': latest_article,
        'penultimate_article': penultimate_article,
    }
    return render(request, 'home/index.html', context)
