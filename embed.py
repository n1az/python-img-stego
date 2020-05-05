### the python script for embedding the text
### for changing image see code line : 11, 16, 104

import cv2
import numpy as np
from matplotlib import pyplot as plt
import operator
from operator import add
from PIL import Image
#doing canny edge detection
img = cv2.imread('goldhill.png',0) #input file reading
edges = cv2.Canny(img,50,100)


#loading test image
testImage = Image.open("goldhill.png") #input file reading
pixelXY = testImage.load()

edgedic = {}

pixValX = []
pixValY = []
finalkeylist = []

addup = 0

pin = 0

#secret text
st = "Anonymous Fsociety and mr. robot yo. ty and mr. robot yo Anonymous Fsociety and mr. robot yo Anonymous Fsociety and mr. robot yo"

#binary convertion
def tobits(s):
    result = []
    for c in s:
        bits = bin(ord(c))[2:]
        bits = '00000000'[len(bits):] + bits
        result.extend([int(b) for b in bits])
    return result

def frombits(bits):
    chars = []
    for b in range(len(bits) / 8):
        byte = bits[b*8:(b+1)*8]
        chars.append(chr(int(''.join([str(bit) for bit in byte]), 2)))
    return ''.join(chars)
#binary secret msg
sm = tobits(st)

counterBin = len(sm)
print(counterBin)
#sorting the edge pixels
for xval in range(512):
	edgedic[xval] = np.count_nonzero(edges[xval])
sorted_d = dict(sorted(edgedic.items(), key=operator.itemgetter(1), reverse = True))

keylist = list(sorted_d.keys())

#checking required main pixel
for xx in range(0,len(keylist)):
	if (addup <counterBin):
		addup = sorted_d[keylist[xx]] + addup
		finalkeylist.append(keylist[xx])
	else:
		break
#creating two list for embedding
for pixvalfinalx in finalkeylist:
	midlist = np.transpose(np.nonzero(edges[pixvalfinalx]))
	finlist= np.ndarray.flatten(midlist)
	for pixvalfinaly in finlist:
		pixValX.append(pixvalfinalx)
		pixValY.append(pixvalfinaly)

# print(pixValX)
# print(pixValY)

# print(len(pixValX))
# print(len(pixValY))

# print(edges[pixValX[0],pixValY[0]])
# print("sortel list : ", sorted_d)
# print("Payload capacity : ",np.count_nonzero(edges))

print(pixelXY[300,300])
#embedding
for binary in sm:
	if (binary == 0 ):
		if (pixelXY[int(pixValX[pin]),int(pixValY[pin])] % 2 == 0 ):
			pass
		elif (pixelXY[int(pixValX[pin]),int(pixValY[pin])] % 2 != 0 ):
			pixelXY[int(pixValX[pin]),int(pixValY[pin])] = pixelXY[int(pixValX[pin]),int(pixValY[pin])]-1
	elif (binary == 1 ):
		if (pixelXY[int(pixValX[pin]),int(pixValY[pin])] % 2 == 0 ):
			pixelXY[int(pixValX[pin]),int(pixValY[pin])] = pixelXY[int(pixValX[pin]),int(pixValY[pin])]+1
		elif (pixelXY[int(pixValX[pin]),int(pixValY[pin])] % 2 != 0 ):
			pass
	pin += 1
# if (int(pixelXY[int(pixValX[pin]),int(pixValY[pin])]) % 2 == 0 ):
# 			pixelXY[int(pixValX[pin]),int(pixValY[pin])] = pixelXY[int(pixValX[pin]),int(pixValY[pin])]+1
# 		elif (int(pixelXY[int(pixValX[pin]),int(pixValY[pin])]) % 2 != 0 ):
# 			pass

#saving stego image
testImage.save('goldhillx.png', format = 'PNG')  #output file reading
print("Success")

###showing edge pixeled image
# plt.subplot(121),plt.imshow(img,cmap = 'gray')
# plt.title('Original Image'), plt.xticks([]), plt.yticks([])
# plt.subplot(122),plt.imshow(edges,cmap = 'gray')
# plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
# plt.show()