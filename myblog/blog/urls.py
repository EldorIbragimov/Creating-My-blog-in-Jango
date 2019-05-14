#from django.urls import path, include
from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [
	#url(r'', views.home, name='blog-home'),
	path('about/', views.about, name='blog-about'),
    path('', views.home, name='blog-home'),
]
