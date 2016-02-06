__NAME__ = 'SIS (Sql Injection Scanner)'
__VERS__ = '0.1f'
__DESC__ = 'This exploit search sql errors on url'
__AUTHORS__ = [ 'DOCTOR_RABB' ]
__TITLE__ = 'sis'
__HELP__ = '<url>'

import urllib2

# -------------
from sys import path
import os

path.insert (0, os.path.realpath (os.path.dirname (__file__)) + '../../modules/api/')
import output_api
# ------------

sql_errors = [ 'SQL Error', 'Query failed', 'You have an error in your SQL' ]

def run (command_args):
    html_page = urllib2.urlopen (command_args [1] + '\'').read ()
    for i in sql_errors:
	if i in html_page:
	    print output_api.YES + 'SQL Error found!'
	    break