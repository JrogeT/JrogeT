from django.shortcuts import render

# Create your views here.

def personal_calendar_index(request):
    return render(request,'personal_calendar/index.html',{})