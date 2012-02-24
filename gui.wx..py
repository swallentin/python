#!/usr/bin/env python

import wx

class wxHelloApp(wx.App):

	def OnInt(self):
		frame = wx.Frame(None, title="wxHello")
		frame.Show()
		self.SetTopWindow(frame)
		return true

if( __name == "__main__" ):
	app = wxHelloApp()
	app.MainLoop()