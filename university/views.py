from django.shortcuts import render

# Create your views here.

def university_index(request):
    return render(request,'university/index.html',{})