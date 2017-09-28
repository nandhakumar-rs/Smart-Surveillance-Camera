import cv2
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import os
from mail import send_mail



cascade =  cv2.CascadeClassifier("face.xml")
camera =  cv2.VideoCapture(0)
counter = 0
id = input("Enter the id : ")
while True:
    _,read_vision = camera.read()
    gray_vision =  cv2.cvtColor(read_vision,cv2.COLOR_BGR2GRAY)
    face = cascade.detectMultiScale(gray_vision,1.05,5)
    for x,y,w,h in face:
        cv2.imwrite("dataset/image." + str(id)+"." + str(counter)+".jpg",gray_vision[y:y+h,x:x+w])
        read_vision = cv2.rectangle(read_vision,(x,y),(x+w,y+h),(255,0,255),2)
        cv2.waitKey(100)
    cv2.imshow("vision",read_vision)

    cv2.waitKey(1)
    if counter >20:
        cv2.imwrite("final.jpg", read_vision)
        break
    counter +=1
send_mail()
print("mail sent")
camera.release()
cv2.destroyAllWindows()




