#!/usr/bin/python
#创建用户主体

import kadmin

username="hehehe/admin@SUPERMAN"

password="123"

kadm=kadmin.init_with_password(username,password)


principal="lalala@SUPERMAN"

password="123"

kadm.ank(principal,password)




