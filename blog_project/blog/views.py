from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from .models import BlogPost
from .serializers import BlogPostSerializer


class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer


def upload_view(request):
    return render(request, 'uploads.html')


def blog_detail_view(request, blog_id):
    blog = get_object_or_404(BlogPost, pk=blog_id)
    context = {
        'blog': blog
    }
    return render(request, 'blog_detail.html', context)


def blog_list_view(request):
    blogs = BlogPost.objects.all().order_by('created_at')
    context = {
        'blogs': blogs
    }
    return render(request, 'blog_list.html', context)
