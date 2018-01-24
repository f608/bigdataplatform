#!/usr/bin/python

import subprocess as sub

username= "root/admin"

p=sub.Popen(["kinit",username],stdin=sub.PIPE,stdout=sub.PIPE,stderr= sub.STDOUT)

input="123"

output=p.communicate(input.encode())

