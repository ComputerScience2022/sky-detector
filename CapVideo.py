from cv2 import cv2
from sky_detector import detector
from matplotlib import pyplot as plt

# Loading video
cap = cv2.VideoCapture('DrivingMiami.mp4')


while True:
    ret, img = cap.read()
    img_sky = detector.get_sky_region_gradient(img)
    cv2.imshow("image", img_sky)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()

cv2.destroyAllWindows()