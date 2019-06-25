import cv2

img = cv2.imread("Alexandre.jpg", cv2.IMREAD_COLOR)
enhance = cv2.detailEnhance(img)
cv2.imshow('Alexandre', enhance)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("Alexandre_result.jpg", img)
