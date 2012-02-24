#!/usr/bin/python
import os, string, shutil

sourcePath = "/users/stephanwallentin/dropbox/torrent"
destinationPath = sourcePath + "/"

filenames = os.listdir(sourcePath)

for filename in filenames:
	if "queue" in filename:
		shutil.move(sourcePath + "/" + filename, destinationPath + filename.replace("queue", "") )

