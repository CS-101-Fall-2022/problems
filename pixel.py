from codecs import utf_16_decode


print("hello")

# making a file variable for reading and writing bytes (rb+)
img = open("bmp_24.bmp",'rb+')

# reading the header of the bmp file (information about the image). A bmp file has a header of 54 bytes
header = img.read(54)

# parsing through the actual image information (pixels) of a 24-bit bmp file.
while(True):
    
    # chunk is a pixel of 3 bytes (24 bits) where each byte is one of red, green, and blue.
    chunk = img.read(1)
    
    if chunk == b"":
        break

    # python allows to access individual bytes through indexing.
    # Each byte is printed as an unsigned integer between 0-255 inclusive.

    try:
        print(str(chunk))
    except:
        pass

img.close()