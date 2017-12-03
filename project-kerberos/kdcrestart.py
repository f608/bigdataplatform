#!/usr/bin/python
# -*- coding= UTF-8 -*-
# KDC重启

import commands

(status, output) = commands.getstatusoutput('sudo service krb5kdc restart')
print status, output

