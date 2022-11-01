from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def register_user(request):
    print('regiter')
    return HttpResponse('regiter')