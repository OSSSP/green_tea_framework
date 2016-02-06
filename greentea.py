# -*- coding: utf-8 -*-

# Main File

import os
from colorama import Fore

module_array = {}

# GreenTea Modules 
from sys import path
path.insert (0, os.path.realpath (os.path.dirname (__file__)) + '/modules/')
path.insert (0, os.path.realpath (os.path.dirname (__file__)) + '/modules/api/')

import output_api

for i in os.listdir (os.path.realpath (os.path.dirname (__file__)) + '/tools/'):
	fp = (os.path.realpath (os.path.dirname (__file__)) + '/tools/' + i)
	if os.path.isdir (fp):
	    for j in os.listdir (os.path.realpath (fp)):
		path.insert (0, fp)
	    	module_array [j.split ('.') [0]] = __import__ (j.split ('.') [0])
# ----------------

def main ():
	
   banner = Fore.GREEN + '''
   ──────────█───────────────────────
   ──────────███─────────────────────
   ───────────█████──────────────────
   ────────────████──────────────────
   ─────────────████───█─────────────
   ─────────────███────██────────────
   ─────────────███────███───────────
   ────────────███────████───────────
   ────────────██────████───█────────
   ───────────██───█████────█────────
   ──────────██───███─────███────────
   ──────────█───██─────█████────────
   ─────────██───█───██████──────────
   ──────────█───█───██──────────────
   ──────────██──█──██───────────────
   ───────────█──█──█────────────────
   ───────────██────█────────────────
   ──────────────────────────────────
   ───────██████████████████─────────
   ────────████████████████──────────
   ─────────██████████████──███──────
   ─────────█████████████████──█─────
   ─────────███████████████─────█────
   ─────────██████████████──────█────
   ─────────██████████████─────██────
   ─────────██████████████────██─────
   ─────────██████████████──███──────
   ─────────████████████████─────────
   ──────────████████████────────────
   ───────────███████████────────────
   ────────────████████──────────────
   ─────────────██████───────────────
   ───────────██████████─────────────'''

   print banner
   print '─────────── ' + Fore.WHITE + ' GreenTea Framework ' + Fore.GREEN +  ' ───────────' + Fore.RESET

   while True:
	command = raw_input ('>>> ')
	args = command.split (' ')
	if args [0] == 'exploits':
	    for i in module_array: print module_array [i].__TITLE__
	elif args [0] == 'run':
#	   print args [1:]
	   for i in module_array:
	       if module_array [i].__TITLE__ == args [1]:
	          try:
	       	      if args [2] == 'help':
		         print 'Using ' + args [1] + ': ' + args [1] + ' ' + module_array [i].__HELP__
		         break
	          except IndexError:
		         print 'Using ' + args [1] + ': ' + args [1] + ' ' + module_array [i].__HELP__
                         break
	          output_api.ApiOutput (module_array [i].__NAME__, module_array [i].__VERS__, module_array [i].__DESC__, module_array [i].__AUTHORS__, None).out ()
	          module_array [i].run (args [1:])
	else:
	   print output_api.ERR + 'Command not found!'
if __name__ == '__main__':
    main ()
