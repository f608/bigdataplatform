"""HManager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from manager.views import homepage,user,hadoop,dataencrypt

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',homepage.home),
    url(r'^kerberos/usermanage/$',user.usermanage),
    url(r'^kerberos/$',user.kerberosmanage),
    url(r'^hadoop/$',hadoop.hadoop_manage),
    url(r'^dataencrypt/$',dataencrypt.data_encrypt),
    #ajax路由
    #用户认证模块
    url(r'^kerberos/pwdverify/',user.pwd_verify),
    url(r'^kerberos/verify/',user.kerberos_verify),
    url(r'^kerberos/kdc/',user.kdc_ops),
    url(r'^kerberos/client/',user.client_ops),
    url(r'^kerberos/listusers/$',user.list_users),
    url(r'^kerberos/delcache/$',user.del_cache),

    url(r'^kerberos/user/admin_login/$',user.kadmin_login),
    url(r'^kerberos/user/admin_logout/$',user.kadmin_logout),

    url(r'^kerberos/user/user_info/',user.get_user_info),
    url(r'^kerberos/user/del/',user.del_user),
    url(r'^kerberos/user/create_user/$',user.create_user),
    url(r'^kerberos/user/chgpsd/$',user.changepsd),

    #集群管理模块
    url(r'^hadoop/hdfs/',hadoop.hdfs_ops),
    url(r'^hadoop/yarn/',hadoop.yarn_ops),
    url(r'^hadoop/jps/',hadoop.jps),
    url(r'^hadoop/file_ls/',hadoop.file_ls),
    url(r'^hadoop/file_view/',hadoop.file_view),
    url(r'^hadoop/file_download/',hadoop.file_download),
    url(r'^hadoop/stop_job/',hadoop.stop_job),

    #加密模块
    #url(r'^dataencrypt/hdfs/',dataencrypt.hdfs_ops)
    url(r'^dataencrypt/kms/',dataencrypt.kms_ops),
    url(r'^dataencrypt/create_key/',dataencrypt.create_key),
    url(r'^dataencrypt/create_zone/',dataencrypt.create_zone),
    url(r'^dataencrypt/key_view/$',dataencrypt.key_view),
    url(r'^dataencrypt/zone_view/$',dataencrypt.zone_view),
]
