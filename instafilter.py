#Import Image from PIL
from PIL import Image

#Load Images into Objects
print(os.listdir()) 
base_img= Image.open("portrait.jpg")
img_filter=Image.open("filter3.jpg")

#Set O/P Image size
size=(760,760)

#Resize all the images to o/p size
base_img=base_img.resize(size)
img_filter=img_filter.resize(size)

#split each image into RGB vectors
r,g,b=base_img.split()
R,G,B=img_filter.split()

#Merge RGB vectors from digfrent images
im=Image.merge("RGB", (r,G,b))
im.show()
# im.save('1_merged.jpg')