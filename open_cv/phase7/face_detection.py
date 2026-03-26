# =============================================================================
# Haar Cascade in OpenCV is a machine learning–based object detection method 
# used to detect objects like faces, eyes, cars, etc. in images or video.
# =============================================================================

# =============================================================================
# detectMultiScale() in OpenCV is the main function used in Haar Cascade object detection.
# It scans the image at multiple sizes (scales) to detect objects like faces, eyes, etc.
# | Parameter      | Meaning                                               |
# | -------------- | ----------------------------------------------------- |
# | `image`        | Grayscale image where detection will happen           |
# | `scaleFactor`  | How much the image size is reduced each step          |
# | `minNeighbors` | How many detections are required to confirm an object |
# =============================================================================


import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    detect_face = face_cascade.detectMultiScale(gray_frame, 1.1, 5)
    
    for (x,y,w,h) in detect_face:
        cv2.rectangle(frame, (x,y),(x+w,y+h), (0,255,0),2)
    
    cv2.imshow("webcam face detection", frame)
    
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()