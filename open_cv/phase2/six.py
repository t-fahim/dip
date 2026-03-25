# rectangle
# color – Line color in BGR format (Blue, Green, Red)
# thickness – Thickness of the line in pixels (use -1 to fill)
# start_point – top-left corner (x1, y1)
# end_point – bottom-right corner (x2, y2)

import cv2

image = cv2.imread('tree_image.jpg')

if image is None:
    print("image not fount")
else:
    print('image loaded')
    pt1 = (50,100)
    pt2 = (200,300)
    color = (0,0,255)
    thickness = -1
    cv2.rectangle(image,pt1,pt2,color,thickness)
    cv2.imshow("rectangle image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    