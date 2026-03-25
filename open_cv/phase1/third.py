import cv2

# load image
image = cv2.imread('tree_image.jpg')

if image is None:
    print("Error! image not found")
else:
    print("image loded successfully")
    
    
# gray scale convertion
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow("color image", image)
cv2.imshow('gray image', gray)
cv2.waitKey(0)
cv2.destroyAllWindows()