"""typeidea URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url
from blog.views import (
    IndexView, CategoryView,TagView,
    PostDetailView,
)
from config.views import links



urlpatterns = [
    path('admin/', admin.site.urls),
    #url(r'^$',post_list),
    #url(r'category/(?P<category_id>\d+)/$',post_list),
    #url(r'tag/(?P<tag_id>\d+)/$', post_list),
    #url(r'post/(?P<post_id>\d+).html$', post_detail) ,
    #url(r'links/$', links),
    #url(r'^super_admin/',admin.site.urls) ,
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'category/(?P<category_id>\d+)/$', CategoryView.as_view(), name='category-list'),
    url(r'tag/(?P<tag_id>\d+)/$', TagView.as_view(), name='tag-list'),
    url(r'post/(?P<post_id>\d+).html$', PostDetailView.as_view(), name='post-detail'),
    url(r'links/$', links, name='links'),
    url(r'^super_admin/', admin.site.urls, name='super-admin'),
]
