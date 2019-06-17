import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2

cap = cv2.VideoCapture(0)
kernelSize = 3
lowThreshold = 1
highThreshold = 10

while (True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #blurGray = cv2.GaussianBlur(gray,(kernelSize, kernelSize), 0)
    edges = cv2.Canny(gray, lowThreshold, highThreshold)

    cv2.imshow("Edges", edges)

    ch = cv2.waitKey(1)

	if ch & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()
