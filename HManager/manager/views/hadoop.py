from django.shortcuts import render, redirect, HttpResponse
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
import json
import subprocess

def hadoop_manage(request):
    if request.method=='GET':
        return render(request,'hadoop.html',locals())

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

def jps(request):
    ret = {'status': 1, 'output':''}
    ret['status'],ret['output']=subprocess.getstatusoutput('jps')
    print(ret)
    return HttpResponse(json.dumps(ret))

def file_ls(request):
    folder=request.GET.get('folder')
    ret = {'status': 1, 'output':'目录错误'}
    if folder:
        ret['status'],ret['output']=subprocess.getstatusoutput('hadoop fs -ls %s'%folder)
    return HttpResponse(json.dumps(ret))

def file_view(request):
    file_name=request.GET.get('filename')
    ret = {'status': 1, 'output':'文件名错误'}
    if file_name:
        ret['status'],ret['output']=subprocess.getstatusoutput('hadoop fs -cat %s'%file_name)
    return HttpResponse(json.dumps(ret))

def file_download(request):
    src=request.GET.get('src')
    des=request.GET.get('des')
    ret = {'status': 1, 'output':'文件名或地址错误'}
    if src and des:
        ret['status'],ret['output']=subprocess.getstatusoutput('hadoop fs –get %s %s'%(src, des))
    return HttpResponse(json.dumps(ret))
