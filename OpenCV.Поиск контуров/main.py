import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mint_low = (83, 63, 127)
    mint_high = (179, 255, 255)
    mask = cv2.inRange(hsv, mint_low, mint_high)
    res = cv2.bitwise_and(frame, frame, mask=mask)
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 900:
            x, y, w, h = cv2.boundingRect(contour)
            frame = cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 0, 0), 2)
    final = cv2.hconcat([frame, frame])
    cv2.imshow("filter", final)
    cv2.imshow("mask", mask)
    cv2.waitKey(1)