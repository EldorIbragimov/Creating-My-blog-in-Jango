from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from posts.views import (
    index, blog, post, search, 
    post_create, post_update, post_delete)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('blog/', blog, name='post-list'),
    path('search/', search, name='search'),
    path('create/', post_create, name='post-create'),
    path('post/<id>/', post, name='post-detail'),
    path('post/<id>/update/', post_update, name='post-update'),
    path('post/<id>/delete/', post_delete, name='post-delete'),
    path('tinymce/', include('tinymce.urls')),
    path('accounts/', include('allauth.urls')),
    #path('login/', auth_views.LoginView.as_view(template_name = 'users/login.html'), name = 'login'),
    #path('logout/', auth_views.LogoutView.as_view(template_name = 'users/logout.html'), name = 'logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)