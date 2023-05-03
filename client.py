import socket
import struct
from PIL import Image
import time

def main(): 
    host = "10.250.211.11"
    port = 5000
    endTag = 300
    
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))

    # recieve image information 
    sizeData = client.recv(4096)
    columnData = client.recv(4096)
    rowData = client.recv(4096)
    
    #unpack image information
   
    colTup = struct.unpack("i", columnData)
    rowTup = struct.unpack("i", rowData )
    sizeTup = struct.unpack("i", sizeData)
    columnNum = colTup[0]
    rowNum = rowTup[0]
    size = sizeTup[0]
    print(size)
    
    # red bytes are transmitted first then green and then blue
    # red transmission 
    
    redBytes = client.recv(size*2)
    print(len(redBytes))
    greenBytes = client.recv(size*2)
    blueBytes = client.recv(size*2)
    print(len(greenBytes))
    print(len(blueBytes))



   
    
    
    # unpack byte stream information 
    redArray = struct.unpack(str(size) + "h", redBytes)
    greenArray = struct.unpack(str(size) + "h", greenBytes)
    blueArray = struct.unpack(str(size) + "h", blueBytes)

    
    # construct image
    image = Image.new("RGB", (columnNum, rowNum))
    i = 0
    for x in range(columnNum):
        for y in range(rowNum):
            image.putpixel((x,y), (redArray[i], greenArray[i], blueArray[i]))
            i += 1

    image.save("image.jpg")






if __name__ == "__main__":
    main()


