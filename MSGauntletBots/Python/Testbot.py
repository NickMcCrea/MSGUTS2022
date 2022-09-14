
import socket
import time
import random
 

msgFromClient       = "requestjoin:jim"
name = "jim"

bytesToSend         = str.encode(msgFromClient)

serverAddressPort   = ("127.0.0.1", 11000)

bufferSize          = 1024

moveInterval = 3
heartbeatInterval = 5


# Create a UDP socket
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

 
# Send to server using created UDP socket
UDPClientSocket.sendto(bytesToSend, serverAddressPort)

 
timeSinceMove = time.time()
timeSinceHeartbeat = time.time()

while True:

    msgFromServer = UDPClientSocket.recvfrom(bufferSize)[0].decode('ascii')
    
    ##uncomment to see message format from server
    #print(msgFromServer)
    
    if "playerposition" in msgFromServer:
        pos = msgFromServer.split(":")[1]
        posSplit = pos.split(",")
        posx = float(posSplit[0])
        posy = float(posSplit[1])


    now = time.time()

    #every 5 seconds, request to move to a random point nearby. No pathfinding, server will 
    #attempt to move in straight line.
    if (now - timeSinceMove) > moveInterval:

        randomX = random.randrange(-50,50)
        randomY = random.randrange(-50,50)
        posx += randomX
        posy += randomY

        timeSinceMove = time.time()

        requestmovemessage = "moveto:" + str(posx)  + "," + str(posy)

        bytesToSend = str.encode(requestmovemessage)
        UDPClientSocket.sendto(bytesToSend, serverAddressPort)
        print(requestmovemessage)

    #heartbeat - server will remove player if it doesn't hear from client every few seconds at least
    if (now - timeSinceHeartbeat) > heartbeatInterval:
        timeSinceHeartbeat = time.time()
        heartbeatMessage = "heartbeat:"
        bytesToSend = str.encode(heartbeatMessage)
        UDPClientSocket.sendto(bytesToSend, serverAddressPort)
        print(heartbeatMessage)




