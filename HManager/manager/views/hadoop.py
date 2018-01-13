from django.shortcuts import render, redirect
from django.http import Http404

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
        ret['status']=1
        ret['output']='无效命令'
    return HttpResponse(json.dumps(ret))

def yarn_ops(request):
    op=request.GET.get('op')
    ret = {'status': 1, 'output':'', 'op':op}
    if op=='start':
        ret['status'],ret['output']=subprocess.getstatusoutput('start-yarn.sh')
    elif op=='stop':
        ret['status'],ret['output']=subprocess.getstatusoutput('stop-yarn.sh')
    else:
        ret['status']=1
        ret['output']='无效命令'
    return HttpResponse(json.dumps(ret))