"""Image thresholding with opencv"""
import cv2
import argparse
import os
import json


def process2(input, output, threshold):
    # Load the image
    img = cv2.imread(input)
    smooothed = blur(img, output, ksize=5, sigma=1.5)

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


def process(img_path, inter_path, output_path, equalizer, clahe, clahe_cliplimit, alpha, beta, ksize, threshold):
    """process image"""
    img = cv2.imread(img_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    if equalizer:
        gray = cv2.equalizeHist(gray)
    if clahe:
        gray = clahe_equalizer(gray, clahe_cliplimit)

    # smoothed
    output = blurring(gray, ksize=(ksize, ksize))
    # sharpening
    output = sharpening(gray, output, alpha, beta)

    # intermediate
    cv2.imwrite(inter_path, output)

    output = thresholding(output, threshold=threshold)
    cv2.imwrite(output_path, output)

    hist = cv2.calcHist([gray], [0], None, [256], [0, 256])

    return hist


def blurring(input, ksize):
    """blurring image"""
    blurred = cv2.GaussianBlur(src=input, ksize=(ksize), sigmaX=0)

    return blurred


def sharpening(input, blurred, alpha, beta):
    """sharpening image"""
    sharpened = cv2.addWeighted(
        src1=input, alpha=alpha, src2=blurred, beta=beta, gamma=0
    )

    return sharpened


def clahe_equalizer(input, cliplimit):
    """clahe equalizer"""
    clahe = cv2.createCLAHE(clipLimit=cliplimit)
    output = clahe.apply(input)

    return output


def thresholding(input, threshold):
    """thresholding image"""
    ret, thresh = cv2.threshold(input, threshold, 255, cv2.THRESH_BINARY_INV)

    return thresh


def save_configs(configs, output_path):
    """save configs in json"""
    with open(os.path.join(output_path, "configs.json"), 'w') as f:
        f.write(json.dumps(configs, indent=4))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Image thresholding with opencv")
    parser.add_argument("--input", type=str, help="Input image")
    parser.add_argument("--output", type=str, help="Output image")
    args = parser.parse_args()

    process(args.input, args.output)
