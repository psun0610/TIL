from django.shortcuts import render, redirect
from .models import Article, Comment
from .forms import ArticleForm, CommentForm

# Create your views here.
def index(request):
    articles = Article.objects.order_by('-pk')
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

def create(request):
    if request.method == 'POST':
        article_form = ArticleForm(request.POST)
        if article_form.is_valid():
            article_form.save()
            return redirect('articles:index')
    else:
        article_form = ArticleForm
    context = {
        'article_form': article_form,
    }
    return render(request, 'articles/create.html', context)

def delete(request, article_pk):
    Article.objects.get(pk=article_pk).delete()
    return redirect('articles:delete', article_pk)

def detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    context = {
        'article': article,
        'comment_form': CommentForm(),
    }
    return render(request, 'articles/detail.html', context)

def comment_create(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.save()
        return redirect('articles:detail', article_pk)

def comment_delete(request, article_pk, comment_pk):
    Comment.objects.get(pk=comment_pk).delete()
    return redirect('articles:detail', article_pk)