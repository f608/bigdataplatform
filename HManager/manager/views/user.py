from django.shortcuts import render, redirect, HttpResponse
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
import json
import subprocess
import kadmin
import pickle
from xml.etree.ElementTree import ElementTree,Element

'''操作xml文件'''
def read_xml(in_path):
  tree = ElementTree()
  tree.parse(in_path)
  return tree

def write_xml(tree,out_path):
  tree.write(out_path)

def find_nodes(tree,path):
  return tree.findall(path)

def change_element(tags,element,text_original,text_changed):
  for tag in tags:
    value = tag.find(element)
    if value.text == text_original:
      value.text = text_changed



def usermanage(request):
    '''用户管理界面'''
    if request.method=='GET':
        if request.session.get('admin'):
            kadm=kadmin.init_with_password(request.session['admin']['un'],request.session['admin']['psd'])
            users=list(kadm.principals())
        return render(request,'usermanage.html',locals())

def kerberosmanage(request):
    '''kerberos管理界面'''
    if request.method=='GET':
        return render(request,'kerberosmanage.html',locals())

@csrf_exempt
def pwd_verify(request):
    '''ajax/用户密码认证'''
    un=request.GET.get('un')
    pwd=request.GET.get('pwd')
    ret = {'status': 1, 'output':'请填写账户名密码'}
    if un and pwd:
        ret['status'],ret['output']=subprocess.getstatusoutput('hadoop job -kill %s'%id)
    return HttpResponse(json.dumps(ret))
    return HttpResponse(json.dumps(ret))

def kerberos_verify(request):
    '''ajax/kerberos操作'''
    op=request.GET.get('op')
    ret = {'status': 0, 'output':'', 'op':op}
    tree= read_xml("/root/bigdata/hadoop-3.0.0/etc/hadoop/core-site.xml")
    root = tree.getroot()
    tags = find_nodes(root,"property")
    if op=='start':
        change_element(tags,"value","simple","kerberos")
    elif op=='stop':
        change_element(tags,"value","kerberos","simple")
    else:
        ret['status']=1
        ret['output']='无效命令'
    write_xml(tree,"/root/bigdata/hadoop-3.0.0/etc/hadoop/core-site.xml")
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

def list_users(request):
    '''ajax/列出认证用户'''
    ret = {'status': 1, 'output':''}
    ret['status'],ret['output']=subprocess.getstatusoutput('sudo klist')
    return HttpResponse(json.dumps(ret))

def del_cache(request):
    '''ajax/删除缓存'''
    status, output=subprocess.getstatusoutput('sudo kdestroy')
    return HttpResponse(json.dumps(status))

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
        ret = {'status': 0,'err':'密码错误'}
    return HttpResponse(json.dumps(ret))

def kadmin_logout(request):
    if request.session['admin']:
        del request.session['admin']
    return redirect('/kerberos/usermanage/')

def get_user_info(request):
    ret={'status':0}
    try:
        if request.session.get('admin'):
            print(request.session['admin']['un'],request.session['admin']['psd'])
            kadm=kadmin.init_with_password(request.session['admin']['un'],request.session['admin']['psd'])
            un=request.GET.get('un')
            princ=kadm.getprinc(un)
            princ='\n'.join([
                "用户名 : %s" % princ.principal,
                "最近更改密码时间 : %s" % princ.last_pwd_change or 'Never',
                "最近成功登录时间 : %s" % princ.last_success or 'Never',
                "最近登录失败时间 : %s" % princ.last_failure or 'Never',
                "过期时间 : %s" % princ.expire or 'Never',
                "密码过期时间 : %s" % princ.pwexpire or 'Never',
                "票据最长生命周期 : %s" % princ.maxlife or 'Never',
                "票据最长更新时间 : %s" % princ.maxrenewlife or 'Never',
                ])
            ret={'status':1,'princ':princ}
    except Exception as e:
        print(e)
        ret['err']='用户信息读取失败'
    return HttpResponse(json.dumps(ret))

def del_user(request):
    if request.session.get('admin'):
        kadm=kadmin.init_with_password(request.session['admin']['un'],request.session['admin']['psd'])
        un=request.GET.get('un')
        #暂未实现
    return redirect('/kerberos/usermanage/')

@csrf_exempt
def create_user(request):
    ret={'status':0}
    try:
        if request.session.get('admin'):
            kadm=kadmin.init_with_password(request.session['admin']['un'],request.session['admin']['psd'])
            un=request.POST.get('un')
            psd=request.POST.get('psd')
            kadm.ank(un,psd)
            ret['status']=1
    except Exception as e:
        ret['err']='用户创建失败'+str(e)
    return HttpResponse(json.dumps(ret))

def changepsd(request):
    ret={'status':0}
    try:
        if request.session.get('admin'):
            kadm=kadmin.init_with_password(request.session['admin']['un'],request.session['admin']['psd'])
            un=request.GET.get('un')
            psd=request.GET.get('psd')
            print(un,psd)
            princ=kadm.getprinc(un)
            princ.change_password(psd)
            ret['status']=1
    except Exception as e:
        print(e)
        ret['err']='用户密码修改失败'
    return HttpResponse(json.dumps(ret))