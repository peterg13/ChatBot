from myAuth import oauth, serverName, port, userName, chatName

import socket
import string

def openSocket():
	s = socket.socket()
	s.connect((serverName, port))
	s.send("PASS " + oauth + "\r\n")
	s.send("NICK " + userName + "\r\n")
	s.send(":{0}!{0}@{0}.tmi.twitch.tv JOIN #{0}\r\n".format(chatName))
	return s

def sendMessage(s, message):
	#messageTemp = ":" + chatName + "!" + chatName + "@" + chatName + ".tmi.twitch.tv PRIVMSG " + chatName + " :" + message
	messageTemp = ":{0}!{0}@{0}.tmi.twitch.tv PRIVMSG #{0} :{1}\r\n".format(chatName, message)
	s.send(messageTemp + "\r\n")
	print("Sent: " + messageTemp)

	
def joinRoom(s):
	readBuffer = ""
	Loading = True
	while Loading:
		readBuffer = readBuffer + s.recv(1024)
		temp = string.split(readBuffer, "\n")
		readBuffer = temp.pop()
		
		for line in temp:
			print(line)
			Loading = loadingComplete(line)
			
	print("\n Successfully connected to ")
	
def loadingComplete(line):
	if("End of /NAMES list" in line):
		return False
	else:	
		return True
	







	
s = openSocket()
joinRoom(s)

buffer = ""


while True:
	buffer = buffer + s.recv(1024)
	temp = string.split(buffer, "\n")
	buffer = temp.pop()
	
	for line in temp:
			print(line)

