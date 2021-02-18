# Create your views here.
from django.shortcuts import render, get_object_or_404

from .models import Blog


def blog_list(request):
    context = {}
    context['blogs'] = Blog.objects.all()
    return render(request, 'blog_list.html', context)


def blog_detail(request, blog_pk):
    context = {}
    context['blog'] = get_object_or_404(Blog, id=blog_pk)
    return render(request, 'blog_detail.html', context)
