from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Code1, Code2, similarity

def index(request):
    template = loader.get_template('compare/index.html')
    context = {"this is index page"}
    return render(request,'compare/index.html',context)

def result(request):
    output = "Code1 and Code2 are"
    if similarity == 0:
        output += "similar"
    elif similarity == 1:
        output += "different"
    return HttpResponse(output)

def check(request):
    return HttpResponse("checking...")