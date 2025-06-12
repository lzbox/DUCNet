# DUCNet: A Dynamic and Aligned Network for Underwater Detection

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Official PyTorch implementation of the paper:

**DUCNet: A Dynamic and Aligned Network for Underwater Detection**  
Dehua Zhang , Zhen Li , Changcheng Yu, Ruixue Xia  
School of Artificial Intelligence, Henan University  
*Accepted to The Visual Computer (2025)*

---

## 📌 Highlights

- 🎯 **Specialized for Underwater Small Object Detection**  
  Tackles underwater blur, low contrast, small targets, and cluttered backgrounds.

- 🧩 **Modular and Lightweight Architecture**  
  Includes three novel modules: `DCAConv`, `DyLiteFPN`, and `AlignDet`.

- ⚡ **State-of-the-Art Performance**  
  Achieves **85.3% mAP** on DUO and **86.5% mAP** on RUOD with high FPS.

---

## 📁 Project Structure

```plaintext
DUCNet/
├── docker/               
├── docs/             
├── examples/            
├── tests/
├── ultralytics/
├── train.py             
├── dataset.yaml              
├── modocs.yaml     
├── README.md           
└── LICENSE              
