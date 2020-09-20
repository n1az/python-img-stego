### the python script for embedding the text
### for changing image see code line : 11, 16, 95

import cv2
import numpy as np
from matplotlib import pyplot as plt
import operator
from operator import add
from PIL import Image
#doing canny edge detection
# for i in range(0,10):
# 	j = str(i)
startx = 0
stopx = 8
#fredkin gate operators
cOut = 0
inPx = 1
inPy = 0
outPx = 1
outPy = 0

def FREDKIN(c):
	cOut = c
	s = XOR(inPx,inPy)
	rs = AND(s,cOut)
	outPx = XOR(inPx,rs)
	outPy = XOR(inPy,rs)
	return 0

def AND (a,b):
	if a == 1 and b == 1:
		return 1
	else:
		return 0
def XOR(a,b):
	if a != b:
		return 1
	else:
		return 0

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

#making equal length binary string
def makeEqLen(a):
	len_a = len(a)
	len_b = 8

	num_zeros = abs(len_a - len_b)
	if (len_a < len_b):
		for i in range(num_zeros):
			a = '0' + a
		return a
	else:
		return a

#secret text
st = "Anonymous Fsocie mr robot Anonymous Fsocie mr robot Anonymous FsAnonymous Fsocie mr robot Anonymous Fsocie mr robot Anonymous Fs"

for i in range(52):
	j=str(i)

	img = cv2.imread('popx/image'+j+'.jpg',0) #input file reading
	edges = cv2.Canny(img,50,100)
	width = img.shape[0]


	#loading test image
	testImage = Image.open("popx/image"+j+".jpg") #input file reading
	pixelXY = testImage.load()

	edgedic = {}

	pixValX = []
	pixValY = []
	finalkeylist = []

	addup = 0

	pin = 0

	


	#binary secret msg
	sms = tobits(st)


	sm = []
	for sb in sms:
		if(sb == 0):
			sm.append(1)
		elif(sb == 1):
			sm.append(0)


	counterBin = len(sm)
	looplen = counterBin/8
	smx = ''.join(str(sxyz) for sxyz in sm)
		
	#sorting the edge pixels
	for xval in range(width):
		edgedic[xval] = np.count_nonzero(edges[xval])
	sorted_d = dict(sorted(edgedic.items(), key=operator.itemgetter(1), reverse = True))

	keylist = list(sorted_d.keys())




	#creating two list for embedding
	for pixvalfinalx in keylist:
		midlist = np.transpose(np.nonzero(edges[pixvalfinalx]))
		finlist= np.ndarray.flatten(midlist)
		for pixvalfinaly in finlist:
			pixValX.append(pixvalfinalx)
			pixValY.append(pixvalfinaly)
	# count = 0
	# for k in pixValX:
	# 	if( k >= 426):
	# 		print(k)
	# 		count+=1
	# print(count)
	# print(len(pixValX))
	#embedding 
	#main loop: iterate secret msg
	for msgbit in range(int(looplen)):
		pix = pixelXY[int(pixValY[pin+0]), int(pixValX[pin+0])]
		if(outPx==1):
			pixR = makeEqLen(bin(pix[0])[2:])
			pixG = makeEqLen(bin(pix[1])[2:])
			pixB = makeEqLen(bin(pix[2])[2:])
			pixR = pixR[:5]+ smx[startx:startx+3]
			startx +=3
			embdR = int(pixR,2)
			pixG = pixG[:5]+ smx[startx:startx+3]
			startx+=3
			embdG = int(pixG,2)
			pixB = pixB[:5]+ smx[startx:startx+2] + pixB[7:]
			startx+=2
			embdB = int(pixB,2)
			pixelXY[int(pixValY[pin]), int(pixValX[pin])] = tuple([embdR, embdG, embdB])
			cOutx = pixB[7:]
			FREDKIN(cOutx)
			pin+=1
		elif(outPx==0):
			outPy = 1
			outPy = 0
			pin+=1
		



		

	#saving stego image
	testImage.save('popy/image'+j+'.jpg', format = 'JPEG')  #output file reading
	print("Success-"+j+"")

