#!/usr/bin/python
import os, string, shutil

sourcePath = "/users/stephanwallentin/dropbox/torrent/Finished"
filenames = os.listdir(sourcePath)

for filename in filenames:
	if ".imported" in filename:
		source = sourcePath + "/" + filename
		print "Source: " + source
		destination = sourcePath + "/" + filename.replace(".imported", "")
		print "Destination: " + destination
		shutil.move( source, destination )
