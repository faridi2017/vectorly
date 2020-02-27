import numpy as np
import cv2

# applying threshold to set all pixel into two
def getTextOverlay(input_image):
    image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)
    ret, bwimg = cv2.threshold(image, 7, 255,cv2.THRESH_BINARY)
    return bwimg


if __name__ == "__main__":
    image_path = 'simpsons_frame0.png'
    img = cv2.imread(image_path)
    output =getTextOverlay(img)
    cv2.imshow('output',output)
    cv2.imwrite('simpons_text.png', output)
    cv2.waitKey(0)
    cv2.destroyAllWIndows()