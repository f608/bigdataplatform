from django.shortcuts import render, redirect
from django.http import Http404

def home(request):
    if request.method=='GET':
        return render(request,'home.html',locals())
    else:
        raise Http404


