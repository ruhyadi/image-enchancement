<div align="center">

# Image Enchanment

<a href="https://www.python.org/"><img alt="Python" src="https://img.shields.io/badge/-Python 3.8+-blue?style=flat&logo=python&logoColor=white"></a>
<a href="https://pytorch.org/get-started/locally/"><img alt="PyTorch" src="https://img.shields.io/badge/-PyTorch 1.8+-red?style=flat&logo=pytorch&logoColor=white"></a>
<a href="https://opencv.org/"><img alt="PyTorch" src="https://img.shields.io/badge/-OpenCV 4.4.0+-green?style=flat&logo=opencv&logoColor=white"></a>
<a href="https://github.com/XPixelGroup/BasicSR"><img alt="Code style: black" src="https://img.shields.io/badge/BasicSR-v1.3.5-purple.svg?style=flat&labelColor=gray"></a>

</div>

## ⚠️&nbsp;&nbsp;Cautions
> This repository currently under development

## 📼&nbsp;&nbsp;Demo
<div align="center">

[demo](assets/demo.gif)

</div>

## 📌&nbsp;&nbsp;Introduction

This repository is used for assessment purposes in the image enhancement task. There are two types of enhancements used:

- Enhancement using OpenCV Python
- Enhancement using GAN (Generative Adversarial Network) and OpenCV Python

## 🚀&nbsp;&nbsp;Quickstart
> In using this repository, it is recommended to use a virtual environment (**Anaconda**) or use the **Docker Image** that has been provided.

### 💎&nbsp;&nbsp;Installation
> The steps will install the required dependencies
> 
1. Clone repository
```bash
git clone https://github.com/ruhyadi/assessment-image-enchancment
```
2. Install requirements inside Virtual Env (details in [miniconda](https://docs.conda.io/en/latest/miniconda.html))
```bash
cd assessment-image-enchancment
pip install -r requirements.txt
```
3. Install **BasicSR**
```bash
cd BasicSR
python setup.py develop
```
4. Download ESRGAN Pretrained Model
```bash
python scripts/download_pretrained_models.py ESRGAN
```

### 🍿&nbsp;&nbsp;Inference
> Intentionally left blank, will be filled later

#### Enchancement with OpenCV
I have provided a GUI application that can be used for this purpose. The application can be accessed by:
```bash
streamlit run app.py
```
In the application you can input **the input image** and **the ground-truth image**. The application will process the image into an intermediate image and an output image. Inside the application there are sliders and buttons that can be combined to produce the best enhancement results.
For details see the demo section.

The enhancement function can also be accessed via `enhancement.py`scripts:
```bash
python enhancement.py \
  --img_path /assets/input.png \
  --inter_path /assets/intermediate.png \
  --output_path /assets/results.png \
  --alpha 1.5 \
  --beta -0.5 \
  --ksize 11 \
  --threshold 170 \
  --clahe \
  --clahe_cliplimit 2.0 \
  --equalizer
```
with the help:
```bash
usage: enhancement.py [-h] [--img_path IMG_PATH] [--inter_path INTER_PATH] [--output_path OUTPUT_PATH] [--equalizer] [--clahe]
                      [--clahe_cliplimit CLAHE_CLIPLIMIT] [--alpha ALPHA] [--beta BETA] [--ksize KSIZE] [--threshold THRESHOLD]

Image enhancement

optional arguments:
  -h, --help            show this help message and exit
  --img_path IMG_PATH   Path to image
  --inter_path INTER_PATH
                        Path to intermediate image
  --output_path OUTPUT_PATH
                        Path to output image
  --equalizer           Equalize histogram
  --clahe               CLAHE
  --clahe_cliplimit CLAHE_CLIPLIMIT
                        CLAHE clip limit
  --alpha ALPHA         Alpha
  --beta BETA           Beta
  --ksize KSIZE         Ksize
  --threshold THRESHOLD
                        Threshold
```

#### Generative Adversarial Network (GAN)
Enhancement can also use GAN. The GAN function here **does not directly** get the thresholding of the image, but as an intermediate for upscaling the image first. The GAN command can be executed with:

```bash
python BasicSR/inference/inference_esrgan.py \
  --model_path BasicSR/experiments/pretrained_models/ESRGAN/ESRGAN_SRx4_DF2KOST_official-ff704c30.pth \
  --input assets
```

The results of upscaling the image using GAN can be seen in the table below:

|Input Image|GAN Results|
|:--:|:--:|
|[head](assets/head.png)|[head-gan](assets/head_ESRGAN.png)|
|[before](assets/input.png)|[output](assets/001_ESRGAN.png)|

The results of the GAN look not very effective for the image in the second row, this is because the GAN is very dependent on the image data being trained, maybe the training data itself does not have the same image as the second row.


## ❤️&nbsp;&nbsp;Acknowledgement

- [OpenCV](https://github.com/opencv/opencv)
- [BasicSR](https://github.com/XPixelGroup/BasicSR)
```
@misc{wang2020basicsr,
  author =       {Xintao Wang and Ke Yu and Kelvin C.K. Chan and
                  Chao Dong and Chen Change Loy},
  title =        {{BasicSR}: Open Source Image and Video Restoration Toolbox},
  howpublished = {\url{https://github.com/xinntao/BasicSR}},
  year =         {2018}
}
```