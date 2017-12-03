from django.shortcuts import render, redirect, HttpResponse
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
import json
import subprocess
import kadmin
import pickle

def usermanage(request):
    '''用户管理界面'''
    if request.method=='GET':
        if request.session.get('admin'):
            kadm=kadmin.init_with_password(request.session['admin']['un'],request.session['admin']['psd'])
            users=kadm.principals()
        return render(request,'usermanage.html',locals())

def kerberosmanage(request):
    '''kerberos管理界面'''
    if request.method=='GET':
        return render(request,'kerberosmanage.html',locals())

@csrf_exempt
def kerberos_verify(request):
    '''ajax/用户认证'''
    un=request.POST.get('un')
    psd=request.POST.get('psd')
    ret={'un':un,'psd':psd}
    return HttpResponse(json.dumps(ret))

def kdc_ops(request):
    '''ajax/kdc操作'''
    op=request.GET.get('op')
    ret = {'status': 1, 'output':'', 'op':op}
    if op=='start':
        ret['status'],ret['output']=subprocess.getstatusoutput('sudo service krb5kdc start')
    elif op=='restart':
        ret['status'],ret['output']=subprocess.getstatusoutput('sudo service krb5kdc restart')
    elif op=='stop':
        ret['status'],ret['output']=subprocess.getstatusoutput('sudo service krb5kdc stop')
    elif op=='status':
        ret['status'],ret['output']=subprocess.getstatusoutput('sudo service krb5kdc status')
    else:
        ret['status']=1
        ret['output']='无效命令'
    return HttpResponse(json.dumps(ret))

def client_ops(request):
    '''ajax/客户端操作'''
    op=request.GET.get('op')
    ret = {'status': 1, 'output':'', 'op':op}
    if op=='start':
        ret['status'],ret['output']=subprocess.getstatusoutput('sudo service kadmin start')
    elif op=='restart':
        ret['status'],ret['output']=subprocess.getstatusoutput('sudo service kadmin restart')
    elif op=='stop':
        ret['status'],ret['output']=subprocess.getstatusoutput('sudo service kadmin stop')
    elif op=='status':
        ret['status'],ret['output']=subprocess.getstatusoutput('sudo service kadmin status')
    else:
        ret['status']=1
        ret['output']='无效命令'
    return HttpResponse(json.dumps(ret))

@csrf_exempt
def kadmin_login(request):
    '''ajax/用户页面管理员登录'''
    un=request.POST.get('un')
    psd=request.POST.get('psd')
    try:
        kadm=kadmin.init_with_password(un,psd)
        ret = {'status': 1, 'un':un}
        request.session['admin']={'un':un,'psd':psd}
    except Exception:
        ret = {'status': 0}
    return HttpResponse(json.dumps(ret))

def kadmin_logout(request):
    if request.session['admin']:
        del request.session['admin']
    return redirect('/kerberos/usermanage/')