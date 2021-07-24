import os
import shutil
import argparse
from yolov5.utils.google_utils import attempt_download


if __name__ == '__main__':
    '''
    Download pre-trained models from YOLOv5 repository
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument('--weights', nargs='+', type=str, default='yolov5s.pt', help='model.pt path(s)')
    opt = parser.parse_args()

    # --img 640 models
    weights_640 = ['yolov5s.pt', 'yolov5m.pt', 'yolov5l.pt', 'yolov5x.pt']

    # --img 1280 models
    weights_1280 = ['yolov5s6.pt', 'yolov5m6.pt', 'yolov5l6.pt', 'yolov5x6.pt']

    weights_repo = weights_640 + weights_1280

    for weights in opt.weights:
        if weights in weights_repo:
            attempt_download(weights)
            shutil.move(src=weights, dst=os.path.join('models', weights))
        else:
            print('File {} is not in YOLOv5 repository'.formatr(weights))
