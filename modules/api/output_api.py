import os
from sys import path

class ApiOutput:

    name = None
    version = None
    desc = None
    devs = None
    title = None	

    def __init__ (self, exploitName, exploitVersion, exploitDescription, exploitDevelopers, exploitTitle):
	self.name = exploitName
	self.version = exploitVersion
	self.desc = exploitDescription
	self.devs = exploitDevelopers
	self.title = exploitTitle

    def out (self):
	print 'Name: ' + self.name
	print 'Version: ' + self.version
	print 'Description: ' + self.desc
	print 'Authors: '
	for i in self.devs: print i
