# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}
    return render(request,'rango/index.html', context=context_dict)

def about(request):
    return HttpResponse ("Rango says here is the about page.<br/> <a href=\"http://127.0.0.1:8000/rango\">Main</a>")