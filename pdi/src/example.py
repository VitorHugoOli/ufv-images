# import numpy as np
# import argparse
import cv2

print(cv2.__version__)

orig = cv2.imread('stars.png')
(B, G, R) = cv2.split(orig)
cv2.imshow('Original', orig)
cv2.imshow('Blue', B)
cv2.imshow('Green', G)
cv2.imshow('Red', R)

cv2.waitKey(0)

print('Height', orig.shape[0])
print('Width', orig.shape[1])
print('Channels', orig.shape[2])

cv2.waitKey(0)
