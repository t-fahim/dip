import cv2

# load image
image = cv2.imread('tree_image.jpg')

if image is None:
    print("Error! image not found")
else:
    print("image loded successfully")
    
# display image
cv2.imshow('image titel', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# saving the image
save = cv2.imwrite('output.jpg', image)
if save:
    print('save successfully')
else:
    print('fail to save')
