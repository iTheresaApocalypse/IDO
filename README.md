# [IDO: Handling Label Noise via Instance-Level Difficulty Modeling and Dynamic Optimization] Implementation

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-1.12%2B-orange)](https://pytorch.org/)

This repository is the official implementation of the paper "Handling Label Noise via Instance-Level Difficulty
Modeling and Dynamic Optimization". It includes complete training, validation, and inference pipelines.

## 📌 Overview

![Overview](Overview.png)We propose IDO, an Instance-level Difficulty Modeling and Dynamic Optimization framework to achieve robust learning over noisy training data. Rather than relying on hyperparameters to regularize different terms in the loss function, IDO designs a dynamically weighted loss function that captures both the cleanliness and difficulty of each individual sample.
This enables instance-level optimization without introducing any additional hyperparameter.

## 🚀 Key Features

- A simple but robust metric - wrong event
- A dynamic loss function considering clean, hard and noise information
- A two-stage framework using pre-trained models to handle noisy labels

## 📂 Project Structure

```plaintext
.
├── config/               # Training configuration files
├── checkpoint/           # The logs files
├── dataloader/           # Data loading and preprocessing
├── model/                # Model Loading
├── utils/                # Utility scripts
├── stage1/               # Statistical data collected during Stage 1
├── stage2/               # Statistical data collected during Stage 2
├── sh/                   # Execution scripts of different datasets
├── stage_1.py            # Code of Stage 1
├── stage_2.py            # Code of Stage 2 (whole dataset bmm)
├── stage_2_class.py      # Code of Stage 2 (class-based bmm)
└── requirements.txt      # Python dependencies
```

## ⚙️ Environment Setup

```
conda create -n IDO python=3.8
conda activate IDO
pip install -r requirements.txt
```

## 🛠️ Quick Start

```
Data Preparation
Download cifar100, tiny-imagenet, cifar100-N, clothing1m, webvision.
```

Extract files to './data/' directory (create if missing).

### Running Py Files 

Stage 1 Training

```
# real-world dataset
python stage_1.py --config 'config/stage1/[dataset].yaml' 
# synthetic dataset
python stage_1.py --config 'config/stage1/[dataset].yaml' --noise_mode ['sym' 'asym' 'idn'] --noise_ratio [0,1]
```

Stage 2 Training

```
# real-world dataset
python stage_2.py --config 'config/stage2/[dataset].yaml' 
# synthetic dataset
python stage_2.py --config 'config/stage2/[dataset].yaml' --noise_mode ['sym' 'asym' 'idn'] --noise_ratio [0,1]
```

### Running sh Files

```
sh sh/[cifar100.sh, tiny_imagenet.sh,realworld.sh]
```

### Procedure Document

1. After finishing stage 1, the wrong event information and a bar chart will be stored into './stage1'.
2. After finishing stage 1, a competitive base model will be stored into './base_model'.
3. After finishing stage 2, the best accuracy will be stored into './stage2'.
4. The training log files will be stored into './checkpoint'.

## 📊 Results

### CIFAR100

| Model    | Sym.20% | Sym.40% | Sym.60% | Asym.40% | Inst.40% |
| -------- | ------- | ------- | ------- | -------- | -------- |
| ResNet50 | 85.1%   | 83.8%   | 81.4%   | 78.2%    | 83.8%    |
| ViT-B/16 | 92.7%   | 92.4%   | 91.5%   | 89.7%    | 92.3%    |

### Tiny-ImageNet

| Model    | Sym.20% | Sym.50% | Inst.40% |
| -------- | ------- | ------- | -------- |
| ResNet50 | 78.6%   | 75.4%   | 77.5%    |
| ViT-B/16 | 91.3%   | 90.3%   | 90.4%    |

### Real-world Dataset

| Dataset  | CIFAR100N | Clothing1M | Webvision |
| -------- | --------- | ---------- | --------- |
| ResNet50 | 73.6%     | 72.6%      | 82.9%     |
| ViT-B/16 | 81.4%     | 73.0%      | 86.0%     |

## 📜 Citation

```
@inproceedings{IDO,
  title     = {Handling Label Noise via Instance-Level Difficulty Modeling and Dynamic Optimization},
  author    = {Zhang, Kuan and Chai, Chengliang and Xu, Jingzhe and Zhang, Chi and Han, Han and Yuan, Ye and Wang, Guoren and Cao Lei},
  booktitle = {arXiv},
  year      = {2025}
}
```

## 🤝 Contributing

Open an issue or submit a PR. Follow the contribution guidelines.

## 📄 License

MIT License. See LICENSE.

