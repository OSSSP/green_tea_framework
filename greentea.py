# -*- coding: utf-8 -*-

# Main File

import os

module_array = {}

# GreenTea Modules 
from sys import path
path.insert (0, os.path.realpath (os.path.dirname (__file__)) + '/modules/')
path.insert (0, os.path.realpath (os.path.dirname (__file__)) + '/modules/api/')

import output_api

for i in os.listdir (os.path.realpath (os.path.dirname (__file__)) + '/modules/'):
    if i != 'api':
	fp = (os.path.realpath (os.path.dirname (__file__)) + '/modules/' + i)
	if os.path.isdir (fp):
	    for j in os.listdir (os.path.realpath (fp)):
		path.insert (0, fp)
	    	module_array [j.split ('.') [0]] = __import__ (j.split ('.') [0])
# ----------------

def main ():
   while True:
	command = raw_input ('>>> ')
	args = command.split (' ')
	for i in module_array:
	    if module_array [i].__TITLE__ == args [0]:
	       output_api.ApiOutput (module_array [i].__NAME__, module_array [i].__VERS__, module_array [i].__DESC__, module_array [i].__AUTHORS__, None).out ()
	       module_array [i].run (args)

if __name__ == '__main__':
    main ()
