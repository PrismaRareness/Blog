from django.shortcuts import render

from app.models import Post


def home(request):
    
    postages = Post.objects.all().order_by("-time_creation")
    
    return render(request, 'home.html', context={'postages': postages})

def detail_post(request, pk):
    postage = Post.objects.get(pk=pk)
    return render(request, 'detail_post.html', context={'postage': postage})
