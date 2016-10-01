oauth = "oauth:8rth19ao4w5h6xdxeydk74r8nms1i0"
serverName = "irc.chat.twitch.tv"
port = 6667
userName = "peterg13"
chatName = "peterg"

import socket
import string

def openSocket():
	s = socket.socket()
	s.connect((serverName, port))
	s.send("PASS " + oauth + "\r\n")
	s.send("NICK " + userName + "\r\n")
	s.send("JOIN #" + chatName + "\r\n")
	return s

def sendMessage(s, message):
	messageTemp = ":" + chatName + "!" + chatName + "@" + chatName + ".tmi.twitch.tv PRIVMSG " + chatName + " :" + message
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
			
	sendMessage(s, "Succesfully joined chat")
	
def loadingComplete(line):
	if("End of /NAMES list" in line):
		return False
	else:	
		return True
	







	
s = openSocket()
joinRoom(s)

while True:
	persist = True

