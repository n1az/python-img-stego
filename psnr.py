### python script for checking psnr
### see code line 18, 19 for changing image

from math import log10, sqrt 
import cv2 
import numpy as np 

def PSNR(original, compressed): 
	mse = np.mean((original - compressed) ** 2) 
	if(mse == 0): # MSE is zero means no noise is present in the signal . 
				# Therefore PSNR have no importance. 
		return 100
	max_pixel = 255.0
	psnr = 20 * log10(max_pixel / sqrt(mse)) 
	return psnr 

def main(): 
	original = cv2.imread("goldhill.png") ##input image Original
	compressed = cv2.imread("goldhillx.png", 1) ### input image Stego
	value = PSNR(original, compressed) 
	print(f"PSNR value is {value} dB") 
	
if __name__ == "__main__": 
	main() 
