import cv2
img = cv2.imread("res/shapes.png")
font = cv2.FONT_HERSHEY_COMPLEX
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for contour in contours:
    epsilon = 0.01 * cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, epsilon, True)
    if len(approx) == 3:
        cv2.drawContours(img, [approx], 0, (0,0,0), 3)
        x = approx.ravel()[0]
        y = approx.ravel()[1]
        cv2.putText(img, "Triangle", (x, y), font, 1, (0))
cv2.imshow("Output", img)
cv2.waitKey(0)





