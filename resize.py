import cv2
import sys

img = cv2.imread(sys.argv[1])
dst = cv2.resize(img, (64,64))
cv2.imwrite(sys.argv[1], dst)
