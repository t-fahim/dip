# line drawing
# color – Line color in BGR format (Blue, Green, Red)
# thickness – Thickness of the line in pixels

import cv2

image = cv2.imread('tree_image.jpg')

if image is None:
    print("image not fount")
else:
    print('image loaded')
    pt1 = (50,100)
    pt2 = (200,300)
    color = (0,0,255)
    thickness = 10
    cv2.line(image,pt1,pt2,color,thickness)
    cv2.imshow("line image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    