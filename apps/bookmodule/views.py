from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    name = request.GET.get("name") or "world!"
    return render(request, "bookmodule/index.html")

def index2(request, val1 = 0):
    return HttpResponse("value1 = "+str(val1))