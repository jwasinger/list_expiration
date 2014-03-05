from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def login_success(request):
    print(request.user)
    return HttpResponse("login success!")
