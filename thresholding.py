"""Image thresholding with opencv"""
import cv2
import numpy as np
import argparse

from skimage.filters import threshold_sauvola
from skimage import img_as_ubyte

def process(input, output, threshold):
    # Load the image
    img = cv2.imread(input)
    smoothed = cv2.GaussianBlur(img, (25, 25), 1)
    unsharped = cv2.addWeighted(img, 1.0, smoothed, -0.5, 1)

    # kernel_emboss = np.array([[-2, -1, 0],
    #                         [-1, 1, 1],
    #                         [0, 1, 2]])

    # emboss_image = cv2.filter2D(smoothed, -1, kernel_emboss)

    # Convert to grayscale
    gray = cv2.cvtColor(unsharped, cv2.COLOR_BGR2GRAY)

    # equalizer
    gray = cv2.equalizeHist(gray)

    # clahe = cv2.createCLAHE(clipLimit=1.0, tileGridSize=(1, 1))
    # gray = clahe.apply(gray)

    # Apply thresholding
    ret, thresh = cv2.threshold(gray, threshold, 255, cv2.THRESH_BINARY_INV)

    # thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 27, 2)

    # Save the image
    cv2.imwrite(output, thresh)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Image thresholding with opencv")
    parser.add_argument("--input", type=str, help="Input image")
    parser.add_argument("--output", type=str, help="Output image")
    args = parser.parse_args()

    process(args.input, args.output)

