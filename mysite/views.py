from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h2>Hello, Apex local. You're seeing the root folder.<h2>")

def home(request):
    return render(request, home/index.html)