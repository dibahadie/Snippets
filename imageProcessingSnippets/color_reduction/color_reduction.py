# reducing the number of color values in each channel
import cv2
import numpy as np
IMAGE_PATH = "sample.jpg"


def color_reduction1 (input):
    # colorReduce()
    div = 20
    quantized = input // div * div + div // 2
    return quantized



# gray return 
def color_reduction2(img):
    height, width, _ = img.shape
    img_quant = np.zeros((height, width), dtype=np.uint8)

    for i in range(height):
        for j in range(width):
            #  operator XXXXXXXX & 11000000 equivalent to  XXXXXXXX AND 11000000 (=192)
            #  operator 01000000 >> 2 is a 2-bit shift to the right = 00010000 
            C1 = (img[i, j, 0] & 192) >> 2
            C2 = (img[i, j, 1] & 192) >> 4
            C3 = (img[i, j, 2] & 192) >> 6

            img_quant[i, j] = C1 | C2 | C3  # merges the 2 MSB of each channel

    return img_quant


# driver code
image = cv2.imread(IMAGE_PATH)
image_reduced1 = color_reduction1(image)
image_reduced2 = color_reduction1(image)


cv2.imshow("image", image_reduced1)
cv2.imshow("image2", image_reduced2)
cv2.waitKey(0)