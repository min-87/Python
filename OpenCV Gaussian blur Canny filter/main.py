import cv2

def noth(x):
    pass

cap = cv2.VideoCapture(0)
cv2.namedWindow("track", cv2.WINDOW_NORMAL)
cv2.resizeWindow("track", 400, 400)
cv2.createTrackbar("sigma", "track", 0, 100, noth)

while True:
    ret, frame = cap.read()
    sigma = cv2.getTrackbarPos("sigma", "track")
    blur = cv2.GaussianBlur(frame, (9,9), sigma)
    canny = cv2.Canny(blur, 100, 200)
    cv2.imshow("Original", frame)
    cv2.imshow("track", canny)
    cv2.waitKey(1)