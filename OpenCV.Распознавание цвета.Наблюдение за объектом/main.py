import cv2

def nothing(self):
    pass

cv2.namedWindow("filter")
cap = cv2.VideoCapture(0)

while True:
    flag, img = cap.read()
    low_blue = (90, 70, 70)
    high_blue =(150, 255, 255)
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask_blue = cv2.inRange(img_hsv, low_blue, high_blue)
    result = cv2.bitwise_and(img_hsv, img_hsv, mask=mask_blue)
    cv2.imshow("filter", result)
    cv2.waitKey(50)


