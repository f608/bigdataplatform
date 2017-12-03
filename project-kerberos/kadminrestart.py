#!/usr/bin/python
# -*- coding= UTF-8 -*-
# kadmin重启

import commands

(status, output) = commands.getstatusoutput('sudo service kadmin restart')
print status, output

