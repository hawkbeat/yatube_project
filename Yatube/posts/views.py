from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):    
    return HttpResponse('Социальная сеть блогеров Yatube')

def group_posts(request):
    return HttpResponse('Посты по группам')