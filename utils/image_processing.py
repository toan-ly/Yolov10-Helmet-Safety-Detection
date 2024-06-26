from PIL import Image
import cv2

def process_image(img):
    img_out = cv2.cvtColor(img.plot(), cv2.COLOR_BGR2RGB)
    return img_out
