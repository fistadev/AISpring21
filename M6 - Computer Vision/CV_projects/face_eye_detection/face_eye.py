import cv2
import time
import numpy as np

# load data
face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye = cv2.CascadeClassifier('haarcascade_eye.xml')
# font = cv2.FONT_HERSHEY_DUPLEX
# time_text = str(time.strftime("%H:%M %p"))
# image = ps.putBText(image,time_text,text_offset_x=image.shape[1]-170,text_offset_y=20,vspace=10,hspace=10, font_scale=1.0,background_RGB=(228,225,222),text_RGB=(1,1,1))

#capture video
capt_video = cv2.VideoCapture(1)

while True:
    ret, img = capt_video.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face.detectMultiScale(gray, 1.6, 10)

    count_faces = 0
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (80, 255, 40), 3)
        rect_faces = gray[y:y + h, x:x + w]
        rect_eyes = img[y:y + h, x:x + w]
        eyes = eye.detectMultiScale(rect_faces)
        # if faces > 1:
        #     count_faces += 1
        #     print(len(count_faces))

        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(rect_eyes, (ex, ey), (ex + ew, ey + eh), (255, 100, 40), 3)

    cv2.imshow('img', img)
    k = cv2.waitKey(30) & 0xff

    # exit videoCapture
    if k == 27:
        break


capt_video.release()
cv2.destroyAllWindows()