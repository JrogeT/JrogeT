from django.shortcuts import render

# Create your views here.

def welcome_index(request):
    return render(request,'welcome/index.html',{})

def error_404_view(request, exception):
    return render(request,'welcome/not_found.html',{})