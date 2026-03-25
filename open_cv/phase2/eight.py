# adding text

# =============================================================================
# image → image where text will be added
# text → string to display
# position → bottom-left corner (x, y)
# font → font type
# font_scale → text size
# color → BGR color (Blue, Green, Red)
# thickness → thickness of text
# =============================================================================

import cv2

image = cv2.imread('tree_image.jpg')

if image is None:
    print("image not fount")
else:
    print('image loaded')
    text = "Hello world"
    position = (50,200)
    font = cv2.FONT_HERSHEY_SIMPLEX
    size = 1
    color = (0,0,255)
    thickness = 2
    cv2.putText(image, text, position, font, size, color, thickness)
    cv2.imshow("text image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()