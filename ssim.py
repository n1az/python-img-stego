### python script for checking psnr
### see code line 8, 9 for changing image


from SSIM_PIL import compare_ssim
from PIL import Image

image1 = Image.open("goldhill.png") ###original image
image2 = Image.open("goldhillx.png") ###stego image
value = compare_ssim(image1, image2)
print(value)