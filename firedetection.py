import cv2
import numpy as np

frame = cv2.imread('frame.jpg')  # Replace 'frame.jpg' with the path to your image or video frame

hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

lower_red = np.array([0, 50, 50])    # Adjust these values based on your specific requirements
upper_red = np.array([10, 255, 255])  # Adjust these values based on your specific requirements

mask = cv2.inRange(hsv, lower_red, upper_red)

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for contour in contours:
    (x, y, w, h) = cv2.boundingRect(contour)
    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
    
cv2.imshow('Fire Detection', frame)
cv2.waitKey(0)
cv2.destroyAllWindows()

