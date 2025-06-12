import socket

import cvzone
import cv2
from cvzone.ColorModule import  ColorFinder
import socket


cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

success, img = cap.read()
h,w,_ = img.shape

myColorFinder = ColorFinder(False)
hasVals = {'hmin': 22, 'smin': 41, 'vmin': 153, 'hmax': 59, 'smax': 213, 'vmax': 255} # color hasValue

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverAddressPort = ("127.0.0.1", 5052)

while True:
    success, img = cap.read()
    imgColor, mask = myColorFinder.update(img, hasVals)
    imgContour, contours = cvzone.findContours(img, mask)


    if contours:
       data = contours[0]['center'][0], h-contours[0]['center'][1], \
              int(contours[0]['area'])
       print(data)
       data = str.encode(str(data))
       sock.sendto(data, serverAddressPort)



    # imgStack =  cvzone.stackImages([img, imgColor, mask, imgContour], 2, 0.5)
    # cv2.imshow("Image", imgStack)
    imgContour = cv2.resize(imgContour, (0,0), None, 0.3, 0.3)
    cv2.imshow("ImageContour", imgContour)
    cv2.waitKey(1)
