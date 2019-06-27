#from django.urls import path, include
from django.conf.urls import url, include
from django.urls import path
from .views import (
	PostListView, 
	PostDetailView,
	PostCreateView,
	PostUpdateView,
	PostDeleteView,
	UserPostListView
)
from . import views


urlpatterns = [
	
	path('about/', views.about, name='blog-about'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),  # <int:pk> here is primary key
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('ckeditor/', include('ckeditor_uploader.urls')), 
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),  # <int:pk> here is primary key
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>/', UserPostListView.as_view(), name='user-posts')
]

