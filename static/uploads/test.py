from PIL import Image, ImageOps
import numpy as np

image_src = 'img.jpg'
im = Image.open(image_src).convert(mode="L")

pixels = np.array(im)
prag = 120
[x, y] = pixels.shape
for i in range(x):
    for j in range(y):
        if pixels[i][j] >= prag:
            pixels[i][j] = 255
        else:
            pixels[i][j] = 0
im_bw = Image.fromarray(pixels)
im_bw.show()
# im_bw.save('img_bw.jpg')