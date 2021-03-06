from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from .forms import ArticleForms
from .models import Article
# Create your views here.


@permission_required('Article.add_article')
def create(request):
    author = User.objects.get(id=request.user.id)
    if request.method == 'POST':
        form = ArticleForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('read.article')
    return render(request, 'article/create.html', {'author': author})


def read(request):
    articles = Article.objects.all()
    return render(request, 'article/read.html', {'articles': articles})


@permission_required('Category.change_category')
def update(request, article_id):
    author = User.objects.get(id=request.user.id)
    article = Article.objects.get(id=article_id)
    if request.method == 'POST':
        form = ArticleForms(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            return redirect('read.article')
    return render(request, 'article/update.html', {'article': article, 'author': author})


@permission_required('Category.delete_category')
def delete(request, article_id):
    article = Article.objects.get(id=article_id)
    article.delete()
    return redirect('read.article')


def show(request):
    article_list = Article.objects.all()
    paginator = Paginator(article_list, 9)
    page_number = request.GET.get('page')
    articles = paginator.get_page(page_number)
    return render(request, 'article/articles.html', {'articles': articles})