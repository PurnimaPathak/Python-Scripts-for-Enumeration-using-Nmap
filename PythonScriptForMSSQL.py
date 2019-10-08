{\rtf1\ansi\ansicpg1252\cocoartf1671\cocoasubrtf600
{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\ri0\partightenfactor0

\f0\fs24 \cf0 #!/usr/bin/env python\
import subprocess\
import os\
import sys\
import reconf\
from reconf import *\
\
if len(sys.argv) != 2:\
     print "Usage: enum_mssql.py <ip address>"\
     sys.exit(0)\
\
ip_address = sys.argv[1]\
\
NMAPS = "nmap -n -sV -sT -Pn -p 1433 --script=ms-sql-brute,ms-sql-config,ms-sql-dac,ms-sql-dump-hashes,ms-sql-empty-password,ms-sql-hasdbaccess,ms-sql-info,ms-sql-query,ms-sql-tables,ms-sql-xp-cmdshell -oA %s/%s_mssql %s" % (reconf.exampth, ip_address, ip_address)\
print "[+] Executing - %s" % (NMAPS)\
results = subprocess.check_output(NMAPS, shell=True) \
if results != "":\
     print results\
}