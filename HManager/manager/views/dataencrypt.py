from django.shortcuts import render, redirect, HttpResponse
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
import json
import subprocess
from manager.views.common import *

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

def datablock_ops(request):
    op=request.GET.get('op')
    ret = {'status': 0, 'output':'', 'op':op}
    tree= read_xml("/root/bigdata/hadoop-3.0.0/etc/hadoop/hdfs-site.xml")
    root = tree.getroot()
    tags = find_nodes(root,"property")
    if op=='start':
        change_element(tags,"value","false","true")
    elif op=='stop':
        change_element(tags,"value","true","false")
    else:
        ret['status'],ret['output']=1,'无效命令'
    write_xml(tree,"/root/bigdata/hadoop-3.0.0/etc/hadoop/hdfs-site.xml")
    return HttpResponse(json.dumps(ret))

def rpc_ops(request):
    op=request.GET.get('op')
    ret = {'status': 0, 'output':'', 'op':op}
    tree= read_xml("/root/bigdata/hadoop-3.0.0/etc/hadoop/core-site.xml")
    root = tree.getroot()
    tags = find_nodes(root,"property")
    if op=='start':
        change_element(tags,"value","authentication","privacy")
    elif op=='stop':
        change_element(tags,"value","privacy","authentication")
    else:
        ret['status'],ret['output']=1,'无效命令'
    write_xml(tree,"/root/bigdata/hadoop-3.0.0/etc/hadoop/core-site.xml")
    return HttpResponse(json.dumps(ret))

def change_algorithm(request):
    algorithm=request.GET.get('algorithm')
    ret = {'status': 0, 'output':''}
    tree= read_xml("/root/bigdata/hadoop-3.0.0/etc/hadoop/hdfs-site.xml")
    root = tree.getroot()
    tags = find_nodes(root,"property")
    if algorithm=='AES':
        create_property(root,"dfs.encrypt.data.transfer.cipher.suites","AES/CTR/NoPadding")
    elif algorithm=='RC4':
        change_element(tags,"value","3des","rc4")
        remove_property(root,"dfs.encrypt.data.transfer.cipher.suites")
    elif algorithm=='3DES':
        change_element(tags,"value","rc4","3des")
        remove_property(root,"dfs.encrypt.data.transfer.cipher.suites")
    else:
        ret['status'],ret['output']=1,'无效命令'
    write_xml(tree,"/root/bigdata/hadoop-3.0.0/etc/hadoop/hdfs-site.xml")
    return HttpResponse(json.dumps(ret))

def change_bitlength(request):
    bitlength=request.GET.get('bitlength')
    ret = {'status': 0, 'output':''}
    tree= read_xml("/root/bigdata/hadoop-3.0.0/etc/hadoop/hdfs-site.xml")
    root = tree.getroot()
    tags = find_nodes(root,"property")

    # aes key bit length can be configured to 128, 192 or 256
    for v in ['128','192','256']:
        try:
            change_element(tags,"value","128",bitlength)
            ret['status'],ret['output']=0,''
        except Exception as e:
            ret['status'],ret['output']=1,str(e)
    write_xml(tree,"/root/bigdata/hadoop-3.0.0/etc/hadoop/hdfs-site.xml")
    return HttpResponse(json.dumps(ret))

