from django.shortcuts import render, redirect, HttpResponse
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
import json
import subprocess

def data_encrypt(request):
    if request.method=='GET':
        return render(request,'dataencrypt.html',locals())