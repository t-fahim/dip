# video capture

# =============================================================================
# | Value | Meaning                                             |
# | ----- | --------------------------------------------------- |
# | `0`   | Default webcam (usually the built-in laptop camera) |
# | `1`   | Second camera (external USB webcam)                 |
# | `2`   | Third camera                                        |
# | `3`   | Fourth camera                                       |
# ============================================================================


import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read() # ret -> true/false; frame -> image
    
    if not ret:
        print("could not read frame")
        break
    
    cv2.imshow('webcame',frame)
    
    # press 'q' for quite
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print('Quiting...')
        break
        
cap.release()
cv2.destroyAllWindows()