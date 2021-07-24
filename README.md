# Export YOLOv5 to Google Coral Dev Mini

## Step 0: Preparation. Download models.

Clone the repository implementing inference of YOLOv5 models on Google Coral Dev Board Mini

```
git clone https://github.com/maxmarkov/yolov5-coral-dev-mini.git
```

This repository uses YOLOv5 as submodule. Clone the submodule and checkout the latest stable release (v5.0 on July 24)

```
cd yolov5 && git submodule init && git submodule update && git checkout tags/v5.0
```

Install all necessary requirements 

```
pip install -r requirements && pip install onnx>=1.9.0
```

Download PyTorch models from YOLOv5 repository into models folder:

```
cd .. && python3 download_models.py --weights yolov5s.pt yolov5s6.pt 
```

## Step 1: Convert PyTorch model into TensorFlow Lite

<img src="data/diagram.png" width="650" height="450">



## Step 2: Deploy model on Coral Dev Board Mini 
