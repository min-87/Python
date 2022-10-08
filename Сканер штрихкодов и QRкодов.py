import cv2
from pyzbar import pyzbar

def decode(image):
    decoded_objects = pyzbar.decode(image)
    for obj in decoded_objects:
        print(f"Знайдено штрих-код:\n{obj}")
        image = draw_barcode(obj, image)
        print("Тип:", obj.type)
        print("Дані:", obj.data)
    return image

def draw_barcode(decoded, image):
    image = cv2.rectangle(image, (decoded.rect.left, decoded.rect.top), (decoded.rect.left + decoded.rect.width, decoded.rect.top + decoded.rect.height), (0, 255, 0), 5)
    return image

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    frame = decode(frame)
    cv2.imshow("frame", frame)
    if cv2.waitKey(1) == ord("q"):
        break
