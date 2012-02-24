#!/usr/bin/python
import random, os, sys

filestypes = ["mp4", "avi", "mkv", "mv4", "iso"]
minimumSize = 1000000000

def getRandomDir(path):
  list = os.listdir(path)
  ri = random.randrange(0, len(list))
  return  "{0}/{1}".format(path, list[ri])

def openRandomDir(path):
  os.system("open \"{0}\"".format( getRandomDir(path)))

def main():
  if len(sys.argv) > 1:
    openRandomDir(sys.argv[1])
  
if __name__ == '__main__':
	main()