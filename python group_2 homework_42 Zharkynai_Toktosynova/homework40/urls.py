"""homework40 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from webapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users', UserListView.as_view(), name='user_list'),
    path('user/<int:pk>', UserDetailView.as_view(), name='user_detail'),
    path('', ArticleListView.as_view(), name='index'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article_detail'),
    path('update_article/<int:pk>', ArticleDetailView.as_view(), name='update_article'),
    path('delete_article/<int:pk>', ArticleDetailView.as_view(), name='delete_article'),
    path('update_user/<int:pk>', UserDetailView.as_view(), name='update_user'),
    path('delete_user/<int:pk>', UserDetailView.as_view(), name='delete_user'),
]