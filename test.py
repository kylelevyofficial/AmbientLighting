# Python program to explain cv2.imread() method

# importing cv2
import cv2
import time

# path
path = r'C:\Users\kyler\Programming Projects\AmbientLighting\input\mountain.jpg'

# Using cv2.imread() method
img = cv2.imread(path)

# Displaying the image
cv2.imshow('image', img)
time.sleep(5)
