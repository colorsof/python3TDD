from django.shortcuts import render
from django.core.context_processors import request
from django.http.response import HttpResponse

# Create your views here.
def home_page(request):
    return render(request, 'home.html')