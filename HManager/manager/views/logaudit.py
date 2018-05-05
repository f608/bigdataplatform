from django.shortcuts import render, redirect, HttpResponse
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
import json
import subprocess
from manager.views.common import *

@check_login
def logaudit_homepage(request):
    title="日志审计"
    return render(request, 'logaudit.html', locals())

@check_login
def elasticsearch_start(request):
    ret = {'status': 1, 'output':''}
    ret['status'],ret['output']=subprocess.getstatusoutput('/home/elk/elasticsearch/bin/elasticsearch -d')
    return HttpResponse(json.dumps(ret))

@check_login
def logstash_start(request):
    ret = {'status': 1, 'output':''}
    ret['status'],ret['output']=subprocess.getstatusoutput('/home/elk/logstash/bin/logstash -f /home/elk/logstash/config/test.conf')
    return HttpResponse(json.dumps(ret))

@check_login
def kibana_start(request):
    ret = {'status': 1, 'output':''}
    ret['status'],ret['output']=subprocess.getstatusoutput('/home/elk/kibana/bin/kibana')
    return HttpResponse(json.dumps(ret))