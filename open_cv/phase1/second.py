import cv2

# load image
image = cv2.imread('tree_image.jpg')

if image is None:
    print("Error! image not found")
else:
    print("image loded successfully")
    
  
# image dimention    
print(image.shape)
h, w, c = image.shape
print(h,w,c)