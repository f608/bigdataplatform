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
from manager.views import homepage,user

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',homepage.home),
    url(r'^kerberos/usermanage/$',user.usermanage),
    url(r'^kerberos/$',user.kerberosmanage),
    #ajax路由
    url(r'^kerberos/verify',user.kerberos_verify),
    url(r'^kerberos/kdc/',user.kdc_ops),
    url(r'^kerberos/client/',user.client_ops),

    url(r'^kerberos/user/admin_login/$',user.kadmin_login),
    url(r'^kerberos/user/admin_logout/$',user.kadmin_logout),

    url(r'^kerberos/user/user_info/',user.get_user_info),
    url(r'^kerberos/user/del/',user.del_user),
]
