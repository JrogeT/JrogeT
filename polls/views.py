from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,"home.html",{"msg":"Hi :D"})
def me(request):
    return HttpResponse("<h1>I'm JrogeT :D</h1>")