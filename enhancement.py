"""Image enhancement with opencv"""
import cv2
import argparse
import os
import json


class Enhancement:
    """Image enchancement with OpenCv"""

    def __init__(
        self,
        img_path,
        inter_path,
        output_path,
        equalizer,
        clahe,
        clahe_cliplimit,
        alpha,
        beta,
        ksize,
        threshold,
    ):
        self.img_path = img_path
        self.inter_path = inter_path
        self.output_path = output_path
        self.equalizer = equalizer
        self.clahe = clahe
        self.clahe_cliplimit = clahe_cliplimit
        self.alpha = alpha
        self.beta = beta
        self.ksize = ksize
        self.threshold = threshold

    def enhance(self):
        """enchance image"""
        img = cv2.imread(self.img_path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        if self.equalizer:
            gray = cv2.equalizeHist(gray)
        if self.clahe:
            gray = self.clahe_equalizer(gray, self.clahe_cliplimit)
        # sharpening image
        output = self.blurring(gray, ksize=(self.ksize, self.ksize))
        output = self.sharpening(gray, output, self.alpha, self.beta)
        # write intermediate image
        cv2.imwrite(self.inter_path, output)
        # write output image
        output = self.thresholding(output, threshold=self.threshold)
        cv2.imwrite(self.output_path, output)

        # write histogram
        hist = cv2.calcHist([gray], [0], None, [256], [0, 256])
        return hist

    def blurring(self, input, ksize):
        """blurring image"""
        blurred = cv2.GaussianBlur(src=input, ksize=(ksize), sigmaX=0)
        return blurred

    def sharpening(self, input, blurred, alpha, beta):
        """sharpening image"""
        sharpened = cv2.addWeighted(
            src1=input, alpha=alpha, src2=blurred, beta=beta, gamma=0
        )
        return sharpened

    def clahe_equalizer(self, input, cliplimit):
        """clahe equalizer"""
        clahe = cv2.createCLAHE(clipLimit=cliplimit)
        output = clahe.apply(input)
        return output

    def thresholding(self, input, threshold):
        """thresholding image"""
        ret, thresh = cv2.threshold(input, threshold, 255, cv2.THRESH_BINARY_INV)
        return thresh

    def save_configs(self, configs, output_path):
        """save configs in json"""
        with open(os.path.join(output_path, "configs.json"), "w") as f:
            f.write(json.dumps(configs, indent=4))


if __name__ == "__main__":
    # argument parser
    parser = argparse.ArgumentParser(description="Image enhancement")
    parser.add_argument("--img_path", default="/assets/input.png", help="Path to image")
    parser.add_argument(
        "--inter_path",
        default="/assets/intermediate.png",
        help="Path to intermediate image",
    )
    parser.add_argument(
        "--output_path", default="/assets/results.png", help="Path to output image"
    )
    parser.add_argument("--equalizer", action="store_true", help="Equalize histogram")
    parser.add_argument("--clahe", action="store_true", help="CLAHE")
    parser.add_argument(
        "--clahe_cliplimit", type=float, default=2.0, help="CLAHE clip limit"
    )
    parser.add_argument("--alpha", type=float, default=1.5, help="Alpha")
    parser.add_argument("--beta", type=float, default=-0.5, help="Beta")
    parser.add_argument("--ksize", type=int, default=11, help="Ksize")
    parser.add_argument("--threshold", type=int, default=170, help="Threshold")
    args = parser.parse_args()

    enhancement = Enhancement(
        img_path=args.img_path,
        inter_path=args.inter_path,
        output_path=args.output_path,
        equalizer=args.equalizer,
        clahe=args.clahe,
        clahe_cliplimit=args.clahe_cliplimit,
        alpha=args.alpha,
        beta=args.beta,
        ksize=args.ksize,
        threshold=args.threshold,
    )
    enhancement.enhance()