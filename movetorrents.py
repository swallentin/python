#!/usr/bin/python
import os, string, shutil

sourcePath = "/Users/stephanwallentin/Dropbox/Torrent/Queue"
destinationPath = "/Users/stephanwallentin/Dropbox/Torrent/Queue/"

filenames = os.listdir(sourcePath)

for filename in filenames:
	if ".imported" in filename:
		shutil.move(sourcePath + "/" + filename, destinationPath + filename.replace(".imported", "") )