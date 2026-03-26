# saving webcam video to a file

# =============================================================================
# out = cv2.VideoWriter(filename, fourcc, fps, frame_size)
# | Parameter      | Meaning                          |
# | -------------- | -------------------------------- |
# | filename   | Name of the output video file    |
# | fourcc     | Video codec (compression format) |
# | fps        | Frames per second                |
# | frame_size | Size of video `(width, height)`  |
# =============================================================================


import cv2

cam = cv2.VideoCapture(0)

frame_width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))

codec = cv2.VideoWriter_fourcc(*'XVID')

recorder = cv2.VideoWriter("video.avi",codec,30,(frame_width,frame_height))

while True:
    success, image = cam.read()
    
    if not success:
        print("could not read frame")
        break
    
    recorder.write(image)
    cv2.imshow('Recording live', image)
    
    if cv2.waitKey(1) & 0xff == ord('q'):
        print('quit..')
        break
    
cam.release()
recorder.release()
cv2.destroyAllWindows()
