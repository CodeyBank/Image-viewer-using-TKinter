import glob
import cv2
import os

raw_images = glob.glob("*jpg")
raw_images1 = os.listdir(r"C:\Users\VIRGIN\PycharmProjects\my_python_projects\ComputerVision\sample-images")

for item in raw_images:
    img = cv2.imread(item, 1)
    resized_image = cv2.resize(img, (400, 400))
    cv2.imshow("Resized form!", resized_image)
    cv2.waitKey(1000)
    cv2.destroyAllWindows()
    cv2.imwrite("resized_" + item, resized_image)

