# Export YOLOv5 to Google Coral Dev Mini

<p align="center">
  <a href="https://github.com/ultralytics/yolov5/discussions/3213">
  <img width="850" src="https://github.com/ultralytics/yolov5/releases/download/v1.0/banner-export-competition.png"></a>
</p>

## Step 0: Preparation. Download models.

Clone the repository implementing inference with YOLOv5 models on Google Coral Dev Board Mini

```
git clone https://github.com/maxmarkov/yolov5-coral-dev-mini.git
```

This repository uses YOLOv5 as submodule. Clone the submodule and checkout the latest stable release (v5.0 on July 24)

```
cd yolov5 && git submodule init && git submodule update && git checkout tags/v5.0
```

Install all necessary requirements 

```
pip install -r requirements.txt && cd .. && pip install -r requirements.txt
```

Download PyTorch models from YOLOv5 repository into models folder:

```
python download_models.py --weights yolov5s.pt yolov5s6.pt 
```

## Step 1: Convert PyTorch model into TensorFlow Lite

Custom models should be placed into models folder.

<img src="data/diagram.png" width="650" height="450">

### Method 1

### Method 2


## Step 2: Deploy model on Coral Dev Board Mini 
