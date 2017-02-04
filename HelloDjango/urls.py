# -*- coding: utf-8 -*-
"""HelloDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url,include
from django.contrib import admin
from hello import views
from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User
from hello.models import Person,Article
from HelloDjango.serializers import ArticleViewSet,UserViewSet
from rest_framework.urlpatterns import format_suffix_patterns

# Serializers define the API representation.


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'context', ArticleViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    url('^index/$',views.index),
    url('^register/$',views.User_list , name='register'),
    url('^login/$',views.User_list , name='login'),
    # url('^login/(?P<pk>[0-9]+)$',views.User_detail , name='login'),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url('^admin/', (admin.site.urls)),
]
# urlpatterns = format_suffix_patterns(urlpatterns)