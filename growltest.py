#!/opt/bin/python

GROWL_UDP_PORT = 9887

try:
 	import hashlib
	md5_constructor = hashlib.md5
except ImportError:
	import md5
	md5_constructor = md5.new

import struct
from socket import AF_INET, SOCK_DGRAM, socket

GROWL_PROTOCOL_VERSION=1
GROWL_TYPE_REGISTRATION=0
GROWL_TYPE_NOTIFICATION=1

class GrowlNotificationPacket:

  def __init__(self, application="growlnotify",
               notification="Command-Line Growl Notification", title="Router",
               description="Notification", priority = 0, sticky = False, password = None ):
    self.application  = application.encode("utf-8")
    self.notification = notification.encode("utf-8")
    self.title        = title.encode("utf-8")
    self.description  = description.encode("utf-8")
    flags = (priority & 0x07) * 2
    if priority < 0:
      flags |= 0x08
    if sticky:
      flags = flags | 0x0100
    self.data = struct.pack( "!BBHHHHH",
                             GROWL_PROTOCOL_VERSION,
                             GROWL_TYPE_NOTIFICATION,
                             flags,
                             len(self.notification),
                             len(self.title),
                             len(self.description),
                             len(self.application) )
    self.data += self.notification
    self.data += self.title
    self.data += self.description
    self.data += self.application
    self.checksum = md5_constructor()
    self.checksum.update(self.data)
    if password:
       self.checksum.update(password)
    self.data += self.checksum.digest()
  # end def

  def payload(self):
    return self.data
  # end def
# end class


def main():
	print "test"
    addr = ("127.0.0.1", GROWL_UDP_PORT)
    s = socket(AF_INET,SOCK_DGRAM)
  	p = GrowlNotificationPacket(title="Test",¨description="Haxx")
	print "test"
	s.sendto(p.payload(), addr)
	s.close()
	
	#     if noc == 5:
	#     	p = GrowlNotificationPacket(title=sys.argv[2],
	#     				    description=sys.argv[3],
	#     				    priority=int(sys.argv[4]))
	#     elif noc == 6:
	#     	p = GrowlNotificationPacket(title=sys.argv[2],
	#     				    description=sys.argv[3],
	#     				    priority=int(sys.argv[4]),
	#     				    sticky=stickyok(sys.argv[5]))
	#     elif noc == 7:
	#     	p = GrowlNotificationPacket(title=sys.argv[2],
	#     				    description=sys.argv[3],
	#                                     priority=int(sys.argv[4]),
	#                                     sticky=stickyok(sys.argv[5]),
	#                                     password=sys.argv[6])
	#     else:
	# p = GrowlNotificationPacket(title=sys.argv[2],
	# 			    description=sys.argv[3])
				

if __name__ == '__main__':
	main()