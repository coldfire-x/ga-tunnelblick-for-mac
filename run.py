# -*- coding: utf8 -*-

import subprocess

FIXED_PASSWD = ''
TUNNELBLINK_VPN_NAME = ''
GA_SECRET = ''

cmd = '/bin/bash connect.sh %s %s %s' % (TUNNELBLINK_VPN_NAME, FIXED_PASSWD, GA_SECRET)
subprocess.call(cmd, shell=True)
