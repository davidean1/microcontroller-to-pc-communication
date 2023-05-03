import socket
from PIL import Image
import struct
import pickle

def main(): 

    
    
    # server set up
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # enter ip for host
    host = '10.250.211.11'
    port = 5000
    


    # set up image
    image = Image.open("minecraft.jpg")
    redBytes = []
    greenBytes = []
    blueBytes = []

    # store image data in arrays
    for x in range(image.size[0]):
        for y in range(image.size[1]):
            r, g, b = image.getpixel((x,y))
            
            redBytes.append(r)
            greenBytes.append(g)
            blueBytes.append(b)
    
    numColumns = image.size[0]
    numRows = image.size[1]
    numPixels = image.size[0] * image.size[1]

    data = json.dumps({"columns" numColumns: , "b": arr2, "c": someVar, })

    print(redBytes)

    # set up information to be sent via socket
    
    
    
    # server start
    #server.bind((host, port))
    #print (f"server started on {host} on port {port}")
    #server.listen(1)
    #conn, address = server.accept()
    #print (f"connection accepted from {address}")

  
    


    
   
    


if __name__ == "__main__":
    main()


