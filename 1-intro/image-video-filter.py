# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 08:39:52 2026

@author: verdi
"""

import cv2
#from matplotlib import pyplot as plt

"""
#Image filter
image = cv2.imread("image/lngshot.jpg")
[h,w,c] = image.shape

for i in range(h):
    for j in range(w):
        image[i,j,1] = 0
        image[i,j,0] = 0
        image[i,j,2] = 0
        
cv2.imshow("image merah", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)
"""


#Video filter
camera = cv2.VideoCapture(0)

filter_mode = "normal"

print("r = red, g = green, b = blue, esc = exit")      

while True:
    ok, image = camera.read()     
    if not ok:
        break
    
    if filter_mode == "red":
        image[:, :, 0] = 0
        image[:, :, 1] = 0
    elif filter_mode == "green":
        image[:, :, 0] = 0
        image[:, :, 2] = 0  
    elif filter_mode == "blue":
        image[:, :, 1] = 0
        image[:, :, 2] = 0


    cv2.putText(
        image, 
        f"Filter: {filter_mode.upper()}", 
        (20, 40), 
        cv2.FONT_HERSHEY_SIMPLEX, 
        0.5, 
        (255, 255, 255), 
        2
    )

    cv2.imshow("camera", image)
    
    key = cv2.waitKey(1) & 0xFF
    
    if key == 27:
        break
    elif key == ord('r'):
        filter_mode = "red"
    elif key == ord('g'):  
        filter_mode = "green"
    elif key == ord('b'):
        filter_mode = "blue"
    elif key == ord('n'):
        filter_mode = "normal"

camera.release()
cv2.destroyAllWindows()