from django.shortcuts import render, redirect, HttpResponse
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
import json
import subprocess
from manager.views.common import *

@check_login
def hadoop_manage(request):
    if request.method=='GET':
        title='集群管理'
        return render(request,'hadoop.html',locals())

@check_login
def hdfs_ops(request):
    op=request.GET.get('op')
    ret = {'status': 1, 'output':'', 'op':op}
    if op=='start':
        ret['status'],ret['output']=subprocess.getstatusoutput('start-dfs.sh')
    elif op=='stop':
        ret['status'],ret['output']=subprocess.getstatusoutput('stop-dfs.sh')
    else:
        ret['status'],ret['output']=1,'无效命令'
    return HttpResponse(json.dumps(ret))

@check_login
def yarn_ops(request):
    op=request.GET.get('op')
    ret = {'status': 1, 'output':'', 'op':op}
    if op=='start':
        ret['status'],ret['output']=subprocess.getstatusoutput('start-yarn.sh')
    elif op=='stop':
        ret['status'],ret['output']=subprocess.getstatusoutput('stop-yarn.sh')
    else:
        ret['status'],ret['output']=1,'无效命令'
    return HttpResponse(json.dumps(ret))

@check_login
def jps(request):
    ret = {'status': 1, 'output':''}
    ret['status'],ret['output']=subprocess.getstatusoutput('jps')
    return HttpResponse(json.dumps(ret))

@check_login
def file_ls(request):
    folder=request.GET.get('folder')
    ret = {'status': 1, 'output':'目录错误'}
    if folder:
        ret['status'],ret['output']=subprocess.getstatusoutput('hadoop fs -ls %s'%folder)
    return HttpResponse(json.dumps(ret))

@check_login
def file_view(request):
    file_name=request.GET.get('filename')
    ret = {'status': 1, 'output':'文件名错误'}
    if file_name:
        ret['status'],ret['output']=subprocess.getstatusoutput('hadoop fs -cat %s'%file_name)
    return HttpResponse(json.dumps(ret))

@check_login
def file_download(request):
    src=request.GET.get('src')
    des=request.GET.get('des')
    ret = {'status': 1, 'output':'文件名或地址错误'}
    if src and des:
        ret['status'],ret['output']=subprocess.getstatusoutput('hadoop fs –get %s %s'%(src, des))
    return HttpResponse(json.dumps(ret))

@check_login
def stop_job(request):
    id=request.GET.get('id')
    ret = {'status': 1, 'output':'JobID错误'}
    if id:
        ret['status'],ret['output']=subprocess.getstatusoutput('hadoop job -kill %s'%id)
    return HttpResponse(json.dumps(ret))

@check_login
def file_upload(request):
    src=request.GET.get('src')
    des=request.GET.get('des')
    ret = {'status': 1, 'output':'文件名或地址错误'}
    if src and des:
        ret['status'],ret['output']=subprocess.getstatusoutput('hadoop fs –put %s %s'%(src, des))
    return HttpResponse(json.dumps(ret))

@check_login
def submit_job(request):
    jar=request.GET.get('jar')
    jobmainclass=request.GET.get('jobmainclass')
    jobargs=request.GET.get('jobargs')
    ret = {'status': 1, 'output':'文件名或参数错误'}
    if jar and jobmainclass and jobargs:
        ret['status'],ret['output']=subprocess.getstatusoutput('hadoop jar %s %s %s'%(jar, jobmainclass, jobargs))
    return HttpResponse(json.dumps(ret))


