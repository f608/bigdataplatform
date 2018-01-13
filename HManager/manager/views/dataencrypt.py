from django.shortcuts import render, redirect
from django.http import Http404

def data_encrypt(request):
    if request.method=='GET':
        return render(request,'dataencrypt.html',locals())