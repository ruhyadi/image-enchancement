"""Image enhancement with opencv"""
import cv2
import argparse
import os
import json

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
    # argument parser
    parser = argparse.ArgumentParser(description="Image enhancement")
    parser.add_argument("--img_path", default="/assets/input.png", help="Path to image")
    parser.add_argument("--inter_path", default="/assets/intermediate.png", help="Path to intermediate image")
    parser.add_argument("--output_path", default="/assets/results.png", help="Path to output image")
    parser.add_argument("--equalizer", action="store_true", help="Equalize histogram")
    parser.add_argument("--clahe", action="store_true", help="CLAHE")
    parser.add_argument("--clahe_cliplimit", type=float, default=2.0, help="CLAHE clip limit")
    parser.add_argument("--alpha", type=float, default=1.5, help="Alpha")
    parser.add_argument("--beta", type=float, default=-0.5, help="Beta")
    parser.add_argument("--ksize", type=int, default=11, help="Ksize")
    parser.add_argument("--threshold", type=int, default=170, help="Threshold")
    args = parser.parse_args()
    
    process(args.input, args.output)
