from django.shortcuts import render
from .forms import CommentForm
from .models import Post,Comment
def index (request):
    posts = Post.objects.order_by('-create_on')
    context = {
        'post': posts
    }
    return render(request, 'blog_index.html', context)

def blog_category(request, category):
    posts= Post.objects.filter(category__category_name__contains=category).order_by('-create_on')
    context= {
        'category' : category,
        'post' : posts
    }
    return render(request, "blog_category.html", context)
def blog_details(request, pk):
    post = Post.objects.get(pk=pk)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post
            )
            comment.save()
    comment = Comment.objects.filter(post=post)
    context = {
        'post': post,
        'comments': comment,
        'form': form
    }
    return render(request, 'blog_details.html', context)
