from django.shortcuts import get_object_or_404, render
from .models import Post
# Create your views here.

def all_posts(request):
    posts = Post.objects.all().order_by('created_on')
    latest_post = posts.last()

    context = {
        'posts': posts, 
        'latest_post': latest_post,
    }

    return render(request, 'blog/blog.html', context)

def post_detail(request, post_id):

    post = get_object_or_404(Post, pk=post_id)

    context = {
        'post': post,
        
    }

    return render(request, 'blog/post_detail.html', context)