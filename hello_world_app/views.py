from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.

#def index(request):
    #return render(request, 'index_hello.html')

#def about(request):
    #return render(request, 'about_hello.html')

def hello(request):
    return HttpResponse("Hello, World!")