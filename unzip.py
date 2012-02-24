import os
import string

def main():
	
	filesToUncompress = open("unzip")
	filesToUncompress = filesToUncompress.read()
	filesToUncompress = filesToUncompress.split("\n")
	for fileToUncompress in filesToUncompress:
		print os.system("unzip -o" + fileToUncompress)
	
if __name__ == '__main__':
	main()