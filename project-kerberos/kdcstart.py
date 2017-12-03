#!/usr/bin/python
# -*- coding= UTF-8 -*-
# KDC启动

import subprocess

(status, output) = subprocess.getstatusoutput('sudo service krb5kdc start')
print(status, output)

