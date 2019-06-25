import cv2

img = cv2.imread("Alexandre.jpg", cv2.IMREAD_COLOR)
cv2.imshow('Alexandre', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
