import numpy as np
import cv2

cap = cv2.VideoCapture(0)
#cv2.namedWindow("Frame")


while(True):
	ret, frame = cap.read()

	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	pathFace = "haarcascade_frontalface_default.xml"
	faceCascade = cv2.CascadeClassifier(pathFace)
	faces = faceCascade.detectMultiScale(gray, scaleFactor=1.10, minNeighbors=5, minSize=(40,40))

	for(x, y, w, h) in faces:
		cv2.rectangle(frame, (x,y), (x+w,y+h), (100,0,255), 2)

	pathEyes = "haarcascade_eye.xml"
	eyeCascade = cv2.CascadeClassifier(pathEyes)
	eyes = eyeCascade.detectMultiScale(gray, scaleFactor=1.02, minNeighbors=15, minSize=(10,10))

	for (x, y, w, h) in eyes:
		xc = (x+ x+w)/2
		yc = (y+ y+h)/2
		radius = w/2
		cv2.circle(frame, (int(xc), int(yc)), int(radius), (0,2550,0), 1)

	cv2.imshow("FaceTrack",frame)

	ch = cv2.waitKey(1)
	if ch & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()
