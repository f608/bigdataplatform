#!/usr/bin/python
#修改用户密码

import kadmin

principal=input()
#输入格式为"user@EXAMPLE.COM"的用户主体名

princ = kadm.get_princ(principal)

password=input()
#输入新密码

princ.change_password(password)



