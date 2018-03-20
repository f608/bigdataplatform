from django.shortcuts import render, redirect, HttpResponse
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
import json
import subprocess, shlex
from manager.views.common import *

@check_login
def home(request):
    if request.method=='GET':
        return render(request,'home.html',locals())
    else:
        raise Http404


def op_handler(service, op):
    ret = {'status': 1, 'output':'', 'op':op}
    if op=='start':
        ret['status'],ret['output']=subprocess.getstatusoutput('systemctl start %s.service'%service)
    elif op=='stop':
        ret['status'],ret['output']=subprocess.getstatusoutput('systemctl stop %s.service'%service)
    elif op=='status':
        ret['status'],ret['output']=subprocess.getstatusoutput('systemctl status %s.service'%service)
    else:
        ret['status']=1
        ret['output']='无效命令'
    return ret

@check_login
def handle_service(request):
    service=request.GET.get('service')
    op=request.GET.get('op')
    ret=op_handler(service, op)
    return HttpResponse(json.dumps(ret))
