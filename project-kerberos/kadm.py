#!/usr/bin/python
# -*- coding: UTF-8 -*-
#在客户端启动kerberos管理器

import kadmin

username="hehehe/admin@SUPERMAN"

password="123"

kadm=kadmin.init_with_password(username,password)
print(kadm)
