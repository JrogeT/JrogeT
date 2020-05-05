from django.shortcuts import render

# Create your views here.

def semester_index(request,semester_number):
    return render(request,'semester/index.html',{})