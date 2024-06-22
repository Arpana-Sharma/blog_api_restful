from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BlogPostViewSet, upload_view, blog_detail_view, blog_list_view

router = DefaultRouter()
router.register(r'posts', BlogPostViewSet, basename='post')

urlpatterns = [
    path('', include(router.urls)),
    path('upload/', upload_view, name='upload'),
    path('blogs/', blog_list_view, name='blog_list'),
    path('blogs/<int:blog_id>/', blog_detail_view, name='blog_detail'),
]
