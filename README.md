# Fire-Detection-in-open-CV-in-python

1.Install OpenCV and other required libraries:
```
pip install opencv-python
```
2.Import the necessary libraries:
```
import cv2
import numpy as np
```
3.Load the video or image frame:
```
frame = cv2.imread('frame.jpg')  # Replace 'frame.jpg' with the path to your image or video frame
```
4.Convert the frame to the appropriate color space:
```
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
```
5.Define the lower and upper thresholds for fire detection:
```
lower_red = np.array([0, 50, 50])    # Adjust these values based on your specific requirements
upper_red = np.array([10, 255, 255])  # Adjust these values based on your specific requirements
```
6.Apply the thresholding to detect fire:
```
mask = cv2.inRange(hsv, lower_red, upper_red)
```
7.Perform morphological operations to reduce noise and improve detection:
```
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
```
8.Find contours of the fire region:
```
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
```
9.Draw bounding rectangles around the detected fire:
```
for contour in contours:
    (x, y, w, h) = cv2.boundingRect(contour)
    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
  ```
  10.Display the result:
  ```
 cv2.imshow('Fire Detection', frame)
cv2.waitKey(0)
cv2.destroyAllWindows()
  ```
  
Remember to replace 'frame.jpg' in Step 3 with the actual path to your image or video frame. Also, adjust the values in Steps 5 (lower and upper thresholds) based on the specific color range of the fire you are detecting.
