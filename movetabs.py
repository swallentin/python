#!/usr/bin/python
import os, string, shutil

sourcePath = "/Users/stephanwallentin/Downloads"
destinationPath = "/Users/stephanwallentin/Dropbox/tabs/"

filenames = os.listdir(sourcePath)

for filename in filenames:
	if ".gp" in filename:
		shutil.move(sourcePath + "/" + filename, destinationPath + filename )