from django.shortcuts import render
from djng.views.crud import NgCRUDView
from django.http import HttpResponse
from hello.models import Person
from hello.models import Article
# Create your views here.


def hello(request):
    return render(request, 'index.html')

def add(request):
    Title=request.POST['NewsTitle']
    Context = request.POST['NewsContext']
    Person = request.POST['NewsPerson']

def register(request):
    if request.method == "POST":
        name = request.POST['displayName']
        email = request.POST['email']
        password = request.POST['password']
        Person.objects.get_or_create(name=name, email=email,password=password)
        return render(request, 'index.html')

def login(request):
    if request.method == "GET":
        email = request.GET['email']
        password = request.GET['password']
        Person.objects.get(email=email,password=password)
        return render(request, 'index.html')

def readnews(request):
        return Article.objects.all()