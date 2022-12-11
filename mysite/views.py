from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, Apex myrun2. You're seeing the root folder.")