#!/usr/bin/python
# -*- coding= UTF-8 -*-
# 查看KDC状态

import commands

(status, output) = commands.getstatusoutput('sudo service krb5kdc status')
print status, output

