#!/usr/bin/python
# -*- coding= UTF-8 -*-
# kadmin启动

import commands

(status, output) = commands.getstatusoutput('sudo service kadmin start')
print status, output

