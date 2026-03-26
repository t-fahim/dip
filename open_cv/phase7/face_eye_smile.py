# face ,eye and smile detection


import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_smile.xml")

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    detect_face = face_cascade.detectMultiScale(gray_frame, 1.1, 5)
    
    for (x,y,w,h) in detect_face:
        cv2.rectangle(frame, (x,y),(x+w,y+h), (0,255,0),1)
        
    roi_gray = gray_frame[y:y+h, x:x+w]
    roi_color = frame[y:y+h, x:x+w]
    
    detect_eye = eye_cascade.detectMultiScale(roi_gray, 1.1, 10)
    if len(detect_eye) > 0:
        cv2.putText(frame,'eye detected' , (x,y-30), cv2.FONT_HERSHEY_SIMPLEX , 0.6, (0,0,255),1)
        
    detect_smile = smile_cascade.detectMultiScale(roi_gray, 1.7, 20)
    if len(detect_smile) > 0:
        cv2.putText(frame,'smile face' , (x,y-10), cv2.FONT_HERSHEY_SIMPLEX , 0.6, (255,0,0),1)
    
    cv2.imshow("smart face detection", frame)
    
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()