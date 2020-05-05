from django.shortcuts import render

# Create your views here.

def welcome_index(request):
    return render(request,'welcome/index.html',{})