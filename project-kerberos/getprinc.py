#!/usr/bin/python
#获取单个用户的主体信息

import kadmin

principal=input()
#输入格式为"user@EXAMPLE.COM"的主体

princ = kadm.getprinc(principal)

print(princ)



