from django.shortcuts import render, redirect
from .models import Article
from .form import ArticleForm

# Create your views here.
def index(request):
    # READ
    articles = Article.objects.order_by('-pk')
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

def create(request):
    # CREATE
    if request.method == 'POST':
        # DB 저장
        article_form = ArticleForm(request.POST)
        # 유효성 검사
        if article_form.is_valid():
            article_form.save()
            return redirect('articles:index')
    # method가 GET이면
    else:
        article_form = ArticleForm()
    context = {
        'article_form': article_form
    }
    return render(request, 'articles/create.html', context)


def detail(request, pk):
    # READ
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)

def update(request, pk):
    # GET 받아서 CREATE
    # method가 POST일때 수정된 글을 저장
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        article_form = ArticleForm(request.POST, instance=article)
        if article_form.is_valid():
            article_form.save()
            return redirect('articles:detail', article.pk)
    # method가 GET일때 
    else:
        article_form = ArticleForm(instance=article)
    context = {
        'article_form': article_form,
    }
    return render(request, 'articles/update.html', context)

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')