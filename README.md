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

Intentionally left blank, will be filled later

</div>

## 📌&nbsp;&nbsp;Introduction

This repository is used for assessment purposes in the image enhancement task. There are three types of enhancements used:

- Enhancement using OpenCV Python
- Enhancement using OpenCV C++
- Enhancement using GAN (Generative Adversarial Network)

The three types will be compared one by one

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

#### GAN
```bash
python BasicSR/inference/inference_esrgan.py \
  --model_path BasicSR/experiments/pretrained_models/ESRGAN/ESRGAN_SRx4_DF2KOST_official-ff704c30.pth \
  --input assets
```

#### Thresholding
```bash
python thresholding.py \
  --input assets/001.png \
  --output results/001-thres.png
```

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