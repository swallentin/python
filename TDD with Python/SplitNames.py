#!/usr/bin/env python
# encoding: utf-8
"""
SplitNames.py

Created by Stephan Wallentin on 2011-05-25.
Copyright (c) 2011 stephan.wallentin@gmail.com. All rights reserved.
"""

import sys
import os
# import sets

def GetUniqueValues(values):
	output = []
	for value in values:
		if value not in output:
			output.append(value)
	return output

def main():
	allNames = "Beverly Chung; Jane Yip; Johnson Jiang; Marvel Zhu; Ophelia Wei; Paul Zhou; Vince Liu; Daniel Zhuang; Helen Lee; Jackson Li; Jacky WangZJ; Lorenzo BuosiSH; Par Lindhe; Sophia L; Tony Shao; Veronica Plaza; Harrison.Zheng; Jay Zhou; Helen Chenmq; Daniel Lupoli; Shen Jiang; Jenny Chen; Valentina Delrio; Beverly Chung; Jane Yip; Johnson Jiang; Marvel Zhu; Ophelia Wei; Paul Zhou; Vince Liu; Daniel Zhuang; Helen Lee; Jacky WangZJ; Par Lindhe; Tony Shao; Veronica Plaza; Harrison.Zheng; Jay Zhou; Bin Chi; Brandon K Lee; Brandon Owens; Brian Mckay; Jim Zhang; Carl Ronnow; Kevin Gu; Lucy Wang_lu; Margaret Zhang; Nikita Dyer; Patrick Schweizer; Samantha Sun; Shaly Shang; Virginie Cailleau; Wendy Bao; Zoe Z; Stephan Wallentin; Jason Wu; Sherry Wan; Renata Barros; Virginie Cailleau; Jenny-Ann Sundbro; Wendy Bao; Stephan Wallentin; Jason Wu; Shen Qian; Bill Zhuang; Zhiming Jiang; Cathy L"
	allNames = allNames.split('; ')
	allNames.sort()
	names = allNames
	names.sort()
	names = GetUniqueValues(names)
	# print len(names)
	# 
	# for name in names:
	# 	print name
	
	# nameset = sets.Set(allNames.split('; '))
	# for name in nameset:
	# 	print name
	# 
	# print len(nameset)
	
	newnameset = sorted(set(allNames))
	
	for name in newnameset:
		print name	
		
		
	
if __name__ == '__main__':
	main()

