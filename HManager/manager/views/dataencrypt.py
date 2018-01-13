from django.shortcuts import render, redirect, HttpResponse
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
import json
import subprocess

def data_encrypt(request):
    if request.method=='GET':
        title='数据加密'
        return render(request,'dataencrypt.html',locals())

'''
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
'''

def kms_ops(request):
    op=request.GET.get('op')
    ret = {'status': 1, 'output':'', 'op':op}
    if op=='start':
        ret['status'],ret['output']=subprocess.getstatusoutput('hadoop --daemon start kms')
    elif op=='stop':
        ret['status'],ret['output']=subprocess.getstatusoutput('hadoop --daemon stop kms')
    else:
        ret['status'],ret['output']=1,'无效命令'
    return HttpResponse(json.dumps(ret))

def create_key(request):
    key_name=request.GET.get('key_name')
    key_len=request.GET.get('key_len')
    ret = {'status': 1, 'output':'缺少密钥名称'}
    if key_name:
        cmd='hadoop key create %s'%key_name
        if key_len:
            cmd+=' -size %s'%key_len
        ret['status'],ret['output']=subprocess.getstatusoutput(cmd)
    return HttpResponse(json.dumps(ret))

def create_zone(request):
    key_name=request.GET.get('key_name')
    key_path=request.GET.get('key_path')
    ret = {'status': 1, 'output':'缺少密钥名称和地址'}
    if key_name and key_path:
        ret['status'],ret['output']=subprocess.getstatusoutput('hdfs crypto -createZone -keyName %s -path %s'%(key_name, key_path))
    return HttpResponse(json.dumps(ret))

def key_view(request):
    ret = {'status': 1, 'output':''}
    ret['status'],ret['output']=subprocess.getstatusoutput('hadoop key list -metadata')
    return HttpResponse(json.dumps(ret))

def zone_view(request):
    ret = {'status': 1, 'output':''}
    ret['status'],ret['output']=subprocess.getstatusoutput('hdfs crypto -listZones')
    return HttpResponse(json.dumps(ret))