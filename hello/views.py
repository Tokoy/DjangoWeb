# -*- coding: utf-8 -*-
from django.shortcuts import render
from djng.views.crud import NgCRUDView
from django.http import HttpResponse
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import routers, serializers, viewsets
from models import Person,Article
from HelloDjango.serializers import ArticleSerializer,UserSerializer

# Create your views here.
class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

def index(request, format=None):
    return render(request, 'index.html')

def User_list(request, format=None):
    if request.method == "GET":
        Email = request.GET['email']
        # Password = request.GET['password']
        # data = JSONParser().parse(request)
        # findUser=Person.objects.get(email=Email,password=Password)
        # serializer = UserSerializer(data, many=True)
        return Response(Email)
    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
    return render(request, 'index.html')



