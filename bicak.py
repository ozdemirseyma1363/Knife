import numpy as np
import cv2
import imutils
import datetime
gun_cascade = cv2.CascadeClassifier("C:\\Users\\User\\Desktop\\bicak1\\classifier\\cascade.xml")
camera = cv2.VideoCapture(0)
# initialize the first frame in the video stream
firstFrame = None
# loop over the frames of the video
gun_exist = False
while True:
    (grabbed, frame) = camera.read()
    # if the frame could not be grabbed, then we have reached the end of the video
    if not grabbed:
       break
    # resize the frame, convert it to grayscale, and blur it
    frame = imutils.resize(frame, width=500)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)
    bicak = gun_cascade.detectMultiScale(gray, 1.3, 410)
    if len(bicak) > 0:
        gun_exist = True
    for (x, y, w, h) in bicak:
        frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]
        # if the first frame is None, initialize it
    if firstFrame is None:
        firstFrame = gray
        continue
    # draw the text and timestamp on the frame
    # show the frame and record if the user presses a key
    cv2.imshow("Security Feed", frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
if gun_exist:
    print("guns detected")
else:
    print("guns NOT detected")
# cleanup the camera and close any open windows
camera.release()
cv2.destroyAllWindows()

