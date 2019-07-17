import os
from PIL import Image
print(os.listdir())
base_img= Image.open("portrait.jpg")
img_filter=Image.open("filter3.jpg")

size=(760,760)

base_img=base_img.resize(size)
img_filter=img_filter.resize(size)

r,g,b=base_img.split()
R,G,B=img_filter.split()

im=Image.merge("RGB", (r,G,b))
im.show()
# im.save('1_merged.jpg')