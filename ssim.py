### python script for checking psnr
### see code line 8, 9 for changing image


from SSIM_PIL import compare_ssim
from PIL import Image

avg = 0
for i in range(52):
	j = str(i)
	image1 = Image.open('popx/image'+j+'.jpg') ###original image
	image2 = Image.open('popy/image'+j+'.jpg') ###stego image
	value = compare_ssim(image1, image2)
	print(value)
	avg += value
avg = avg / 52
print("SSIM avg is : %.4f " % avg)