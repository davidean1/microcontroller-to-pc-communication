import socket
from PIL import Image
import array
import struct
import time


def main(): 
    
    # server set up
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # enter ip for host
    host = '10.250.211.11'
    port = 5000
    endTag = b"<END>"

    # set up image
    image = Image.open("minecraft.jpg")
    redBytes = array.array('h')
    greenBytes = array.array('h')
    blueBytes = array.array('h')

    # store image data in arrays
    for x in range(image.size[0]):
        for y in range(image.size[1]):
            r, g, b = image.getpixel((x,y))
            
            redBytes.append(r)
            greenBytes.append(g)
            blueBytes.append(b)
    
    # pixel data prep
    redBytes = redBytes.tobytes()
    blueBytes = blueBytes.tobytes()
    greenBytes = greenBytes.tobytes()


    # image information prep
    numColumns = image.size[0]
    numRows = image.size[1]
    numPixels = image.size[0] * image.size[1]
    print(numPixels)
    numPixels = struct.pack("i", numPixels)
    numRows = struct.pack("i", numRows)
    numColumns = struct.pack("i", numColumns)
    
    # server start
    server.bind((host, port))
    print (f"server started on {host} on port {port}")
    server.listen(1)
    conn, address = server.accept()
    print (f"connection accepted from {address}")

    # send image data in order of size, column number, row number, red bytes, green bytes, and blue bytes
    conn.sendall(numPixels)
    time.sleep(.2)
    conn.sendall(numColumns)
    time.sleep(.2)
    conn.sendall(numRows)
    time.sleep(.2)
    print(f"Length of bytes for red {len(redBytes)}")
    print(f"Length of bytes for green {len(greenBytes)}")
    print(f"Length of bytes for blue {len(blueBytes)}")

    conn.sendall(redBytes)
    time.sleep(.5)
    conn.sendall(greenBytes)
    time.sleep(.5)
    conn.sendall(blueBytes)


if __name__ == "__main__":
    main()


