# MSGUTS2022
Material for MS Challenge GUTS 2022


# Message structure

Client to server 

requestjoin:name
moveto:posX,posY
heartbeat:

Server to client (note wall and floor message repeats X and Y coord pairs per segment, i.e. one message for multiple walls)

playerjoined:name,posX,posY

playerposition:posX,posY

nearbywalls:posX,posY,posX,posY,posX,posY.....

nearbyfloors:posX,posY,posX,posY,posX,posY....

nearbyitem:itemType,posX,posY

nearbyplayer:name,posX,posY

exit:posX,posY
