from django.shortcuts import render
from .models import Articles
from .forms import ArticleForm
# Create your views here.


def upload_articles(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        return render(request,'articlelist.html')
    else:
        form = ArticleForm()
    return render(request,'uploadarticles.html',{'form':form})


def articles_list(request):
    articles = Articles.objects.all()
    return render(request,'articlelist.html',{'articles':articles})

  