"""brain_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^news$', views.otcNewsList, name='otcnews'),
    url(r'^Pg1$', views.otcNewsList, name='otcnews'),
    url(r'^Pg2$', views.pg2, name='otcnews_sub'),
    url(r'^Pg3$', views.pg3, name='otcnews_sub'),
    url(r'^Pg4$', views.pg4, name='otcnews_sub'),
    url(r'^Pg5$', views.pg5, name='otcnews_sub'),
    url(r'^Pg6$', views.pg6, name='otcnews_sub'),
    url(r'^Pg7$', views.pg7, name='otcnews_sub'),
    url(r'^Pg8$', views.pg8, name='otcnews_sub'),
    url(r'^Pg9$', views.pg9, name='otcnews_sub'),
    url(r'^Pg10$', views.pg10, name='otcnews_sub'),
    url(r'^securities$', views.otcSecuritiesList, name='otcsecurities'),
    url(r'^send$', views.sendNews, name='send'),


]
