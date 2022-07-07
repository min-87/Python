import cv2

file_path = 'res/360.avi'

cap = cv2.VideoCapture(file_path)

frame_number = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
print(frame_number)

frame_count = 0
while True:
    ret, frame = cap.read()
    if ret is False:
        break
    frame_count += 1
cap.release()
print("Frame counter: ", frame_count)

