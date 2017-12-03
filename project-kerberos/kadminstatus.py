#!/usr/bin/python
# -*- coding= UTF-8 -*-
# 查看kadmin的状态

import commands

(status, output) = commands.getstatusoutput('sudo service kadmin status')
print status, output

