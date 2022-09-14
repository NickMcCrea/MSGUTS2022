# MSGUTS2022
Material for MS Challenge GUTS 2022


# Message structure

## Client to server 

** Note, server expects client to send heartbeat message at least once every few seconds. If it doesn't receive one for 10 seconds, it will remove player**

requestjoin:name
moveto:posX,posY
heartbeat:

## Server to client 

playerjoined:name,posX,posY

playerposition:posX,posY

** For the next two messages, client will receive one posX, posY pair per segment in visibility radius **

nearbywalls:posX,posY,posX,posY,posX,posY.....

nearbyfloors:posX,posY,posX,posY,posX,posY....

nearbyitem:itemType,posX,posY

nearbyplayer:name,posX,posY

exit:posX,posY
