from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from .models import Post, Category
from articles.models import Article
from django.core.paginator import Paginator
# Create your views here.


def all_posts(request):
    query = None
    posts = Post.objects.all().order_by('created_on')
    latest_post = posts.last()
    categories = Category.objects.all()

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('all_posts'))
            
            queries = Q(title__icontains=query) | Q(body__icontains=query)
            posts = posts.filter(queries)
    
    page = request.GET.get('page', 1)
    paginator = Paginator(posts, 3)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)

    context = {
        'posts': posts, 
        'latest_post': latest_post,
        'search_term': query,
        'categories': categories,
    }

    return render(request, 'blog/blog.html', context)


def post_detail(request, post_id):

    post = get_object_or_404(Post, pk=post_id)

    context = {
        'post': post,      
    }

    return render(request, 'blog/post_detail.html', context)


def all_articles(request):
    articles = Article.objects.all().order_by('-published_date')
    
    context = {
        'articles': articles,
    }

    return render(request, 'blog/blog.html', context)