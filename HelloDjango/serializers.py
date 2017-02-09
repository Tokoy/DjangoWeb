# -*- coding: utf-8 -*-
from rest_framework import routers, serializers, viewsets
from hello.models import Person,Article

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('id', 'email', 'password')


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id','title', 'content', 'name')

# ViewSets define the view behavior.
class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = UserSerializer