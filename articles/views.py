from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Article, Category, Publication
from django.views.generic import ListView
from django.core.paginator import Paginator
from django.db.models.functions import Lower


def all_articles(request):

    articles = Article.objects.all()
    query = None
    categories = None
    publications = None
    sort = None
    direction = None
    
    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey=='name':
                sortkey = 'lower_name'
                articles = articles.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            articles = articles.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            articles = articles.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)
    
    if request.GET:
        if "q" in request.GET:
            query = request.GET["q"]
            if not query:
                messages.error(request, "you've entered no search criteria")
                return redirect(reverse("articles"))

            queries = Q(name__icontains=query) | Q(keywords__icontains=query)
            articles = articles.filter(queries)
    
    if request.GET:
        if 'publication' in request.GET:
            publications = request.GET['publication'].split(',')
            articles = articles.filter(publication__name__in=publications)
            publications = Publication.objects.filter(name__in=publications)

    current_sorting = f'{sort}_{direction}'

    page = request.GET.get('page', 1)
    paginator = Paginator(articles, 20)
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)


    context = {
        'articles': articles,
        'search_term': query,
        'current_categories': categories,
        'current_publications': publications,
        'current_sorting': current_sorting,
    }

    return render(request, "articles/articles.html", context)
    return render(request, 'core/articles.html', { 'articles': articles })

@login_required
def add_article(request):

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only admin users can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'article added successfully')
            return redirect(reverse('add_article'))
        else:
            messages.error(request, 'failed to add article, please ensure the form is valid')
    else:
        form = ArticleForm()

    template = 'articles/add_article.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

@login_required
def edit_article(request, article_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only admin users can do that.')
        return redirect(reverse('home'))

    article = get_object_or_404(Article, pk=article_id)
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ArticleForm(instance=article)
        messages.info(request, f'You are editing {article.name}')

    template = 'articles/edit_article.html'
    context = {
        'form': form,
        'article': article,
    }


    return render(request, template, context)

@login_required
def delete_article(request, article_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only admin users can do that.')
        return redirect(reverse('home'))
        
    article = get_object_or_404(Article, pk=article_id)
    article.delete()
    messages.success(request, 'Article deleted!')
    return redirect(reverse('articles'))