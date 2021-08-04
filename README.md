# Export YOLOv5 to Google Coral Dev Mini

<p align="center">
  <a href="https://github.com/ultralytics/yolov5/discussions/3213">
  <img width="850" src="https://github.com/ultralytics/yolov5/releases/download/v1.0/banner-export-competition.png"></a>
</p>


Table of contents
=================
- [Step 0: Preparation. Download models](#preparation)
- [Step 1: Convert PyTorch model into TensorFlow Lite](#conversion)
  * [Method 1: via TensorFlow](#convert-tf)
  * [Method 2: via Keras](#convert-keras)
  * [Method 3: via OpenVino](#convert-vino)
- [Step 2: Deploy model on Coral Dev Board Mini](#deployment) 

<a name="preparation"></a>
## Step 0: Preparation. Download models.

Clone the repository implementing inference with YOLOv5 models on Google Coral Dev Board Mini

```
git clone https://github.com/maxmarkov/yolov5-coral-dev-mini.git
```

This repository uses YOLOv5 as submodule. Clone the submodule and checkout the latest stable release (v5.0 on July 24)

```
git submodule init && git submodule update && cd yolov5 && git checkout tags/v5.0
```

Install all necessary requirements 

```
cd .. && pip install -r yolov5/requirements.txt && pip install -r requirements.txt
```

Download PyTorch models from YOLOv5 repository into models folder:

```
python download.py --weights yolov5s.pt yolov5s6.pt 
```
<a name="conversion"></a>
## Step 1: Convert PyTorch model into TensorFlow Lite

Coral Dev Board requires the model to be in a TensorFlow Lite format. 
Custom models should be placed into models folder.

<a name="convert-tf"></a>
### Method 1 (via TensorFlow)


<details><summary>Conversion diagram</summary>
<p>

<img src="data/diagram.png" width="650" height="450">

</p>
</details>

PyTorch to ONNX to TensorFlow to TensorFlow Lite:

```
python export.py --weights models/yolov5s.pt --img 320 --batch 1 --dynamic
```

**Download already converted files**: [onnx](https://drive.google.com/drive/folders/16mC7g1IFVg16HW6ivrn2H148xbGnHtDb?usp=sharing) | [tf](https://drive.google.com/drive/folders/1PZuDDC5TMdiTx_y6l6ultq05Bt2syEt4?usp=sharing) | [tflite](https://drive.google.com/drive/folders/18rw0fv1VmqqUHHjdgU9zbYGkJMY6nJ-z?usp=sharing)

<a name="convert-keras"></a>
### Method 2 (via Keras)

Conversion via keras using [this repository](https://github.com/zldrobit/yolov5)

```
cd yolov5-conversion && python3 models/tf.py --weights ../models/yolov5s.pt --cfg models/yolov5s.yaml --img 320 
```

<a name="convert-vino"></a>
### Method 3 (via OpenVINO IR)

Conversion via OpenVINO IR using [this repository](https://github.com/PINTO0309/openvino2tensorflow)

```
python export.py --weights models/yolov5s.pt --img 320 --batch 1 --dynamic onnx openvino

```

<a name="deployment"></a>
## Step 2: Deploy model on Coral Dev Board Mini 

```
python detect.py --weights models/yolov5s.tflite
```
