from django.shortcuts import render, redirect, HttpResponse
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
import json
import subprocess
from manager.views.common import *

@check_login
def accesscontrol_homepage(request):
    title="访问控制"
    return render(request, 'accesscontrol.html', locals())

@check_login
def sentry_start(request):
    ret = {'status': 1, 'output':''}
    ret['status'],ret['output']=subprocess.getstatusoutput(r'sentry --command service --conffile  ${SENTRY_HOME}/conf/sentry-site.xml')
    return HttpResponse(json.dumps(ret))

@check_login
def hue_start(request):
    ret = {'status': 1, 'output':''}
    ret['status'],ret['output']=subprocess.getstatusoutput(r'/root/bigdata/hue/build/env/bin/hue runserver 0.0.0.0:8888')
    return HttpResponse(json.dumps(ret))