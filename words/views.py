from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse("hello world, you are at the wordle landing page")